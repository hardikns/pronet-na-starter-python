from flask import Flask
from flask.ext.restful import Api
import NetworkController

app = Flask(__name__)
api = Api(app)
NetworkController(api)

if __name__ == "__main__":
	app.run(debug=True)
