class Container():
	containerId = None                  # String
	accessRightId = None                # String
	searchStrings = []                  # List of Strings
	creationTime = None                 # DateTime
	lastModifiedTime = None             # DateTime
	maxNrOfInstances = None             # Integer
	contentInstancesReference = None    # String
	subscriptionReference = None        # String

	def getContainerId(self):
		return containerId

	def getAccessRightId(self):
		return accessRightId

	def getSearchStrings(self):
		return searchStrings

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

