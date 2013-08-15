try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        raise ImportError
from werkzeug import Response

from flask import jsonify

def status_jsonify(args, status_code=None):
	res = jsonify(args)
	if status_code: res.status_code = status_code
	return res

def register_error_handlers(app):
	@app.errorhandler(404)
	def page_not_found(e):
		data = {'error':'fuck this sucks'}
		r = status_jsonify(data, status_code=404)
		return r