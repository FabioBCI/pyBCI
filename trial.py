#Author: Fabio R. Llorella Costa
#Data: 20/11/2017
#Description: Esta clase contiene un vector NxM donde N es el numero de columnas y M el numero de registros, N se identifica como la cantidad de canales y M seria el eje temporal
#             Indicando la cantidad de puntos

import numpy as np

class Trial:
    #Atributos de la clase
    numero_canales=0
    cantidad_puntos=0
    data=[]

    def __init__(self,data):
        l=np.shape(data)
        self.data=data        
        self.numero_canales=l[0]
        self.cantidad_puntos=l[1]


    
