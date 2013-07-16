#
# Module: Notes REST Controller
# 
# This controller handles REST calls 
# via Flask
# 
# 2013, Frank Caron

#Imports
from pythonotes import pythonotes
from pythonotes import DBHelper

#Object
tempHelper = DBHelper.DBReader()

@pythonotes.route('/')
@pythonotes.route('/index')
def index():
    return "Frank's humble python web service beginnings, now with notes."

#REST Controller
from flask import jsonify

@pythonotes.route('/notes/', methods = ['GET'])
def get_tasks():
    return jsonify( { 'notes': tempHelper.db_get_last_row_id() } )