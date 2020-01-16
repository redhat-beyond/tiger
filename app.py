#!/usr/bin/env python3
from flask import Flask, render_template, request, session
import logging
from mysql import connector

app = Flask(__name__)

app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"


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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')


@app.route('/messages_view')
def messages_view():
    message = conn.cursor()
    message.execute("SELECT * FROM tiger.messages ORDER BY create_date DESC")
    view = message.fetchall()
    return render_template('/messages_view.html', view=view)


def search_messages(conn):
    filter = conn.cursor()
    word = input()
    filter.execute("SELECT * FROM tiger.messages WHERE content LIKE % s" +
                   "ORDER BY create_date DESC", (" % {} % ".format(word),))
    filtering = filter.fetchall()
    return filtering


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == "POST":
        req = request.form
        email = req.get("email")
        password = req.get("password")
        session["EMAIL"] = email
        session["PASSWORD"] = password
        return render_template('Home.html', email=session["EMAIL"])
    return render_template('/sign_up.html')


@app.route('/log_out')
def log_out():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')


def check_username(username):
    maulers = conn.cursor()
    Fender = "SELECT * FROM users WHERE username  =" + username
    maulers.execute(Fender)
    result = maulers.fetchall()
    if not result:
        # the user doesnt exist
        return False
    else:
        # the user exists
        return True
