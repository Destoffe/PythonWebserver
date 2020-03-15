#!/usr/bin/python
import sys
import Adafruit_DHT
from flask import Flask, request,Response
import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')

app = Flask(__name__)
temperature = 0.0
#Starts the webserver on the localhost with /getWeather
#Reads the temperature files and sends that as the data 
@app.route('/getWeather')
def getWeather():

    file = open("data.txt", "r")
    text = float(file.read())
    data = {
        'temperature' : text

