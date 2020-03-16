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

    #1. Detector def defectos: def detect_fail
        #1.1. Llamar al clasificador.
        #1.2. Llamar a location.
    #2. Clasificador: classificator_fail.
    

        