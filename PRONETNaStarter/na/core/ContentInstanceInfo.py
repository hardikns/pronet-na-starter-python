from datetime import datetime

class ContentInstanceInfo():
	_contentInstance = False
	_appId = False
	_deviceId = False
	_receivedTime = False

	def __init__(self, appId, deviceId, contentInstanceDict):
	
		self._contentInstance = ContentInstance(contentInstanceDict)
		self._appId = appId
		self._deviceId = deviceId
		self._receivedTime = datetime.now()

	def getContentInstance(self):
		return self._contentInstance

	def getAppId(self):
		return self._appId

	def getDeviceId(self):
		return self._deviceId

	def getReceivedTime(self):
		return self._receivedTime

	def __str__(self):
		return """
		Device Params Received.......\n
		Content Received : %s \n
		App Id           : %s \n
		Device Id        : %s \n 
		Time of Issue    : %s \n
		Recieved Time    : %s \n
		-----------------------------\n""" %  (	self._contentInstance.getContent(),
											 	self._appId(),
											 	self._deviceId,
											 	self._contentInstance.getCreationTime(),
											 	self._receivedTime) 


