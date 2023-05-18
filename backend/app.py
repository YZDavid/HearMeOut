from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summary")
def summary():
    return render_template("summary.html", input=request.args.get("input"))