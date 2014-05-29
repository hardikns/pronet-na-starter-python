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
			commandId = int(args['command'])
			if NetworkController._networkApp and NetworkController._networkApp.isCreated() == True:
				try: 
					command = NetworkController._networkApp.sendDeviceCommand(deviceId, commandId)
	
				except Exception as e:
					return """SendCommand Failed<br>Request<br>%s<br>json:%s<br>
					          Error Received from Pronet%s""" % (e[1], e[2], e[3]), httplib.FORBIDDEN
				else:  
					resp_string =  "Device Id: " + deviceId + \
								   " Command Reference: " + str(command.getCommand())
					print resp_string
					return resp_string, httplib.OK
			else:
				if NetworkController._networkApp == False:
					return "Add Device Forbidden, Configure NA", httplib.FORBIDDEN
				else:
					return "Incorrect Configuration", httplib.FORBIDDEN

	class AutoConfigure(Resource):
		def get(self):
			parser = reqparse.RequestParser()
			parser.add_argument('m2mPoC', type=str, required=True, location='args')
			parser.add_argument('aPoCPath', type=str, required=True, location='args')
			args = parser.parse_args()
			m2mPoC = args.get('m2mPoC', False)
			aPoCPaths = [args.get('aPoCPath', False)]

			aPoC = request.url_root

			if not NetworkController._networkApp:
				try: 
					NetworkController._networkApp = NetworkApp.autoConfigure(m2mPoC, aPoC, aPoCPaths)
				except Exception as e:
					return """Communication with Pronet failed<br>Request<br>%s<br>json:%s<br>
					          Error Received from Pronet%s""" % (e[1], e[2], e[3]), httplib.FORBIDDEN
				else:
					return "Network App Configured with Pronet at " + m2mPoC + \
							" appId " +  NetworkController._networkApp.getAppId(), httplib.OK
			else:
				return "Already Configured with " + NetworkController._networkApp.getm2mPoC() + \
						" appId " +  NetworkController._networkApp.getAppId(), httplib.FORBIDDEN
				 

	def __init__(self, api):
		_api = api
		api.add_resource(self.ReceiveDeviceParams, 
			"/pronet-na-starter/applications/<string:appId>/containers/<string:deviceId>/contentinstances")
		api.add_resource(self.Configure,'/pronet-na-starter/configure')
		api.add_resource(self.SendCommand, '/pronet-na-starter/send-command/<string:deviceId>')
		api.add_resource(self.AutoConfigure, '/pronet-na-starter/autoconfigure')

			




