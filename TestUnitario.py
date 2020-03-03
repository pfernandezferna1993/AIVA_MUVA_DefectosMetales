import unittest

class TestImage (unittest.TestCase):
    def test_inclusions(self):
        '''
            Test detection a inclusion. 
        '''
        result = defect_classifier()
        self.assertEquals(result, 0)

    def test_scratches(self):
        '''
            Test detection a scratches. 
        '''
        result = defect_classifier()
        self.assertEquals(result, 1)

    def test_patches(self):
        '''
            Test detection a patches. 
        '''
        result = defect_classifier()
        self.assertEquals(result, 2)

    def test_pitted_surface(self):
        '''
            Test detection a pitted_surface. 
        '''
        result = defect_classifier()
        self.assertEquals(result, 3)

    def test_crazing(self):
        '''
            Test detection a crazing. 
        '''
        result = defect_classifier()
        self.assertEquals(result, 4) 

    def test_rolled_in_scale(self):
        '''
            Test detection a rolled_in_scale. 
        '''
        result = defect_classifier()
        self.assertEquals(result, 5)      

    
    def test_localicer_result (unittest.TestCase):
        '''
            Test localicer result.
        ''' 
        l1, l2, l3, l4 = defect_localicer()
        self.assertTrue(l4 >= l1)
        self.assertTrue(l3 >= l2)
