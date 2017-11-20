
#Author: Fabio R. Llorella Costa
#Data: 20/11/2017
#Description: Esta clase contiene un vector NxM donde N es el numero de columnas y M el numero de registros, N se identifica como la cantidad de canales y M seria el eje temporal
#             Indicando la cantidad de puntos

import matplotlib.pyplot as plt

class visual:

    def __init__(self):
        pass
        
    def plot_array(self,data):
        #Show array
        plt.plot(data)
