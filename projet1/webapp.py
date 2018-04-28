#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:48:08 2018

@author: coiadoml
"""

from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pprint


#app.config['MONGO_DBNAME'] = 'DataEngineering'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017'
app = Flask(__name__)
address= []

mongo = PyMongo(app)

client = MongoClient('localhost', 27017)

db = client.DataEngineering


@app.route('/search', methods=['GET', 'POST'])
def search():
    monuments = db.monumentsParis
    title = request.form['title']
    list = monuments.find( { 'title':title } )
    for i in list:
        address.append(i['adresse'])
    return render_template('index.html',myvar = 'Example',links= address)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html',myvar = 'Example')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
