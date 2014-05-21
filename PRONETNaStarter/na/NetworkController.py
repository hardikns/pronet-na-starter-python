from flask import Flask
from flask.ext.restful import Resource, reqparse
from PRONETNaStarter.na.core.ContentInstanceInfo import ContentInstanceInfo 
import httplib

class NetworkController():
	_api = False
	_parser = False
	def __init__(self, api):
		_api = api
		api.add_resource(receiveDeviceParams, 
			"/pronet-na-starter/applications/<string:appId>/containers/<string:deviceId>/contentinstances")

	class receiveDeviceParams(Resource):
		def post(self, appId, deviceId):
			parser = reqparse.RequestParser()
			parser.add_argument('contentInstance', type=dict)
			args = parser.parse_args()
			contentInstanceInfo = ContentInstanceInfo(appId, deviceId, args['contentInstance'])
			print contentInstanceInfo
			return ("Success Guaranteed", httplib.OK)


			




