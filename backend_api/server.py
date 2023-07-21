from flask import Flask, request, jsonify, send_file
import sqlite3
import converter
import datetime

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/conversions', methods=['GET', 'POST'])
def conversions():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM conversions')
        res = [
            dict(id=row[0], input=row[1], output=row[2], audio_filename=row[3])
            for row in cursor.fetchall()
        ]
        if len(res) == 0:
            return '', 404
        return jsonify(res), 200
    
    if request.method == 'POST':
        # Parsing input data, accepting both form input and json input
        if request.form.get('input') is None:
            try:
                input_data = request.get_json(force=True)
                input_text = input_data['input']
                create_audio = input_data.get('audio')
            except:
                return 'Please provide key value pair with "input" as the key', 500
        else:
            input_text = request.form.get('input')
            create_audio = request.form.get('audio')

        # Runs the input through the converter summary function
        output = converter.summary(input_text)

        # If there is an option to create audio, create a filename and the associated mp3 file.
        if create_audio:
            current_timestamp = int(datetime.datetime.now().timestamp())
            filename = "audio_user1_" + str(current_timestamp)
            filepath = f"audio_files/{filename}.mp3"
            converter.make_audio(output, filepath)
        else:
            filename = None

        # Add to database and commit
        query = """
            INSERT INTO conversions (raw_input, summary_output, audio_filename)
            VALUES (?, ?, ?)
        """
        cursor.execute(query, (input_text, output, filename))
        conn.commit()
        return jsonify({'id':cursor.lastrowid, 'input':input_text, 'output':output, 'audio_filename': filename}), 200
    
@app.route('/conversions/<int:id>', methods=['GET', 'DELETE'])
def conversionByID(id):
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM conversions WHERE id = ?", (id,))
        res = cursor.fetchone()
        if res is None:
            return 'Not Found', 404
        res_obj = dict(id=res[0], input=res[1], output=res[2], audio_filename=res[3])
        return jsonify(res_obj), 200
    
    if request.method == 'DELETE':
        query = """DELETE FROM conversions WHERE id = ?"""
        conn.execute(query, (id,))
        conn.commit()
        return jsonify({'deleted_id': id}), 200
    
@app.route('/audio/<filename>')
def audio(filename):
    return send_file(f'audio_files/{filename}.mp3')


if __name__ == '__main__':
    app.run(debug=True)
