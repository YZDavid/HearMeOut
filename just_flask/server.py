from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
import converter
import sqlite3
import os

app = Flask(__name__)

DATABASE_COLS = ("id", "input", "output", "timestamp", "audio", "performance", "input_percent", "method")

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

@app.route("/url_summariser")
def url_summariser():
    return render_template("url_summariser.html", page_name="URL Summariser")

@app.route("/latest")
def output():
    conn = db_connection()
    cursor = conn.cursor()  
    query = """
            SELECT * FROM conversions
            ORDER BY timestamp DESC
            LIMIT 1
        """
    res = cursor.execute(query)
    summary = res.fetchone()
    if summary == None:
        return render_template('latest.html', summary=None, page_name="Latest")
    
    result = dict()
    for i in range(len(summary)):
        field = DATABASE_COLS[i]
        if field == 'timestamp':
            result[field] = format_time(summary[i])
        else:
            result[field] = summary[i]
    
    return render_template("latest.html", summary=result, page_name = "Latest")


@app.route("/history")
def history():
    conn = db_connection()
    cursor = conn.cursor()  
    query = """
            SELECT * FROM conversions
            ORDER BY timestamp DESC
        """
    cursor.execute(query)
    result = []
    for row in cursor.fetchall():
        d = dict()
        for i in range(len(row)):
            field = DATABASE_COLS[i]
            if field == "timestamp":
                d[field] = format_time(row[i])
            else:
                d[field] = row[i]
        result.append(d)
    return render_template("history.html", past_summaries=result, page_name="History")

@app.route("/summarise", methods=["POST"])
def summarise():
    # Connect to database
    conn = db_connection()
    cursor = conn.cursor()

    # Initialize input data from request.form
    input = request.form.get("input")
    create_audio = request.form.get("audio") == "on"
    percentage = request.form.get("percentage")

    # Summarisation style based on input
    if percentage:
        percentage = int(percentage)
        output = converter.summary(input, percentage)
    else:
        output = converter.summary(input)
    performance = round((len(output) / len(input)) * 100, 2)

    # Creation of audio if specified
    timestamp = int(datetime.now().timestamp())
    if create_audio:
        filename = f'audio_{timestamp}'
        filepath = f'static/audio/{filename}.mp3'
        converter.make_audio(output, filepath=filepath)
    else:
        filename = None
    
    # Update database, note that database does not need an ID as it will be auto-assigned
    query = """
            INSERT INTO conversions
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
    database_input = (None, input, output, timestamp, filename, performance, percentage, "text")
    cursor.execute(query, database_input)
    conn.commit()

    # Create dictionary object to pass to render template. Note that timestamp is changed to human readable format.
    timestamp = format_time(timestamp)
    database_input = (None, input, output, timestamp, filename, performance, percentage, "text")
    result = dict()
    for i in range(len(database_input)):
        field = DATABASE_COLS[i]
        result[field] = database_input[i]
    
    return render_template("latest.html", summary=result, page_name="Output")

@app.route("/url_summarise", methods=["POST"])
def url_summarise():
    # Connect to database
    conn = db_connection()
    cursor = conn.cursor()

    # Initialize input data from request.form
    input = request.form.get("url_input")
    create_audio = request.form.get("audio") == "on"

    # Call Summarisation function
    try:
        original_len, output = converter.url_summary(input)
    except:
        return render_template("url_summariser.html", error=True, page_name="URL Summariser")
    performance = round((len(output) / original_len) * 100, 2)

    # Creation of audio if specified
    timestamp = int(datetime.now().timestamp())
    if create_audio:
        filename = f'audio_{timestamp}'
        filepath = f'static/audio/{filename}.mp3'
        converter.make_audio(output, filepath=filepath)
    else:
        filename = None
    
    # Update database, note that database does not need an ID as it will be auto-assigned
    query = """
            INSERT INTO conversions
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
    database_input = (None, input, output, timestamp, filename, performance, None, "url")
    cursor.execute(query, database_input)
    conn.commit()

    # Create dictionary object to pass to render template. Note that timestamp is changed to human readable format.
    timestamp = format_time(timestamp)
    database_input = (None, input, output, timestamp, filename, performance, None, "url")
    result = dict()
    for i in range(len(database_input)):
        field = DATABASE_COLS[i]
        result[field] = database_input[i]
    
    return render_template("latest.html", summary=result, page_name="Output")
    
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

@app.route("/testing", methods=["POST"])
def test():
    url = request.form.get('input')
    result = converter.news_summary(url)
    return result

if __name__ == "__main__":
    app.run(debug=True)