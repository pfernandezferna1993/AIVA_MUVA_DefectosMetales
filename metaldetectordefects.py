'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
Clase principal: metal_detector_defect()
'''
from initialize import Initialize
from defect import Defect as defect


class Metal_detector_defect: 
    '''
        Clase que detecta defectos en piezas metálicas.
    '''
    def __init__(self,pathdb,pathoutput):
        '''
            Constructor que carga el detector.
        '''
        self.pathdb = pathdb
        self.pathoutput = pathoutput

    def dectection(self):
        '''
            Función a la que se le introduce una imágen de entrada y devuelve 
            a su salida un fichero xml.
        ''' 
        #print(self.pathdb)
        #print(self.pathoutput)

        #1. Cargar y preprocesar los datos:
        initialize = Initialize(self.pathdb)
        dirsImages = initialize.loadimages()

        for file in dirsImages:
            image = initialize.preprocesing(file)
            #2. Detectar defectos:
            detector = defect()
            detector.defectdetector(image)
            
            #3. Presentar resultados: llamar a la clase results.
