'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
'''

from metaldetectordefects import Metal_detector_defect as mdd
import json
from testunitario import TestImage as test

if __name__ == '__main__': 
    '''
        Programa principal del proyecto.
    '''
    # Declarar constantes.
    with open('./constans.json', 'r') as f:
        constans = json.load(f)

    # Activar el detector.
    defectdetector = mdd(constans['inputpath'],constans['outputpath'])
    print(defectdetector)
    defectdetector.dectection()
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
