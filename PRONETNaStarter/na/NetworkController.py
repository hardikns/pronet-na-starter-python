from flask import Flask, request
from flask.ext.restful import Resource, reqparse
from PRONETNaStarter.na.core.ContentInstanceInfo import ContentInstanceInfo 
import httplib
import json

class receiveDeviceParams(Resource):
	def post(self, appId, deviceId):
		contentInstanceInfo = ContentInstanceInfo(appId, deviceId, json.loads(request.data))
		print contentInstanceInfo
		return ("Success Guaranteed", httplib.OK)

class NetworkController():
	_api = False
	_parser = False

	def __init__(self, api):
		_api = api
		api.add_resource(receiveDeviceParams, 
			"/pronet-na-starter/applications/<string:appId>/containers/<string:deviceId>/contentinstances")

			




