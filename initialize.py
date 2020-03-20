'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
Clase que carga y preprocesa los datos de entrada. Estos serán imágenes.
'''

import json
import glob
from keras.backend import expand_dims
from keras.preprocessing.image import img_to_array
import cv2

class Initialize: 
    '''
        Carga y preprocesa las imágenes de entrada.
    '''

    def __init__(self,pathdb):
        '''
            Constructor del objeto initialize.
        '''
        self.pathdb = pathdb
        self.dirsImages = []
        

    #1.Cargar imágenes:
    def loadimages(self):
        '''
            Carga las imágenes de entrada
        '''
        # Declarar constantes.
        with open('./constans.json', 'r') as f:
            constans = json.load(f)
        print('Cargando imágenes del directorio: ' + self.pathdb)
        path = self.pathdb +'*' + constans['format']
        self.dirsImages = glob.glob(path)

        return self.dirsImages

    #2.Preprocesar imágenes: 
    def preprocesing(self,file): 
        '''
            Preprocesasdo de imágenes, adecúa la imagen a la entrada del modelo.
        '''
        #print(image.shape)
        image = cv2.imread(file)
        filename = file.split('/')[-1]
        #print('Cargando imagen: ' + filename)
        # Convierte numpy array
        image = img_to_array(image)
        #Escalar los valores de los pixeles al intervalo [0,1]
        image = image.astype('float32')
        image /= 255.0
        #Añadir una dimension ya que tenemos un solo ejemplo
        image = expand_dims(image, 0)
        #print(image.shape)

        return image