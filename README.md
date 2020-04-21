# AIVA_MUVA_DefectosMetales

## Autores:
- Garazi Alfaro García
- Patricia Fernández Fernández

## MOTIVACIÓN:
Este proyecto contiene la práctica de la asignatura Aplicaciones Industriales en la Visión Artificial perteneciente al Máster Universitario en Visión Artificial impartido en la Universidad Rey Juan Carlos.

## DESCRIPCIÓN:
Detección de defectos o posibles manchas en piezas metálicas en una línea de producción. Con este algoritmo se identifican el tipo de defecto y su respectiva localización, a través de una imagen de la pieza a tratar.

## INSTALACIÓN DE LIBRERIAS EN EL SERVIDOR: 
A parte de la versión python 3, se debe instalar la lista de librerías requirements.txt. Si tienes instalado pip3, únicamente necesitarás lanzar la siguiente línea de comandos para ejecutar la instalación de los requirements.txt. 

	pip3 install requirements.txt

Además, se deberá instalar manualmente CUDA (NVIDIA) en una verión igual o mayor a la 10.0.

Estos dos pasos son necesario para que dispongas de todos los recursos neceesarios para poder utilizar este proyecto.  

## INSTRUCCIONES DE EJECUCIÓN DEL SERVIDOR:
Dentro de la carpeta AIVA_MUVA_DefectosMetales:
> python3 main.py

## INSTALACIÓN DE LIBRERIAS EN EL CLIENTE:
Dentro del sistema del cliente, a parte de la versión python 3, se deberá instalar la lísta de librerias requirements_client.txt igual que se hizo anteriormente en el servidor.
> pip3 install requirements.txt

Este paso, es necesario para que dispongas de todos los recursos neceesarios para poder utilizar este proyecto.  


## INSTRUCCIONES DE EJECUCIÓN DEL CLIENTE:
Dentro de la carpeta AIVA_MUVA_DefectosMetales y del sistema del cliente se ejecutará el siguiente comando:
> python3 client.py
