def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

import unittest

class testSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2,3),5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3,-3),-6)
    
    def test_soma_zero(self):
        self.assertEqual(soma(0,0),0)

class testSub(unittest.TestCase):
    def test_sub_positivos(self):
        self.assertEqual(sub(4,2),2)

    def test_sub_negativos(self):
        self.assertEqual(sub(-3,-3),0)
    
    def test_sub_zero(self):
        self.assertEqual(sub(0,-2),2)

class testMult(unittest.TestCase):
    def test_mult_positivos(self):
        self.assertEqual(mult(2,3),6)

    def test_mult_negativos(self):
        self.assertEqual(mult(-3,-3),9)
    
    def test_mult_zero(self):
        self.assertEqual(mult(5,0),0)

class testDiv(unittest.TestCase):
    def test_div_positivos(self):
        self.assertEqual(div(10,5),2)

    def test_div_negativos(self):
        self.assertEqual(div(-10,-5),2)
    
    def test_div_zero(self):
        self.assertEqual(div(0,-5,),0)

if __name__ == '__main__':
    unittest.main()