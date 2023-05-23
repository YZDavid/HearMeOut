from flask import Flask, render_template, request, url_for
from transformers import pipeline
from datetime import datetime
import pyttsx3
import os

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
engine = pyttsx3.init()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summary", methods=["POST", "GET"])
def summary():
    input = request.form.get("input")
    output = summarizer(input, max_length=250, min_length=100, do_sample=False)[0]['summary_text']
    # filename is audio_timestamp in windows file friendly format, no illegal characters such as ':'
    filename = f'audio_{datetime.now()}.mp3'.replace(':', '.')
    engine.save_to_file(output, 'test.mp3')
    engine.runAndWait()
    # pyttsx3 is only able to create output files such as 'test.mp3' for some reason, just output as such and use os library to rename file
    os.rename('test.mp3', f'static/{filename}')
    return render_template("summary.html", input=input, output=output, audio=filename)