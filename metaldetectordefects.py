'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
Clase principal: metal_detector_defect()
'''

class Metal_detector_defect: 
    '''
        Clase que detecta defectos en piezas metálicas.
    '''
    def __init__(self):
        '''
            Constructor que carga el detector.
        '''
        self.pathdb = ""
        self.pathoutput = ""

    def dectection(self,):
        '''
            Función a la que se le introduce una imágen de entrada y devuelve 
            a su salida un fichero xml.
        '''

        #1. Cargar y preprocesar los datos: llamar a clase initialize.
        #2. Detectar defectos: llamar a la clase piece.
        #3. Presentar resultados: llamar a la clase results.
        #4. ¿? Evaluación: llamar a la clase evaluation.