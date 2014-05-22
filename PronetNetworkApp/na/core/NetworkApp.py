import requests, json

class NetworkApp():
	_appID = False
	_isCreated = False
	_m2mPoC = False

	def init(self, appID, m2mPoC):
		self._appID = appID
		self._m2mPoC = m2mPoC
		self._isCreated = True

	def isCreated(self):
		return self._isCreated

	def getAppId(self):
		return self._appID

	def sendDeviceCommand(self, deviceId, commandId):
		command = Command()
		command.setCommand(commandId)
		commandUrl = self._m2mPoC + "/pronet/applications/" + \
					 appId + "/containers/" + deviceId + "/commands"
		commandData = Json.dumps(command.__dict__)
		restResp = request.post(commandUrl, commandData)
		commandResp = Command().__dict__.update(Json.Loads(restResp.content()))
		return commandResp