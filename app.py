import sys
from flask import Flask, render_template, url_for, request
from generator import generate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    code_snippet = generate(text)
    return render_template("code.html", code_snippet=code_snippet)


if __name__ == "__main__":
    app.run(debug=True)