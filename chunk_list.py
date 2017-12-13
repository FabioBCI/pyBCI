import chunk
import event

class chunk_list:
	def __init__(self):
		self.array_chunks=[]
		self.num_chunks=0

	def Add(self,chunk):
		self.array_chunks.append(chunk)
		self.num_chunks=self.num_chunks+1

	def create_features(self,feature,param):
		array_features=[]
		for chunks in self.array_chunks:
			feature=chunks.Transform(feature,param)

	def getChunk(self,number_chunk):
		if(number_chunk>self.num_chunks):
			return []
		else:
			return self.array_chunks[number_chunk]
