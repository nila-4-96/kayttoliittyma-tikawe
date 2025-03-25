from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page1")
def page1():
    return "Tämä lienee sivu 1"

@app.route("/page2")
def page2():
    return "Tämä lienee sivu 2"

@app.route("/test")
def test():
    content = ""
    for i in range(1, 101):
        content += str(i) + " "
    return content

@app.route("/page/<int:page_id>")
def page(page_id):
    return "Tämä on sivu " + str(page_id)
