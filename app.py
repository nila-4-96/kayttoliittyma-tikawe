from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Tähän tulee käyttöliittymä."

@app.route("/page1")
def index():
    return "Tämä on sivu 1"

@app.route("/page2")
def index():
    return "Tämä on sivu 2"
