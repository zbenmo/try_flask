from flask import Flask, render_template, url_for
from markupsafe import escape


app = Flask(__name__)


@app.route("/<name>")
def hello_world(name):
    return render_template('hello.html', name=name)


# with app.test_request_context():
#     print(url_for("hello_world", name='<script>alert("bad")</script>'))

def show_the_login_form():
    return "login here:"


@app.get('/login')
def login_get():
    return show_the_login_form()


def do_the_login():
    return "okay, you are now logged-in"


@app.post('/login')
def login_post():
    return do_the_login()