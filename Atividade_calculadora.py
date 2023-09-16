def soma (a,b):
    return a + b

def sub (a,b):
    return a - b

def div (a,b):
    if b != 0:
        return a/b

def mult (a,b):
    return a * b

import unittest

class TestSum(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3),5)

    def test_soma_negativo(self):
        self.assertEqual(soma(-5,-3), -8)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)
    
    def test_soma_postivo_negativo(self):
        self.assertEqual(soma(-6, 2), -4)

class TestSub(unittest.TestCase):
    def test_sub_positivo(self):
          self.assertEqual(sub(10, 3), )

    def test_sub_negativo_float(self):
        self.assertEqual(sub(-4,-2), -2)

    def test_sub_zero(self):
        self.assertEqual(sub(0, 0), 0)
    
    def test_sub_positivo_negativo(self):
        self.assertEqual(sub(-6, 2), -8)

class TestDiv(unittest.TestCase):
    def test_div_positive(self):
          self.assertEqual(div(10, 2), 5)

    def test_div_negativo_float(self):
        self.assertEqual(div(-10, -5), -15)

    def test_div_zero1(self):
        self.assertEqual(div(2, 0), None)

    def test_div_zero2(self):
        self.assertEqual(div(0, 3), 0)
    
    def test_div_positivo_negativo(self):
        self.assertEqual(div(-9, 2), -4.5)

class TestMult(unittest.TestCase):
    def test_mult_positivo(self):
          self.assertEqual(mult(9, 2), 18)

    def test_mult_negativo(self):
        self.assertEqual(mult(-9,-2), 18)

    def test_mult_zero(self):
        self.assertEqual(mult(0, 0), 0)
    
    def test_mult_positivo_negativo(self):
        self.assertEqual(mult(-10, 2), -20)

if __name__ == '__main__':
    unittest.main()
