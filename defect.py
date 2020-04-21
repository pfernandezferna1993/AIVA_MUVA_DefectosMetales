'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
Clase que detecta un defecto en una pieza. Devuelve: 
    - la etiqueta que identifica el defecto
    - la fiabilidad de la clasificación del defecto
    - la localización del defecto
'''
import keras
import numpy as np

from keras_yolo3 import yolo3_one_file_to_detect_them_all as yolo 
#from keras_yolo3 import train as yolotrain

class Defect:
    '''
        Clase que detecta un defecto en una pieza.
    '''

    def __init__(self): 
        '''
            Constructor del objeto defect.
        '''
        self.tag = None
        self.fidelity = None
        self.location = []
                    
        # TO DO: Load yolov3 model
        # 0. Entrenar la red para adquirir los pesos personalizados (fuera de este codigo).
        # 1. Cargar el modelo de red. model = [..]
        # 2. Cargar al modelo los nuevos pesos.
        self.model = model
        

    #1. Detector def defectos:
    def defectdetector(self, image):
        print(self.model)
        #TO-DO: Prediccion de una imagen. Clasificación y regresión.
        #yhat = self.model.predict(image)
        #print(yhat)

    

        