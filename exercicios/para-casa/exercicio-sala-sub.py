

def subtrair (a, b):
    return a - b
    
import unittest

class TestSubtrair (unittest.TestCase):
    def test_subtrair_positivos(self):
        self.assertEqual (subtrair(2, 3), 5) 
    
    def test_subtrair_negativos (self):
        self.assertEqual (subtrair(-2,-3),-5) 
   
    def test_subtrair_zeros (self):
        self.assertEqual (subtrair(0,0),0) 
        
    def test_subtrair_positivo_negativo (self):
        self.assertEqual (subtrair(-5, 3),-2) 

if __name__ == '__main__':
    unittest.main()