'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
'''
import cv2
import base64
import json
import http.client

def client(path):
    print('Procesing image... ' + path)

    # Cargamos una imagen, luego va a base64, a un mapa y a un JSON
    img = cv2.imread(path)
    png_encoded_img = cv2.imencode('.jpg', img)
    base64_encoded_img = base64.b64encode(png_encoded_img[1])
    message = {'img': base64_encoded_img.decode('UTF-8')}
    json_message = json.dumps(message)
    #print(json_message)


    # Creamos conexión, cabecera y enviamos el mensaje con un POST
    headers = {'Content-type': 'application/json'}
    connection = http.client.HTTPConnection('127.0.0.1', port=8000)
    connection.request('POST','', json_message, headers)

    # Esperamos la respuesta y la pintamos por pantalla
    resp = connection.getresponse()
    print(resp.read().decode())

if __name__ == '__main__':
    print('If you want to stop the program insert \'exit\' ')
    while True:
        print('Insert image path:')
        path = input()
        if (path == 'exit'):
            print('The program has ended.')
            break
        else:
            try: 
                client(path)
            except:
                print('The image path entered incorrectly.')


