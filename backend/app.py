from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summary", methods=["POST"])
def summary():
    return render_template("summary.html", input=request.form.get("input"))