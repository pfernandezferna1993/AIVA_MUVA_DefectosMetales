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
                    
        # Load yolov3 model
        model = yolo.make_yolov3_model()
        weight_reader = yolo.WeightReader('./keras_yolo3/yolov3.weights')
        weight_reader.load_weights(model)
        print(type(model))
        #model.save('model.h5')
        self.model = model
        

    #1. Detector def defectos:
    def defectdetector(self, image):
        print(self.model)
        #TO-DO:
        yhat = self.model.predict(image, batch_size=None, verbose=0)
        print(yhat)
        print([a.shape for a in yhat])
        #yolotrain._main_("../config.json")
        #1.1. Llamar al clasificador.
        #1.2. Llamar a location.
    #2. Clasificador: classificator_fail.
    

        