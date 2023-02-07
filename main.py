import json
import requests
from flask import Flask, redirect, url_for, render_template, session, request
from secret import secret_key, site_key, re_key
from handlers.db import Users

users = Users()
app = Flask(__name__)
app.secret_key = secret_key

def is_human(captcha_response):
    secret = re_key
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']

@app.route("/")
def index():
    if 'logined' in session:
        return "<p>Hello, World!</p>"
    else:
        return redirect(url_for('login'))


@app.route("/register")
def register():
    return render_template('register.html', site_key = site_key)

@app.route("/sign_up", methods = ['POST'])
def sign_up():
    if is_human(request.form['g-recaptcha-response']):

        login = request.form['email']
        password = request.form['password']
        if users.is_correct(login, password):
            return 'User is already exists!'
        else:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            users.register(login, password, firstname, lastname)
            user = users.get(login)
            session['logined'] = True
            session['user'] = user
            return 'true'
    else:
        return 'Please prove that You are not a robot!'

@app.route("/sign_in", methods = ['POST'])
def sign_in():
    if is_human(request.form['g-recaptcha-response']):

        login = request.form['email']
        password = request.form['password']
        if users.is_correct(login, password):
            user = users.get(login)
            session['logined'] = True
            session['user'] = user
            return 'true'
        else:
            return 'Invalid login or password!'
    else:
        return 'Please prove that You are not a robot!'

@app.route("/login")
def login():
    return render_template('login.html', site_key = site_key)

if __name__ == '__main__':

    app.run()