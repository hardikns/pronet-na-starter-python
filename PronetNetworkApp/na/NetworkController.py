from flask import Flask, request
from flask.ext.restful import Resource, reqparse
from PronetNetworkApp.na.core.ContentInstanceInfo import ContentInstanceInfo 
from PronetNetworkApp.na.core.NetworkApp import NetworkApp
import httplib
import json

class NetworkController():
	_api = False
	_parser = False
	_networkApp = False

	class ReceiveDeviceParams(Resource):
		def post(self, appId, deviceId):
			contentInstanceInfo = ContentInstanceInfo(appId, deviceId, json.loads(request.data))
			print contentInstanceInfo
			return ("Success Guaranteed", httplib.OK)

	class Configure(Resource):
		def get(self):
			parser = reqparse.RequestParser()
			parser.add_argument('m2mPoC', type=str, required=True, location='args')
			parser.add_argument('appId', type=str, required=True, location='args')
			args = parser.parse_args()
			m2mPoC = args.get('m2mPoC', False)
			appId = args.get('appId', False)
			if not NetworkController._networkApp or NetworkController._networkApp.isCreated() == False:
				NetworkController._networkApp = NetworkApp()
				NetworkController._networkApp.init(appId, m2mPoC)
				return "Network Application Configured Successfully", httplib.OK
			else:
				return "NA Reconfiguration Forbidden", httplib.FORBIDDEN

	class SendCommand(Resource):
		def get(self, deviceId):
			parser = reqparse.RequestParser()
			parser.add_argument('command', type=str, required=True, location='args')
			args = parser.parse_args()
			commandId = args['command']
			if NetworkController._networkApp and NetworkController._networkApp.isCreated() == True:
				command = self._networkApp.sendDeviceCommand(deviceId, commandId)
				resp_string =  "Device Id: " + deviceId + " Command Reference: " + command.getCommand()
				print resp_string
				return resp_string, httplib.OK
			else:
				if self._networkApp == False:
					return "Add Device Forbidden, Configure NA", httplib.FORBIDDEN
				else:
					return "Device Exists , Device Id: " + deviceId, httplib.FORBIDDEN

	def __init__(self, api):
		_api = api
		api.add_resource(self.ReceiveDeviceParams, 
			"/pronet-na-starter/applications/<string:appId>/containers/<string:deviceId>/contentinstances")
		api.add_resource(self.Configure,'/pronet-na-starter/configure')
		api.add_resource(self.SendCommand, '/pronet-na-starter/send-command/<string:deviceId>')

			




