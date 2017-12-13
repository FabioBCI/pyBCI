import numpy as np
import event
import scipy
from scipy import signal
import features_eeg

class chunk:
	def __init__(self):
		self.data=[]
		self.name_sesion=""
		self.event=[]
		self.fm=0
		self.selected_channels=0
		self.transform=[]
		self.type_feature=""

	def __init__(self,data,name_sesion,event,fm,selected_channels):
		self.data=data
		self.name_sesion=name_sesion
		self.event=event
		self.fm=fm
		self.selected_channels=selected_channels
		self.transform=[]
		self.type_feature=""

	def getData(self):
		return self.data

	def getEvent(self):
		return self.event

	def getSesion(self):
		return self.name_sesion

	def getFm(self):
		return self.fm

	def Transform(self,feature,band): #Problema de estructura de datos
		if(feature=='WELCH'):
			fh=self.fm/2
			fs=self.fm
			size_data=np.shape(self.data)
			size_chanels=np.shape(self.selected_channels)
			feature=[]#np.zeros([(size_chanels[0]*(fh+1))])
			for c in self.selected_channels:
				vector_aux=self.data.ix[:,c]
				vector=vector_aux.tolist()
				v_aux=[float(i) for i in vector]#Convertimos a floats
				power=features_eeg.pwelch(v_aux,fs,250)
				feature=np.concatenate([feature,power],axis=0)

			self.transform=feature
			self.type_feature='WELCH'
			return feature
		else:
			if(feature=='PERIODOGRAM'):
				fh=self.fm/2
				fs=self.fm
				size_data=np.shape(self.data)
				size_chanels=np.shape(self.selected_channels)
				feature=np.zeros([(size_chanels[0]*(fh+1))])
				for c in self.selected_channels:
					vector_aux=self.data.ix[:,c]
					vector=vector_aux.tolist()
					v_aux=[float(i) for i in vector]#Convertimos a floats
					power=features_eeg.periodogram(v_aux,fs)
					feature=np.concatenate([feature,power],axis=0)

				self.transform=feature
				self.type_feature='PERIODOGRAM'
				return feature
			else:
				pass