'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
Clase que localiza el defecto en una ubicación concreta de la pieza. 
Devuelve un array con las coordenadas correspondientes.
'''

class Location: 
    '''
        Clase que localiza el defecto en una ubicación concreta de la pieza.
    '''

    def __init__(self): 
        '''
            Constructor del objeto location.
        '''
        self.xmin = None
        self.ymin = None
        self.xmax = None
        self.ymax = None

    #1. Localizador: def locator