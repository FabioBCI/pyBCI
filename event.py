
class event:
	def __init__(self):
		self.label=""
		self.time=0
		self.duration=0

	def __init__(self,label,time,duration):
		self.label=label
		self.time=time
		self.duration=duration

	def getLabel(self):
		return self.label
		
	def getStart(self):
		return self.time

	def getDuration(self):
		return self.duration

	def setLabel(self,label):
		self.label=label

	def setStart(self,start):
		self.time=start

	def setDuration(self,duration):
		self.duration=end

	def getTimeStart_in_values(self,fm):
		return (self.time*fm)

	def getDuration_in_values(self,fm):
		return (self.duration*fm)