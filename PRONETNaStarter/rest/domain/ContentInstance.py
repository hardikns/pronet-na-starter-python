from PRONETNaStarter.utils import constants
from datetime import datetime

class ContentInstance():

	def __init__(self, contentInstanceDict):
		self._contentInstanceId = contentInstanceDict.get('contentInstanceId')	
		self._creationTime      = datetime.strptime(contentInstanceDict.get('creationTime'), 
													PRONET_DATE_FORMAT)
		self._lastModifiedTime  = datetime.strptime(contentInstanceDict.get('lastModifiedTime'), 
													PRONET_DATE_FORMAT)
		self._contentTypes      = list(contentInstanceDict.get('contentTypes'))
		self._mimeType          = list(contentInstanceDict.get('mimeType'))
		self._contentSize       = int(contentInstanceDict.get('contentSize'))
		self._content           = contentInstanceDict.get('content')

	def getContentInstanceId(self):
		return self._contentInstanceId

	def getCreationTime(self):
		return self._creationTime

	def getLastModifiedTime(self):
		return self._lastModifiedTime

	def getContentTypes(self):
		return self._contentTypes

	def getMimeType(self):
		return self._mimeType

	def getContentSize(self):
		return self._contentSize

	def getContent(self):
		return self._content

	def setContentInstanceId(self, contentInstanceId):
		self._contentInstanceId = contentInstanceId

	def setCreationTime(self, creationTime):
		self._creationTime = creationTime

	def setLastModifiedTime(self, lastModifiedTime):
		self._lastModifiedTime = lastModifiedTime

	def setContentTypes(self, contentTypes):
		self._contentTypes = contentTypes

	def setMimeType(self, mimeType):
		self._mimeType = mimeType

	def setContentSize(self, contentSize):
		self._contentSize = contentSize

	def setContent(self, content):
		self._content = content