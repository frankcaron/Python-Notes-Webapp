import os
from flask import Flask

pythonotes = Flask(__name__)
pythonotes.config.from_pyfile('config.py')
from pythonotes import Notes, Notes_REST