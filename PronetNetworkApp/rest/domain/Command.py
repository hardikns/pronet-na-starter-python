class Command():
	commandId = None	
	creationTime = None
	lastModifiedTime = None
	commandType = None
	execEnable = None
	description = None
	execInstancesReference = None
	subscriptionsReference = None
	command = None

	def getCommandId(self):
		return self.commandId

	def setCommandId(self, commandId):
		self.commandId = commandId

	def getCreationTime(self):
		return self.creationTime

	def setCreationTime(self, creationTime):
		self.creationTime = creationTime

	def getLastModifiedTime(self):
		return self.lastModifiedTime

	def setLastModifiedTime(self, lastModifiedTime):
		self.lastModifiedTime = lastModifiedTime

	def getCommandType(self):
		return self.commandType

	def setCommandType(self, commandType):
		self.commandType = commandType

	def getExecEnable(self):
		return self.execEnable

	def setExecEnable(self, execEnable):
		self.execEnable = execEnable

	def getDescription(self):
		return self.description

	def setDescription(self, description):
		self.description = description

	def getExecInstancesReference(self):
		return self.execInstancesReference

	def setExecInstancesReference(self, execInstancesReference):
		self.execInstancesReference = execInstancesReference

	def getSubscriptionsReference(self):
		return self.subscriptionsReference

	def setSubscriptionsReference(self, subscriptionsReference):
		self.subscriptionsReference = subscriptionsReference

	def getCommand(self):
		return self.command

	def setCommand(self, command):
		self.command = command
