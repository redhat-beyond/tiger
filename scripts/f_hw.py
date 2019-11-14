#!/usr/bin/env python3
from flask import Flask

f_app = Flask(__name__)


@f_app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    f_app.run()
