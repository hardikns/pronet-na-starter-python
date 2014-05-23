import requests, json
from PronetNetworkApp.rest.domain.Command import Command

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