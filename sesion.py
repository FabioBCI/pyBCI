#Author: FabioBCI
#Data: 23/11/2017

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as lib_signal
import event
import chunk
import chunk_list

class sesion:
	data=[]
	fm=0
	channels_index=[]
	channels_name=[]
	num_channels=0
	file_name=""

	def __init__(self):
		pass		

	def read_csv_data(self,file_data):
		self.file_name=file_data
		try:
			aux_data=pd.read_csv(file_data,header=None)
			header=aux_data.ix[0] #Cogemos la cabecera del fichero
			size_data=np.shape(aux_data)
			fm_line=aux_data.ix[1]
			size_header=np.shape(header)
			self.fm=int(fm_line.ix[(size_header[0]-1):].tolist()[0])
			self.num_channels=size_header[0]-2 #Cantidad de canales de que disponemos
			self.channels_index=range(1,self.num_channels+1)
			self.channels_name=header.tolist()[1:(self.num_channels)+1]
			aux_data=aux_data.ix[1:(size_data[0]),1:(self.num_channels)]
			self.data=aux_data.astype(float)
			self.channels_selected=self.channels_index
			self.events_table=[]
		except Exception as e:
			print("[*]-ERROR TO READ EEG FILE => "+str(e))
	
	def read_csv_events(self,file_events):
		try:
			aux_data=pd.read_csv(file_events,header=0)
			size=np.shape(aux_data)#Rows x Columns

			for i in range(0,size[0]): #Leo cada registro y creamos un objeto evento
				evento=event.event(int(aux_data.ix[i,1]),aux_data.ix[i,0],aux_data.ix[i,2])
				self.events_table.append(evento)

		except Exception as e:
			print("[*]-ERROR TO CREATE EVENTS => "+str(e))

	def Load_CSV(self,file_eeg,file_events):
		self.read_csv_data(file_eeg)
		self.read_csv_events(file_events)

	def getChunks(self,window,overlap,event_label): 
		try:
			if(self.events_table==[]):
				print("[*]-NO EVENTS IN THIS SESSION")
				return []
			else:
				size_signals=np.shape(self.data)
				start=0
				cont=0
				end=start+window
				array_chunks=chunk_list.chunk_list()
				while end<size_signals[0]:
					chunk_data=self.data.ix[start:end-1,:]
					for event in self.events_table:
						if(start>=(event.getTimeStart_in_values(self.fm)) and end<(event.getTimeStart_in_values(self.fm)+event.getDuration_in_values(self.fm))):
							if(event.getLabel()==event_label):
								#Es un chunk del tipo event que buscamos
								object_chunk=chunk.chunk(chunk_data,self.file_name,event,self.fm,self.channels_selected)
								array_chunks.Add(object_chunk) #Aqui no esta bien <= PROBLEMA !!!!!
								cont=cont+1
							else:
								pass
						else:
							pass

					start=end-overlap
					end=start+window

				return array_chunks

		except Exception as e:
			print("[*]-ERROR TO CREATE CHUNKS => "+str(e))

	def select_channels(self,channels):
		self.channels_selected=channels		

	def show_events(self):
		for event in self.events_table:
			print(event.getLabel())


