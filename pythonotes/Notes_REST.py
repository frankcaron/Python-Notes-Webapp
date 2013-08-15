#
# Module: Notes REST Controller
# 
# This controller handles REST calls 
# via Flask
# 
# 2013, Frank Caron

# Imports
from pythonotes import pythonotes
from pythonotes import DBHelper
from pythonotes import Notes
import json
from flask import abort, request, jsonify

temp_helper = DBHelper.DBReader()
temp_writer = DBHelper.DBWriter()
temp_deleter = DBHelper.DBDeleter()

@pythonotes.route('/')
@pythonotes.route('/index')
def index():
    return "Frank's humble python web service beginnings, now with notes. And fun."

# REST Handlers
# -------------------

# ============================
#
# GETs
#  
# ============================

# Notes - GET
# Return collection of notes
@pythonotes.route('/notes/', methods = ['GET'])
def get_all_notes(): 
    temp = temp_helper.db_read_all()
    return jsonify( { 'notes': temp } )

# Note - GET
# Return a specified notes resource
@pythonotes.route('/notes/<int:note_id>', methods = ['GET'])
def get_specific_note(note_id): 
    temp = temp_helper.db_read_specific(note_id)
    if len(temp) == 0:
        abort(404) 
    return jsonify( { 'notes': temp } )
    
# Notepad - Get
# Returns all the notes associated with a specific notepad    
@pythonotes.route('/notepad/<int:notepad_id>', methods = ['GET'])
def get_specific_notepad(notepad_id): 
    temp = temp_helper.db_read_specific_notepad(notepad_id)
    if len(temp) == 0:
        abort(404) 
    return jsonify( { 'notes': temp } )
    
# Last Note Created - GET
# Returns the row ID for the last row created
@pythonotes.route('/notes/lastid', methods = ['GET'])
def get_last_note_id():
    return jsonify( { 'note_id': temp_helper.db_get_last_row_id() } )
    
# ============================
#
# POSTs
#  
# ============================

# Create Note - POST
# Returns the row ID for the last row created
    
# No spaces in function values    
@pythonotes.route('/notes/', methods=['POST'])
def make_new_note():
    if not request.json or not 'note_content' in request.json or not 'note_creator' in request.json:
        abort(400)
    temp_writer.db_create_note(request.json['note_content'], request.json['note_creator'], int(temp_helper.db_get_last_row_id()) + 1);
    # Figure out who the user is to isolate the notepad
    # retrieve the notepad object associated
    # create a new note with the content
    return jsonify( { 'note_id': temp_helper.db_get_last_row_id() } ), 201    
    
# ============================
#
# DELETEs
#  
# ============================

# Create Note - POST
# Returns the row ID for the last row created
    
@pythonotes.route('/notes/<int:note_id>', methods = ['DELETE'])
def delete_specific_note(note_id):
    #Check to see if a note with that ID actually exists
    #if not request.json or not 'note_content' in request.json or not 'note_creator' in request.json:
    #    abort(400)
    #
    temp_deleter.db_delete(note_id);
    return jsonify( { 'note_id': temp_helper.db_get_last_row_id() } ), 200 