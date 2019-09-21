# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:32:26 2019

@author: salam thabet
"""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '<h1> Hello from flask </h1>'

if __name__ == '__name__':
    app.run()