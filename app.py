#!/usr/bin/env python3
from flask import Flask, render_template, session, request
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

@app.route('/')
def Home():
	if not session.get("EMAIL") is None:
		return render_template('Home.html' , email=session["EMAIL"])
	else:
		return render_template('Home.html')

@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')

@app.route('/signup',methods=["GET", "POST"])
def sign_up():
	if request.method == "POST":
		req = request.form
		email = req.get("email")
		password = req.get("password")
		session["EMAIL"]=email
		session["PASSWORD"]=password
		return render_template('Home.html',email=session["EMAIL"])
	return render_template('/sign-up.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
