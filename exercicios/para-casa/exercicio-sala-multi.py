

def multiplicacao (a, b):
    return a * b
    
import unittest

class TestMultiplicacao (unittest.TestCase):
    def test_multiplicacao_positivos(self):
        self.assertEqual (multiplicacao(2, 3), 5) 
    
    def test_multiplicacao_negativos (self):
        self.assertEqual (multiplicacao(-2,-3),-5) 
   
    def test_multiplicacao_zeros (self):
        self.assertEqual (multiplicacao(0,0),0) 
        
    def test_multiplicacao_positivo_negativo (self):
        self.assertEqual (multiplicacao(-5, 3),-2) 

if __name__ == '__main__':
    unittest.main()