import sys
import os
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)