import unittest
from xml.etree import ElementTree


class TestImage (unittest.TestCase):
    def test_crazing(self):
        '''
            Test detection a crazing. 
        '''
        #detector = DefectDetector()
        #result = detector.detector(imagen)
        tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/crazing_1.xml')
        # tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/inclusion_1.xml')
        root = tree.getroot()
        boxes = list()
        folder = root.find('folder')
        self.assertEquals(folder.text,'cr')
        w = root.find('size').find('width')
        h = root.find('size').find('height')
        d = root.find('size').find('depth')
        self.assertEqual(int(w.text),200)
        self.assertEqual(int(h.text),200) 
        self.assertEqual(int(d.text),1)
        for obj in root.findall('.//object'):
            name = obj.find('name').text
            self.assertEqual(name,'crazing')
            pose = obj.find('pose').text
            self.assertEqual(pose,'Unspecified')

    def test_inclusions(self):
        '''
            Test detection a inclusion. 
        '''
        #detector = DefectDetector()
        #result = detector.detector(imagen)
        tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/inclusion_1.xml')
        # tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/crazing_1.xml')
        root = tree.getroot()
        boxes = list()
        folder = root.find('folder')
        self.assertEquals(folder.text,'in')
        w = root.find('size').find('width')
        h = root.find('size').find('height')
        d = root.find('size').find('depth')
        self.assertEqual(int(w.text),200)
        self.assertEqual(int(h.text),200) 
        self.assertEqual(int(d.text),1)
        for obj in root.findall('.//object'):
            name = obj.find('name').text
            self.assertEqual(name,'inclusion')
            pose = obj.find('pose').text
            self.assertEqual(pose,'Unspecified')

    def test_patches(self):
        '''
            Test detection a patches. 
        '''
        #detector = DefectDetector()
        #result = detector.detector(imagen)
        tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/patches_1.xml')
        # tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/crazing_1.xml')
        root = tree.getroot()
        boxes = list()
        folder = root.find('folder')
        self.assertEquals(folder.text,'pa')
        w = root.find('size').find('width')
        h = root.find('size').find('height')
        d = root.find('size').find('depth')
        self.assertEqual(int(w.text),200)
        self.assertEqual(int(h.text),200) 
        self.assertEqual(int(d.text),1)
        for obj in root.findall('.//object'):
            name = obj.find('name').text
            self.assertEqual(name,'patches')
            pose = obj.find('pose').text
            self.assertEqual(pose,'Unspecified')

    def test_pitted_surface(self):
        '''
            Test detection a pitted_surface. 
        '''
        #detector = DefectDetector()
        #result = detector.detector(imagen)
        tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/pitted_surface_1.xml')
        # tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/crazing_1.xml')
        root = tree.getroot()
        boxes = list()
        folder = root.find('folder')
        self.assertEquals(folder.text,'pa')
        w = root.find('size').find('width')
        h = root.find('size').find('height')
        d = root.find('size').find('depth')
        self.assertEqual(int(w.text),200)
        self.assertEqual(int(h.text),200) 
        self.assertEqual(int(d.text),1)
        for obj in root.findall('.//object'):
            name = obj.find('name').text
            self.assertEqual(name,'pitted_surface')
            pose = obj.find('pose').text
            self.assertEqual(pose,'Unspecified')



    def test_scratches(self):
        '''
            Test detection a scratches. 
        '''
        #detector = DefectDetector()
        #result = detector.detector(imagen)
        tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/scratches_1.xml')
        # tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/crazing_1.xml')
        root = tree.getroot()
        boxes = list()
        folder = root.find('folder')
        self.assertEquals(folder.text,'sc')
        w = root.find('size').find('width')
        h = root.find('size').find('height')
        d = root.find('size').find('depth')
        self.assertEqual(int(w.text),200)
        self.assertEqual(int(h.text),200) 
        self.assertEqual(int(d.text),1)
        for obj in root.findall('.//object'):
            name = obj.find('name').text
            self.assertEqual(name,'scratches')
            pose = obj.find('pose').text
            self.assertEqual(pose,'Unspecified')

    def test_rolled_in_scale(self):
        '''
            Test detection a rolled_in_scale. 
        '''
        #detector = DefectDetector()
        #result = detector.detector(imagen)
        tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/rolled-in_scale_1.xml')
        # tree = ElementTree.parse('./NEU-DET/ANNOTATIONS/crazing_1.xml')
        root = tree.getroot()
        boxes = list()
        folder = root.find('folder')
        self.assertEquals(folder.text,'rs')
        w = root.find('size').find('width')
        h = root.find('size').find('height')
        d = root.find('size').find('depth')
        self.assertEqual(int(w.text),200)
        self.assertEqual(int(h.text),200) 
        self.assertEqual(int(d.text),1)
        for obj in root.findall('.//object'):
            name = obj.find('name').text
            self.assertEqual(name,'rolled-in_scale')
            pose = obj.find('pose').text
            self.assertEqual(pose,'Unspecified')   
