PythonNoteService
=================

A simple note storage and editing web service written in Python to be consumed by apps.

The end-goal of this service will be to serve a RESTful API which persists, updates, creates, and deletes notes
on the cloud. This API will be consumed by device apps that provide the UX for the service.

There will be three total repositories when complete:
- PythonNoteService
- iOSNoteApp
- RubyOnRailsNoteWebPortal

This should be fun. Contributions, comments, and criticisms of my sloppy code welcome!

Contributors
=================
Frank Caron, 2013  
http://frankcaron.com

Design
=================

NotesService
------

The note service will be a simple service designed to store, retrieve, and update written notes. Think of it like “Evernote Lite”. This service will be exposed via a REST API. That API will then be consumed by mobile apps and a simple Python-based web front-end.

Classes
------

**Class: Note (Model)**

This is the base note class for a Note object which will contain the content.

*Attributes:*

Note name str  
Note creator str  
Note content str_long  
Note title (computed) str  

*Functions:*

create_note (cls, creator, content)  
update_note(cls, content)  
determine_title  
creates the title from the content; finds first line break  

**Class: Notepad (Model)**

This is the notes array for manipulating notes.

*Attributes:*

Array of notes  

*Functions:*

create_new_note(cls, position)  
retrieve_new_note(cls, position)    
delete_note(cls, position)

**Class: Publisher (Controller)**

This is the publisher class to expose note CRUD over REST.

*Attributes:*

notepad  
rest_connector  
database_connector  

*Functions:*

accept_web_request  
handle_web_request  

**Class: Bookcase (View/Template)**

This is the web view for displaying the notes; consumes REST API.

*Functions:*

accept_user_input  
handle_user_input  

NotesDB
------

Simple database model to store notes

note_id as INT AUTOINC PK  
notepad_id as INT AUTOINC  
creator as TEXT  
date_created as DATE  
title as STRING  
content as STRING  
