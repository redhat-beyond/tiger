#!/usr/bin/env python3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')


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
