'''
Máster Universitario en Visión Artificial
ASIGNATURA: Aplicaciones Industriales en Visión Artificial
Autores: 
Garazi Alfaro García
Patricia Fernández Fernández

PRÁCTICA: Detección de fallos en superficies metálicas.
'''

import glob
from cv2 import cv2
import random
import json
import xml.etree.ElementTree as ET





# Defect classifier,
def defect_classifier(img):
    '''
    DEFECT CLASSES:
    0: inclusions
    1: scratches
    2: patches
    3: pitted_surface
    4: crazing
    5: rolled_in_scale
    '''
    tag = random.randint(0,5)

    return tag

def defect_localicer(img):
    '''
    location = [xmin,ymin,xmax,ymax] in pixels
    size = [width,height,depth] in pixels
    '''
    height, width, depth = img.shape
    size = [width,height,depth]

    xmin = random.randint(0,width)
    ymin = random.randint(0,height)
    xmax = random.randint(xmin,width)
    ymax = random.randint(ymin,height)
    location = [xmin,ymin,xmax,ymax]

    return location, size

def create_output_xml(defect,location,shape,outputpath,inputdb,filename):
    template = ET.parse('template.xml')
    root = template.getroot()
    annotation = ET.Element('annotation')

    # Complete general information
    folder = ET.SubElement(annotation,'folder')
    folder.text = defect['folder']
    filename = ET.SubElement(annotation,'filename')
    filename.text = filename
    source = ET.SubElement(annotation,'source')
    database = ET.SubElement(source,'database')
    database.text = inputdb
    size = ET.SubElement(annotation,'size')
    width = ET.SubElement(size,'width')
    width.text = str(shape[0])
    height = ET.SubElement(size,'height')
    height.text = str(shape[1])
    depth = ET.SubElement(size,'depth')
    depth.text = str(shape[2])
    segmented = ET.SubElement(annotation,'segmented')
    segmented.text = str(0)



    # Complete defect information
    object = ET.SubElement(annotation, 'object')
    name = ET.SubElement(object,'name')
    name.text = defect['name']
    pose = ET.SubElement(object,'pose')
    pose.text = 'Unspecified'
    truncated = ET.SubElement(object,'truncated')
    truncated.text = str(0)
    difficult = ET.SubElement(object,'difficult')
    difficult.text = str(0)
    bndbox = ET.SubElement(object, 'bndbox')
    xmin = ET.SubElement(bndbox,'xmin')
    xmin.text = str(location[0])
    ymin = ET.SubElement(bndbox,'ymin')
    ymin.text = str(location[1])
    xmax = ET.SubElement(bndbox,'xmax')
    xmax.text = str(location[2])
    ymax = ET.SubElement(bndbox,'ymax')
    ymax.text = str(location[3])

    # create a new XML file 
    mydata = ET.tostring(annotation,encoding='utf-8', method='xml')
    myfile = open("output.xml", "wb")
    myfile.write(mydata)

if __name__ == '__main__':
    with open('./constans.json', 'r') as f:
        constans = json.load(f)
    # Load images
    inputPath = './NEU-DET/IMAGES/'
    path = inputPath + '*.jpg'
    dirs = glob.glob(path)
    inputImages = []

    # Procesing images
    for file in dirs:
        print('Cargando imagen...')
        img = cv2.imread(file)
        filename = file.split('/')[-1]
        print(filename)
        tag = defect_classifier(img)
        print('Etiqueta del defecto: ' + str(tag))
        location, size = defect_localicer(img)
        print('Location: ' + str(location))
        print('Size: ' + str(size))
        defect = constans['defects'][str(tag)]
        inputdb = constans['inputpath'].split('/')[1]
        create_output_xml(defect,location,size,constans['outputpath'],inputdb,filename)
        cv2.imshow('image', img)
        cv2.waitKey()

