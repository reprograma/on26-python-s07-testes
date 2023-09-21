def soma(a,b):
    return a + b

def sub(c,d):
    return c - d

def div(e,f):
    return e / f

def multiplicacao(g,h):
    return g * h

import unittest

class TestCalculadora(unittest.TestCase):

    def teste_soma_positivos(self):

        self.assertEqual(soma(2,3),5)


    def test_soma_negativos(self):

        self.assertEqual(soma(-3,-3),-6)

    def test_soma_zero(self):

        self.assertEqual(soma(-3,3),0)

    def test_sub_positivos(self):
        self.assertEqual(sub(2,2), 0)   

    def test_sub_negativos(self):
        self.assertEqual(sub(-4,-4),-8)    

    def test_div_positivo(self):
        self.assertEqual(div(10,2), 5)

    def test_div_negativos(self):
        self.assertEqual(div(-10, -2), 5)   

    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(5,5), 25)     

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-10, -10), 100)    
 

if __name__ == '__main__':

    unittest.main()
