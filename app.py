#!/usr/bin/env python3
from flask import Flask, render_template, request
import logging
from mysql import connector

app = Flask(__name__)


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


@app.route('/log_in', methods=['GET', 'POST'])
# TODO write logic to this function
def log_in():
    if request.method == 'POST':
        return render_template('home.html')
    return render_template('/sign_up.html')


@app.route('/log_out')
# TODO after seesion will be merge write this function
def log_out():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
