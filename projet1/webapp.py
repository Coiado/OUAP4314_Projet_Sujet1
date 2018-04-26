#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:48:08 2018

@author: coiadoml
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/add')
def home_page():
    monuments = mongo.db.monumentsParis
    passage = monuments.find[{'title':'Passage Brady'}]
    return 'Okay'
#    passage = monuments.find_one({'title':'Passage Brady'})
 #   return passage
     