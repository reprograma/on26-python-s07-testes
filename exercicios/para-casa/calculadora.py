# Exerc calculadora

def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    if b != 0:
        return a / b


import unittest

class TesteSoma(unittest.TestCase):
    def test_soma_positivo(self):
        self.assertEqual(soma(8,7),15)

    def test_soma_negativo(self):
        self.assertEqual(soma(-4,-5), -9)

    def test_soma_zero(self):
        self.assertEqual(soma(0,0),0)

    def test_soma_postivo_negativo(self):
        self.assertEqual(soma(-6,3),-3)

class TestSubracao(unittest.TestCase):
    def test_sub_positivo(self):
          self.assertEqual(subtracao(10,4),6)

    def test_sub_negativo(self):
        self.assertEqual(subtracao(-8,-5), -3)

    def test_sub_zero(self):
        self.assertEqual(subtracao(0,0),0)

    def test_sub_positivo_negativo(self):
        self.assertEqual(subtracao(-8,2),-10)

class TestMult(unittest.TestCase):
    def test_mult_positivo(self):
          self.assertEqual(multiplicacao(15,3),45)

    def test_mult_negativo(self):
        self.assertEqual(multiplicacao(-6,-3),18)

    def test_mult_zero(self):
        self.assertEqual(multiplicacao(0,0),0)

    def test_mult_positivo_negativo(self):
        self.assertEqual(multiplicacao(-7,3),-21)

class TestDiv(unittest.TestCase):
    def test_div_positivo(self):
          self.assertEqual(divisao(24,4),6)

    def test_div_negativo_float(self):
        self.assertEqual(divisao(-8,-5), 1.6)

    def test_div_zero1(self):
        self.assertEqual(divisao(2,0),None)

    def test_div_zero2(self):
        self.assertEqual(divisao(0,3),0)

    def test_div_positivo_negativo(self):
        self.assertEqual(divisao(-11,2),-5.5)


if __name__ == '__main__':
    unittest.main()