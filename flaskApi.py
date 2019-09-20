# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:32:26 2019

@author: salam thabet
"""

from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class MLClassifier(Resource):
    def get(self):
        return{'label':'apple'}
api.add_resource(MLClassifier,'/classifier')


if __name__ == '__name__':
    app.run()