from flask import Flask
from flask import render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    db = sqlite3.connect("database.db")
    db.execute("INSERT INTO visits (visited_at) VALUES (datetime('now'))")
    db.commit()
    result = db.execute("SELECT COUNT(*) FROM visits").fetchone()
    count = result[0]
    db.close()
    return "Sivua on ladattu " + str(count) + " kertaa"

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/result", methods=["POST"])
def result():
    pizza = request.form["pizza"]
    extras = request.form.getlist("extra")
    message = request.form["message"]
    return render_template("result.html", pizza=pizza, extras=extras, message=message)

@app.route("/page/<int:page_id>")
def page(page_id):
    return "Tämä lienee sivu " + str(page_id)
