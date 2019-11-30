#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home.html')
	
@app.route('/')
def Subscribe():
    return render_template('#')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
