from PronetNetworkApp.utils.datetime_new import datetime
import json

class Container():
	containerId = None                  # String
	accessRightId = None                # String
	searchStrings = []                  # List of Strings
	creationTime = None                 # DateTime (converted from Epoch format)
	lastModifiedTime = None             # DateTime (converted from Epoch format)
	maxNrOfInstances = None             # Integer
	contentInstancesReference = None    # String
	subscriptionReference = None        # String

	def __init__(self, obj_dict=None):
		self.containerId = None                  
		self.accessRightId = None                
		self.searchStrings = []                  
		self.creationTime = None                 
		self.lastModifiedTime = None             
		self.maxNrOfInstances = None             
		self.contentInstancesReference = None    
		self.subscriptionReference = None        
		if obj_dict == None:
			return
		for key in self.__dict__.keys():
			self.__dict__[key] = obj_dict.get(key, None)
		if isinstance(self.creationTime, (int, long)): 
			self.creationTime = datetime.fromEpoch(self.creationTime)
		if isinstance(self.lastModifiedTime, (int, long)): 
			self.lastModifiedTime = datetime.fromEpoch(self.lastModifiedTime)

	def toJson(self):
		obj_dict = self.__dict__
		obj_dict['creationTime'] = obj_dict['creationTime'] and \
		                           obj_dict['creationTime'].epoch() or 0
		obj_dict['lastModifiedTime'] = obj_dict['lastModifiedTime'] and \
									   obj_dict['lastModifiedTime'].epoch() or 0
		return json.dumps(obj_dict)

	def getContainerId(self):
		return self.containerId

	def getAccessRightId(self):
		return self.accessRightId

	def getSearchStrings(self):
		return self.searchStrings

	def getCreationTime(self):
		return creationTime

	def getLastModifiedTime(self):
		return lastModifiedTime

	def getMaxNrOfInstances(self):
		return maxNrOfInstances

	def getContentInstancesReference(self):
		return contentInstancesReference

	def getSubscriptionReference(self):
		return subscriptionReference

	def setContainerId(self, containerId):
		self.containerId = containerId

	def setAccessRightId(self, accessRightId):
		self.accessRightId = accessRightId

	def setSearchStrings(self, searchStrings):
		self.searchStrings = searchStrings

	def setCreationTime(self, creationTime):
		self.creationTime = creationTime

	def setLastModifiedTime(self, lastModifiedTime):
		self.lastModifiedTime = lastModifiedTime

	def setMaxNrOfInstances(self, maxNrOfInstances):
		self.maxNrOfInstances = maxNrOfInstances

	def setContentInstancesReference(self, contentInstancesReference):
		self.contentInstancesReference = contentInstancesReference

	def setSubscriptionReference(self, subscriptionReference):
		self.subscriptionReference = subscriptionReference

