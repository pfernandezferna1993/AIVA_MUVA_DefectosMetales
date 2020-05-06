'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
'''

#from metaldetectordefects import Metal_detector_defect as mdd
import json
from testunitario import TestImage as test
import socketserver
from server import Servidor
from defect import Defect as defect

if __name__ == '__main__': 
    '''
        Programa principal del proyecto.
    '''
    # Declarar constantes.
    with open('./constans.json', 'r') as f:
        constans = json.load(f)


    #TO DO: 
    # 1. Cargar el modelo de red. -->   detector = defect()
    

    #Poner en marcha el servidor
    server_address = ('127.0.0.1', 8000)
    httpd = socketserver.TCPServer(server_address, Servidor)
    print('Starting httpd on port 8000')
    httpd.serve_forever()


    '''
        Lanzar los test unitarios.
    '''
    '''
        tester = test()
        test_cr = tester.test_crazing()
        test_in = tester.test_inclusions()
        test_sr = tester.test_scratches()
        test_pa = tester.test_patches()
        test_rs = tester.test_rolled_in_scale()
        test_ps = tester.test_pitted_surface()
        
        print(test_cr)
        print(test_in)
        print(test_sr)
        print(test_pa)
        print(test_rs)
        print(test_ps)
    '''
