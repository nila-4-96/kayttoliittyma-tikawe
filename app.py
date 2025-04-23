import sqlite3
import os
import math, time, secrets, markupsafe
from flask import Flask
from flask import redirect, render_template, request, session, abort, url_for, make_response, flash, g
import config, forum, users
from functools import wraps

app = Flask(__name__)
app.secret_key = config.secret_key

DATABASE_FILE = "database.db"
SCHEMA_FILE = "schema.sql"

if not os.path.exists(DATABASE_FILE):
    with sqlite3.connect(DATABASE_FILE) as conn, open(SCHEMA_FILE, "r") as f:
        conn.executescript(f.read())


def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403, "CSRF-virhe.")


@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    page_size = 10
    thread_count = forum.get_thread_count()
    page_count = math.ceil(thread_count / page_size)
    page_count = max(page_count, 1)

    if page < 1:
        return redirect("/1")
    if page > page_count:
        return redirect("/" + str(page_count))

    threads = forum.get_threads(page, page_size)
    return render_template("index.html", page=page, page_count=page_count, threads=threads)


@app.route("/search")
def search():
    query = request.args.get("query")
    type = request.args.getlist("type")
    status = request.args.getlist("status")
    priority = request.args.getlist("priority")
  
    results = forum.search(query, type, status, priority) if query or type or status or priority else []
    return render_template("search.html", query=query, type=type, status=status, priority=priority, results=results)


@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    messages = users.get_messages(user_id)
    return render_template("user.html", user=user, messages=messages)


@app.route("/thread/<int:thread_id>")
def show_thread(thread_id):
    thread = forum.get_thread(thread_id)
    if not thread:
        abort(404)
    messages = forum.get_messages(thread_id)
    return render_template("thread.html", thread=thread, messages=messages)


@app.route("/new_thread", methods=["POST"])
@require_login
def new_thread():
    check_csrf()

    title = request.form["title"]
    content = request.form["content"]

    type = request.form["type"]
    status = request.form["status"]
    priority = request.form["priority"]

    if not title or len(title) > 100 or len(content) > 5000:
        abort(403, "VIRHE: Otsikko tai viesti on liian pitkä.")
    user_id = session["user_id"]

    thread_id = forum.add_thread(title, content, type, status, priority, user_id)
    return redirect("/thread/" + str(thread_id))


@app.route("/new_message", methods=["POST"])
@require_login
def new_message():
    check_csrf()

    content = request.form["content"]
    if len(content) > 5000:
        abort(403, "VIRHE: Viesti on liian pitkä.")
    user_id = session["user_id"]
    thread_id = request.form["thread_id"]

    type = request.form.get("type")
    status = request.form.get("status")
    priority = request.form.get("priority")

    try:
        forum.add_message(content, user_id, thread_id, type, status, priority)
    except sqlite3.IntegrityError:
        abort(403, "IntegrityError")

    return redirect("/thread/" + str(thread_id))


@app.route("/edit/<int:message_id>", methods=["GET", "POST"])
@require_login
def edit_message(message_id):
    message = forum.get_message(message_id)
    if not message or message["user_id"] != session["user_id"]:
        abort(403, "VIRHE: Voit muokata vain omia viestejä.")

    if request.method == "GET":
        return render_template("edit.html", message=message)

    if request.method == "POST":
        check_csrf()
        content = request.form["content"]
        if len(content) > 5000:
            abort(403, "VIRHE: Viesti on liian pitkä.")
        forum.update_message(message["id"], content)
        return redirect("/thread/" + str(message["thread_id"]))


@app.route("/remove/<int:message_id>", methods=["GET", "POST"])
@require_login
def remove_message(message_id):
    message = forum.get_message(message_id)
    if not message or message["user_id"] != session["user_id"]:
        abort(403, "VIRHE: Voit poistaa vain omat viestit.")

    if request.method == "GET":
        return render_template("remove.html", message=message)

    if request.method == "POST":
        check_csrf()
        if "continue" in request.form:
            forum.remove_message(message["id"])
        return redirect("/thread/" + str(message["thread_id"]))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", filled={})

    if request.method == "POST":
        username = request.form["username"]
        if not username:
            abort(403, "VIRHE: Käyttäjätunnus on pakollinen.")
        if len(username) < 3 or len(username) > 16:
            abort(403, "VIRHE: Käyttäjätunnuksen on oltava 3-16 merkin pituinen.")
        password1 = request.form["password1"]
        password2 = request.form["password2"]

    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat, ole hyvä ja kokeile uudestaan.", "error")
        filled = {"username": username}
        return render_template("register.html", filled=filled)

    try:
        users.create_user(username, password1)
        flash("Tunnus luotu, voit nyt kirjautua sisään.", "success")
        return redirect("/login")
    except sqlite3.IntegrityError:
        flash("VIRHE: tunnus on jo varattu. Ole hyvä ja kokeile toista tunnusta.", "error")
        filled = {"username": username}
        return render_template("register.html", filled=filled)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["csrf_token"] = secrets.token_hex(16)
            flash("Olet kirjautunut sisään.", "success")
            return redirect("/")
        else:
            flash("VIRHE: väärä tunnus tai salasana, ole hyvä ja kokeile uudestaan.", "error")
            return render_template("login.html")


@app.route("/logout")
@require_login
def logout():
    del session["user_id"]
    return redirect("/")


@app.route("/add_image", methods=["GET", "POST"])
@require_login
def add_image():
    if request.method == "GET":
        return render_template("add_image.html")

    if request.method == "POST":
        check_csrf()
        file = request.files["image"]
        if not file.filename.endswith(".jpg"):
            flash("VIRHE: Lähettämäsi tiedosto ei ole jpg-tiedosto")
            return redirect("/add_image")

        image = file.read()
        if len(image) > 100 * 1024:
            flash("VIRHE: Lähettämäsi tiedosto on liian suuri")
            return redirect("/add_image")

        user_id = session["user_id"]
        users.update_image(user_id, image)
        flash("Kuva on onnistuneesti lisätty.")
        return redirect("/user/" + str(user_id))


@app.route("/image/<int:user_id>")
def show_image(user_id):
    image = users.get_image(user_id)
    if not image:
        abort(404, "VIRHE: Kuvaa ei ole.")

    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image/jpeg")
    return response


@app.before_request
def before_request():
    g.start_time = time.time()


@app.after_request
def after_request(response):
    elapsed_time = round(time.time() - g.start_time, 2)
    print("elapsed time:", elapsed_time, "s")
    return response


@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)