from flask import Flask, request, jsonify
import sqlite3

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
            dict(id=row[0], input=row[1], output=row[2])
            for row in cursor.fetchall()
        ]
        if len(res) == 0:
            return '', 404
        return jsonify(res), 200
    
    if request.method == 'POST':
        if request.form.get('input') is None:
            try:
                input_data = request.get_json(force=True)
                print(input_data)
                input_text = input_data['input']
            except:
                return 'Please provide key value pair with "input" as the key', 500
        else:
            input_text = request.form.get('input')
        output = input_text[:20]
        query = """
            INSERT INTO conversions (raw_input, summary_output)
            VALUES (?, ?)
        """
        cursor.execute(query, (input_text, output))
        conn.commit()
        return jsonify({'id':cursor.lastrowid, 'input':input_text, 'output':output}), 200
    
@app.route('/conversions/<int:id>', methods=['GET', 'DELETE'])
def conversionByID(id):
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM conversions WHERE id = ?", (id,))
        res = cursor.fetchone()
        if res is None:
            return 'Not Found', 404
        res_obj = dict(id=res[0], input=res[1], output=res[2])
        return jsonify(res_obj), 200
    
    if request.method == 'DELETE':
        query = """DELETE FROM conversions WHERE id = ?"""
        conn.execute(query, (id,))
        conn.commit()
        return jsonify({'deleted_id': id}), 200

if __name__ == '__main__':
    app.run(debug=True)
