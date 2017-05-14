from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

import os
import jinja2
import webapp2
import logging
import json
import urllib
#import MySQLdb
import math

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


@app.route('/')
def index():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render()
    
@app.route('/data')
def data():
    template = JINJA_ENVIRONMENT.get_template('templates/data.html')
    return template.render()

@app.route('/about')
def about():
    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    return template.render()
    
@app.route('/slides')
def slides():
    template = JINJA_ENVIRONMENT.get_template('templates/slides.html')
    return template.render()

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
