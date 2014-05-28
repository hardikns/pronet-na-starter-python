import requests, json
from PronetNetworkApp.rest.domain.Command import Command
from PronetNetworkApp.rest.domain.Application import Application
from PronetNetworkApp.utils.constants import *

class NetworkApp():
	_appId = False
	_isCreated = False
	_m2mPoC = False

	def init(self, appId, m2mPoC):
		self._appId = appId
		self._m2mPoC = m2mPoC
		self._isCreated = True

	def isCreated(self):
		return self._isCreated

	def getAppId(self):
		return self._appId

	def getm2mPoC(self):
		return self._m2mPoC

	@classmethod
	def autoConfigure(cls, m2mPoC, aPoC):
		jsonBody = Application(obj_dict={'aPoC':aPoC, 
								'searchStrings': APP_SEARCH_STRING_LIST, 
								'accessRightID': APP_ACCESS_RIGHTS_ID }).toJson()
		commandUrl = m2mPoC + "/pronet/applications"
		headers={'content-type': 'application/json'}
		try:
			restResp = requests.post(commandUrl, data=jsonBody, headers=headers)
			respdict = json.loads(restResp.content)
		except Exception as e:
			raise Exception(e, commandUrl, jsonBody, restResp.content)
		netApp = cls()
		netApp.init(respdict['appId'], m2mPoC)
		return netApp

	def sendDeviceCommand(self, deviceId, commandId):
		command = Command()
		command.setCommand(commandId)
		commandUrl = self._m2mPoC + "/pronet/applications/" + \
					 self._appId + "/containers/" + deviceId + "/commands"
		print command.__dict__
		headers={'content-type': 'application/json'}
		
		try:
			restResp = requests.post(commandUrl, data=command.toJson(), headers=headers)
			respdict = json.loads(restResp.content)
		except Exception as e:
			raise Exception(e, commandUrl, command.toJson(), restResp.content)
		print restResp.content
		commandResp = Command(json.loads(restResp.content))
		return commandResp