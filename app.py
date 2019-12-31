#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/templates')


@app.route("/")
def Home():
    return render_template('Home.html')


#@app.route('/contact_us')
#def contact_us():
#    return render_template('/contact_us.html')


if __name__ == '__main__':
    app.run(host="localhost")
