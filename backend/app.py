from flask import Flask, render_template, request, url_for
from transformers import pipeline
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import pyttsx3
import os

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
engine = pyttsx3.init()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///output.db'
db = SQLAlchemy(app)

class Output(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_field = db.Column(db.Text, nullable=False)
    output_field = db.Column(db.Text, nullable=False)
    audio_path = db.Column(db.String(200))
    date = db.Column(db.DateTime)    

INPUT = None
OUTPUT = None
AUDIO = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summary", methods=["POST", "GET"])
def summary():
    if request.method == "POST":
        input = request.form.get("input")
        output = summarizer(input, max_length=250, min_length=200, do_sample=False)[0]['summary_text']
        # filename is audio_timestamp in windows file friendly format, no illegal characters such as ':'
        filename = f'audio_{datetime.now()}.mp3'.replace(':', '.')
        engine.save_to_file(output, 'test.mp3')
        engine.runAndWait()
        # pyttsx3 is only able to create output files such as 'test.mp3' for some reason, just output as such and use os library to rename file
        os.rename('test.mp3', f'static/{filename}')
        global INPUT, OUTPUT, AUDIO
        INPUT, OUTPUT, AUDIO = input, output, filename
        return render_template("summary.html", input=input, output=output, audio=filename)
    else:
        try:
            return render_template("summary.html", input=INPUT, output=OUTPUT, audio=AUDIO)
        except:
            return render_template("summary.html")


@app.route("/saved")
def saved():
    return render_template("saved.html")