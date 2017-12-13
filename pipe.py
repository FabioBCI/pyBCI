
import sesion

class pipe:
	def __init__(self):
		#******** PREPROCESSING ************
		self.spatial_filter_type=0
		self.freq_filter_type=0
		self.rang_filter=[]
		self.threshold=0
		self.windows_size=0
		self.overlap=0
		self.number_average=0
		self.select_channels=[]
		#***********************************

		#******** FEATURES *****************
		self.features_type=""
		#***********************************

		#******* CLASSIFICATION *************
		self.classification_type=""
		#***********************************

		self.sessions_list=[]
		self.id_pipe=0

	def AddSesion(self,session):
		self.sessions_list.Add(session)

	def Config_preprocessing(self):
		#1.Seleccionamos que canales queremos
		print("What channels do you want to select ?")
		canales=input()