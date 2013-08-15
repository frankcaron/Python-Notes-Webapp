import os
from flask import Flask
from errors import register_error_handlers

pythonotes = Flask(__name__)
pythonotes.config.from_pyfile('config.py')
register_error_handlers(pythonotes)
from pythonotes import Notes, Notes_REST