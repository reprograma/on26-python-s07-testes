def soma (a,b):
    return a + b
def subtracao (a,b):
    return a - b
def multiplicacao (a,b):
    return a * b
def divisao (a,b):
    if b != 0:
        return a / b
    #if b != 0:
    #    return a / b
    # raise ZeroDivisionError

import unittest

class TestSoma (unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual (soma(2, 3), 5) 
    
    def test_soma_negativos (self):
        self.assertEqual (soma(-2,-3),-5) 
   
    def test_soma_zeros (self):
        self.assertEqual (soma(0,0),0) 
        
    def test_soma_positivo_negativo (self):
        self.assertEqual (soma(-5, 3),-2) 


class TestSub (unittest.TestCase):
    def test_sub_positivos (self):
        self.assertEqual (subtracao(2,1),1)

    def test_sub_negativos (self):
        self.assertEqual (subtracao(-4,-1),-3)

    def test_sub_zero (self):
        self.assertEqual (subtracao(0,0),0)

    def test_sub_positivos_negativos (self):
        self.assertEqual (subtracao(-2,1),-3)
        
class TestMulti (unittest.TestCase):
    def test_sub_positivos (self):
        self.assertEqual (multiplicacao(2,1),2)

    def test_sub_negativos (self):
        self.assertEqual (multiplicacao(-4,-1),4)

    def test_sub_zero (self):
        self.assertEqual (multiplicacao(0,0),0)

    def test_sub_positivos_negativos (self):
        self.assertEqual (multiplicacao(-2,1),-2)
        
class TestDiv (unittest.TestCase):
    def test_sub_positivos (self):
        self.assertEqual (divisao(2,2),1)

    def test_sub_negativos (self):
        self.assertEqual (divisao(-4,-2),2)

    def test_sub_zero_divisor (self):
        self.assertEqual (divisao(5,0),None)
        # with self.assertRaises(ZeroDivisionError):
    
    def test_sub_zero_dividendo (self):
        self.assertEqual (divisao(0,10),0)

    def test_sub_positivos_negativos (self):
        self.assertEqual (subtracao(-2,1),-3)


if __name__ == '__main__':
    unittest.main()