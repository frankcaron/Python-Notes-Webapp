import os
from flask import Flask

pythonotes = Flask(__name__)
from pythonotes import Notes, Notes_REST