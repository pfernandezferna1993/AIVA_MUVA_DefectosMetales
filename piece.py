'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
Clase que detecta todos los posibles defectos que tiene una pieza.
'''

class Piece: 
    '''
        Clase que detecta todos los posibles defectos que tiene una pieza.
    '''

    def __init__(self, image):
        '''
            Constructor del objeto pieza.
        '''
        self.image = image
        self.defects = []

    #1.Detector de defectos: def detector.
        #1.1. Llama a la clase results para presentar los resultados.

    #get_piece
    #set_piece