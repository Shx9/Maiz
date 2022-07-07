import os

from flask import Flask, flash, redirect, render_template, request, session
import requests
import json

#Configures application
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    location = request.form.get("location")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=YOUR_API_KEY".format(location)
    payload={}
    headers={}
    response = requests.request("GET", url, headers=headers, data=payload)
    presponse = response.json()
    return render_template('schedule.html', presponse=presponse, location=location)

@app.route('/schedule', methods = ["GET", "POST"])
def schedule():
    if request.method == 'GET':
        return render_template("schedule.html")
    return render_template("scheduled.html")

@app.route('/business', methods = ["GET", "POST"])
def business():
    if request.method == 'GET':
        return render_template("business.html")
    phone = request.form.get("phone")
    if request.form.get("11am_3p")=="11am_3p":
        res = "3 people at 11:00AM."
    elif request.form.get("2pm_2p")=="2pm_2p":
        res = "2 people at 2:00PM."
    elif request.form.get("4pm_5p")=="4pm_5p":
        res = "4 people at 5:00PM."
    url = "https://api.sendblue.co/api/send-message"
    jdict={"number":phone, "content":'You have confirmed your booking for {}'.format(res)}
    headers={"sb-api-key-id": "YOUR_API_KEY",
            "sb-api-secret-key": "YOUR_API_SECRET_KEY",
            "content-type": "application/json"}
    message = requests.post(url, json=jdict, headers=headers)
    return render_template("booked.html")

@app.route('/booked', methods = ["GET"])
def booked():
    return render_template("booked.html")
    