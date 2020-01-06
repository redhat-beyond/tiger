#!/usr/bin/env python3
from flask import Flask, render_template, request, session


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


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
	if request.method == "POST":
		req = request.form
		email = req.get("email")
		password = req.get("password")
		session["EMAIL"]=email
		session["PASSWORD"]=password
		return render_template('Home.html',email=session["EMAIL"])
	return render_template('/sign_up.html')
# TODO write logic to this function

@app.route('/log_out')
# TODO after seesion will be merge write this function
def log_out():
    return render_template('Home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
