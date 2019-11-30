#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
