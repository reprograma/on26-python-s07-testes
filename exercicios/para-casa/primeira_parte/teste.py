def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b != 0:
        return a / b
    
def mult(a, b):
    return a * b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2,3), 5)
        
    def test_soma_negativos(self):
        self.assertEqual(soma(-3,-3), -6)
        
    def teste_soma_zero(self):
        self.assertEqual(soma(0,0), 0)
    
    def test_soma_com_negativo(self):
        self.assertEqual(soma(7,-6), 1)
    
    def test_soma_float(self):
        self.assertEqual(soma(1.5, 2.5), 4)
        
class TestSubtracao(unittest.TestCase):
    def test_sub_positivos(self):
        self.assertEqual(sub(5,2), 3)
    
    def test_sub_negativos(self):
        self.assertEqual(sub(-3, -5), 2)
        
    def test_sub_zero(self):
        self.assertEqual(sub(0, 0), 0)
    
    def test_sub_neg_posit(self):
        self.assertEqual(sub(-7, 5), -12)
        
    def test_sub_float(self):
        self.assertEqual(sub(-1.2, -5.8), 4.6)
        
class TestDivisao(unittest.TestCase):
    def test_div_positivo(self):
        self.assertEqual(div(10, 5), 2)
    
    def test_div_neg(self):
        self.assertEqual(div(-20, -2), 10)
        
    def test_div_neg_posit(self):
        self.assertEqual(div(-10, 2), -5)
    
    def test_div_zero(self):
        self.assertEqual(div(0, 5), 0)
        
    def test_div_zero_erro(self):
        self.assertEqual(div(5, 0), None)
    
    def test_div_float(self):
        self.assertEqual(div(12.3, 2.5), 4.92)
        
class TestMultiplicacao(unittest.TestCase):
    def test_mult_positivo(self):
        self.assertEqual(mult(5, 2), 10)
    
    def test_mult_neg(self):
        self.assertEqual(mult(-10, -5), 50)
    
    def test_mult_float(self):
        self.assertEqual(mult(12, 2.5), 30)
        
    def test_mult_neg_posit(self):
        self.assertAlmostEqual(mult(12, 3.5), 42)
        
    def test_mult_zero(self):
        self.assertAlmostEqual(mult(24, 0), 0)
    
        

if __name__== '__main__':
    unittest.main()
    


