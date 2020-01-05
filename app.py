#!/usr/bin/env python3
from flask import Flask, render_template
import mysql.connector

app=Flask(_name_)

mydb=mysql.connector.connect(host = "localhost",user = "root",passwd = "LoginPass@@11223344",database = "tiger")


@app.route('/')
def Home():
    return render_template('Home.html')


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

def check_username(us):
    maulers = mydb.cursor()

    Fender = "SELECT * FROM users WHERE username  ="+ us

    maulers.execute(Fender)

    result = mycursor.fetchall()

    if not result:
        # the user doesnt exist
        return false
    else:
        # the user exists
        return true







