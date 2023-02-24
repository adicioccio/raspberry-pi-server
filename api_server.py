import flask
from flask import request, jsonify


# initialization of flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True


# api endpoint data goes here
resources = [
    {'id': 0,
     'name': 'John Smith',
     'employee_num': 69,
     'profit': 1900.42,
     'date_updated': '2022'}
]


# create html display page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Adam's Test API</h1>
<p>Endpoint Route: /api/v1/resources</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(resources)


# start up application on designated port
app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)


# info found here:
# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask