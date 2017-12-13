
import sesion
import pandas as pd

class pipe:
	def __init__(self):
		#******** PREPROCESSING ************
		self.spatial_filter_type=-1
		self.freq_filter_type=-1
		self.order_filter=-1
		self.rang_filter=[]
		self.threshold=-1
		self.windows_size=0
		self.overlap=0
		self.number_average=0
		self.select_channels=[]
		#***********************************

		#******** FEATURES *****************
		self.features_type=""
		self.freq_rang_features=[]
		#***********************************

		#******* CLASSIFICATION *************
		self.classification_type=""
		#***********************************

		self.sessions_list=[]
		self.id_pipe=0

	def AddSesion(self,session):
		self.sessions_list.Add(session)

	def Config(self):
		self.Config_preprocessing()
		self.Config_features()

	def Config_preprocessing(self):
		#1.Seleccionamos que canales queremos
		print("What channels do you want to select ?")
		canales=input()
		print("Apply Spatial filter ?")
		if(input()=='yes'):
			print('******************************************')
			print('Wich Spatial Filter want do you apply ?')
			print('')
			print('1- CAR')
			print('2- LAPLACIAN')
			print('3- CSP')
			print('*****************************************')
			spatial_filter=input()
		else:
			spatial_filter=-1

		print("Apply Frecuencial filter ?")
		if(input()=='yes'):
			print('******************************************')
			print('Wich Frecuencial Filter want do you apply ?')
			print('')
			print('1- LOW PASS BAND')
			print('2- HIGH PASS BAND')
			print('3- BAND PASS')
			print('*****************************************')
			freq_filter=input()
			print("Filter order :")
			order=input()
			print("Frequencies Rang :")
			freq_rang=input()
		else:
			freq_filter=-1

		print("Apply threshold ?")
		if(input()=='yes'):
			print("Value threshold :")
			threshold=input()
		else:
			threshold=-1

		print("Windows size :")
		windows=input()
		print("overlap :")
		overlap=input()
		print("Avarage Trials :")
		average=input()

		#Aplicamos los valores introducidos
		self.select_channels=canales
		self.spatial_filter_type=spatial_filter
		self.freq_filter_type=freq_filter
		self.order_filter=order
		self.rang_filter=freq_rang
		self.threshold=threshold
		self.windows_size=windows
		self.overlap=overlap
		self.number_average=average

	def Load_CSV_CONFIG(sefl,csv_file):
		file_config=pd.read_csv(csv_file,header=None)
		

	def Config_features(self):
		print('******************************************')
		print('Wich Type of Features want do you apply ?')
		print('')
		print('1- WELCH')
		print('2- PERIODOGRAM')
		print('3- SUM BAND ALPHA AND BETA')
		print('4- WAVELET')
		print('5- NOTHING')
		print('*****************************************')

		feature=input()
		self.features_type=feature
		if(feature==1 or feature==2):
			print("Frequencies Rang ?")
			rang=input()
			self.freq_rang_features=rang
		else:
			pass

	def show(self):
		print('*****************************************')		
		print('*           PREPROCESSING               *')
		print('-----------------------------------------')
		if(self.spatial_filter_type>0):
			if(self.spatial_filter_type==1):
				print(' Spatial filter: CAR')
			else:
				if(self.spatial_filter_type==2):
					print(' Spatial filter: LAPLACIAN ')
				else:
					print(' Spatial filter: CSP       ')
		else:
			print(' Spatial filter: NO APPLY')
		if(self.freq_filter_type>0):
			if(self.freq_filter_type==1):
				print(' Frecuencial filter: LOW PASS  ')
				print('             Band:',self.rang_filter)
			else:
				if(self.freq_filter_type==2):
					print(' Frecuencial filter: HIGH PASS ')
					print('             Band:',self.rang_filter)
				else:
					print(' Frecuencial filter: BAND PASS ')
					print('             Band:',self.rang_filter)
		else:
			print(' Frecuencial filter: NO APPLY      ')

		if(self.threshold>0):
			print(' Threshold: YES ',self.threshold)
		else:
			print(' Threshold: NO APPLY              ')

		print(' Selected channels: ',self.select_channels)
		print(' Windows size: ',self.windows_size)
		print(' Overlap: ',self.overlap)
		print('')
		print('*****************************************')	
		print('*               FEATURES                *')
		print('-----------------------------------------')
		if(self.features_type==1):
			print(' Feature type : WELCH')
			print('          Rang: ',self.freq_rang_features)
		else:
			if(self.features_type==2):
				print(' Feature type : PERIODOGRAM')
				print('          Rang: ',self.freq_rang_features)
			else:
				if(self.features_type==3):
					print(' Feature type : SUM BANDS ALPHA AND BETA')
				else:
					if(self.features_type==4):
						print(' Feature type : WAVELET')
					else:
						print(' Feature type : NOTHING')

		print('******************************************')
