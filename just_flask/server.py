from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
import converter
import sqlite3
import os

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except sqlite3.error as e:
        print(e)
    return conn

def format_time(timestamp):
    formatted = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return formatted

@app.route('/')
def home():
    return render_template("home.html", page_name = "Home")

@app.route("/about")
def about():
    return render_template("about.html", page_name = "About")

@app.route("/summariser")
def summariser():
    return render_template("summariser.html", page_name="Summariser")

@app.route("/history")
def history():
    conn = db_connection()
    cursor = conn.cursor()  
    cursor.execute('SELECT * FROM conversions')
    result = [
        dict(id=row[0], 
             input=row[1], 
             output=row[2], 
             timestamp=format_time(row[3]), 
             filename=row[4])
        for row in cursor.fetchall()
    ]
    return render_template("history.html", past_conversions=result, page_name="History")

@app.route("/output", methods=["POST", "GET"])
def output():
    # Connect to database
    conn = db_connection()
    cursor = conn.cursor()

    # Initialize from form, run summarizer and or audio creator
    input = request.form.get("input")
    create_audio = request.form.get("audio") == "on"
    output = converter.auto_summary(input)
    timestamp = int(datetime.now().timestamp())
    if create_audio:
        filename = f'audio_{timestamp}'
        filepath = f'static/audio/{filename}.mp3'
        converter.make_audio(output, filepath=filepath)
    else:
        filename = None
    
    # Update database
    query = """
            INSERT INTO conversions (input, output, timestamp, audio)
            VALUES (?, ?, ?, ?)
        """
    cursor.execute(query, (input, output, timestamp, filename))
    conn.commit()
    return render_template("output.html", input=input, filename=filename, output=output, timestamp=format_time(timestamp), page_name="Output")
    
@app.route("/delete/<int:id>")
def delete(id):
    conn = db_connection()
    cursor = conn.cursor()
    # Find and delete audio file if any
    query = """SELECT audio FROM conversions WHERE id = ?"""
    cursor.execute(query, (id,))
    try:  
        audio_file = cursor.fetchone()[0]
    except:
        audio_file = None
    path = os.path.join(os.getcwd(), 'static', 'audio', f"{audio_file}.mp3")
    if os.path.exists(path):
        os.remove(path)
    # Delete conversion from database
    query = """DELETE FROM conversions WHERE id = ?"""
    cursor.execute(query, (id,))
    conn.commit()
    return redirect("/history")

if __name__ == "__main__":
    app.run(debug=True)