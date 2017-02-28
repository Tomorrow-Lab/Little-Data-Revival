# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import sys
sys.path.insert(0, '/home/pi/Documents/')

import DarkSky
from flask import Flask, jsonify, render_template, request
import serial, time

ser = serial.Serial('/dev/ttyACM0',9600)
app = Flask(__name__)

@app.route('/_push_text')
def push_text():
    t = request.args.get('t', 0, type=str)
    ser.write(t.encode())
    ser.write('#'.encode())
    return jsonify(result=a + b + c)

@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=int)
    ser.write(bytes([a,b,c]))
    return jsonify(result=a + b + c)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
