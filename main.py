from flask import Flask, redirect, url_for, render_template, session
from secret import secret_key

app = Flask(__name__)
app.secret_key = secret_key

@app.route("/")
def index():
    if 'logined' in session:
        return "<p>Hello, World!</p>"
    else:
        return redirect(url_for('login'))

@app.route("/register")
def register():
    return "<p>Hello, World!</p>"

@app.route("/sign_in")
def sign_in():
    session['logined'] = True
    return redirect(url_for('index'))
@app.route("/login")
def login():
    return "<a href='/sign_in'>login</a>"

if __name__ == '__main__':
    app.run()