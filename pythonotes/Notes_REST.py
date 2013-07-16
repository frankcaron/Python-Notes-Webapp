#Hello World
from pythonotes import pythonotes

@app.route('/')
@app.route('/index')
def index():
    return "Frank's humble python web service beginnings, now with notes."

#REST Controller
from flask import jsonify

notes = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'content': u'Milk, Cheese, Pizza, Fruit, Tylenol' 
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'content': u'Need to find a good Python tutorial on the web' 
    }
]

@app.route('/notes/', methods = ['GET'])
def get_tasks():
    return jsonify( { 'notes': notes } )