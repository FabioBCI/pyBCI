#Author: FabioBCI
#Data: 24/11/2017

import matplotlib.pyplot as plt
import plotly.plotly as py


class show:
	def __init__(self):
		pass

	def show_channel(self,input_data,channel):
			plt.plot(input_data[:,channel])

	def show_channel_piece(self,input_data,channel,start,end):
		plt.plot(input_data[start:end,channel])

	def show_signals(self,input_data):
		plt.plot(input_data)

	def show_chunk(self,chunk):
		plt.plot(chunk.data)

	def show_chunk_and_transform(self,chunk):
		x=chunk.data.ix[:,1]
		y=chunk.transform

		plt.subplot(121)
		plt.plot(x)
		plt.title('Original Data Channel 1')
		plt.ylabel('Voltage')

		plt.subplot(122)
		plt.plot(y)
		plt.xlabel('time (s)')
		plt.title('Features Vector WELCH')
		plt.ylabel('Power')

		plt.subplots_adjust(left=0.2, wspace=0.8, top=0.8)

	def refresh(self):
		plt.show()
