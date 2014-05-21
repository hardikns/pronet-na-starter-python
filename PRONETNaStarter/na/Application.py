from flask import Flask
from flask.ext.restful import Api
from NetworkController import NetworkController

def main():
	app = Flask(__name__)
	api = Api(app)
	nc = NetworkController(api)
	app.run(debug=True, host='0.0.0.0' )
