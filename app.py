#!/usr/bin/env python3
from flask import Flask, render_template, request, session, redirect, url_for
import logging
from flask_debugtoolbar import DebugToolbarExtension
from mysql import connector
from passlib.hash import sha256_crypt

app = Flask(__name__)

# !--- For debugging switch to true ---!
app.debug = False

app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"
toolbar = DebugToolbarExtension(app)


def definedlog(fileHandler):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler(fileHandler)
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def connect_db(host, user, password, database):
    connection = connector.connect(
        user=user, password=password, host=host, database=database)
    return connection


conn = connect_db('localhost', 'root', 'LoginPass@@11223344', 'tiger')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        userDetails = request.form
        username = userDetails['username']
        password = sha256_crypt.encrypt(userDetails["password"])
        mycursor = conn.cursor()
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        conn.commit()
        # if authenticate_user(username, password):
        session["USERNAME"] = username
        session["PASSWORD"] = password
        return redirect(url_for('send_message'))
    return render_template('/sign_up.html')


@app.route('/')
def home():
    return render_template('/home.html')


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        userDetails = request.form
        username = session["USERNAME"]
        msg = userDetails['content']
        mycursor = conn.cursor()
        sql = "INSERT INTO messages (username, content) VALUES (%s, %s)"
        val = (username, msg)
        mycursor.execute(sql, val)
        conn.commit()
        return redirect(url_for('messages_view'))
    return render_template('/send_message.html')


def check_username(username, pas):
    maulers = conn.cursor()
    Fender = "SELECT * FROM users"
    maulers.execute(Fender)
    result = maulers.fetchall()
    for user in result:
        print(user)
        if user[0] == username:
            if sha256_crypt.verify(pas, user[1]):
                return True
    return False


def authenticate_user(username, password):
    if check_username(username, password):
        return True
    return False


@app.route('/messages_view', methods=['GET', 'POST'])
def messages_view():
    message = conn.cursor()
    if request.method == "POST":
        word = request.form['word']
        message.execute("SELECT * FROM tiger.messages WHERE content LIKE %s" +
                        "ORDER BY create_date DESC", ("%{}%".format(word),))
        view = message.fetchall()
        return render_template('/messages_view.html', view=view)
    message.execute("SELECT * FROM tiger.messages ORDER BY create_date DESC")
    view = message.fetchall()
    return render_template('/messages_view.html', view=view)


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == "POST":
        req = request.form
        username = req.get("username")
        password = req.get("password")
        if authenticate_user(username, password):
            session["USERNAME"] = username
            session["PASSWORD"] = password
            return redirect(url_for('send_message'))
        else:
            return redirect(url_for('log_in'))
        return render_template('send_message.html',
                               username=session["USERNAME"])
    return render_template('/sign_in.html')


@app.route('/log_out')
def log_out():
    session.clear()
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
