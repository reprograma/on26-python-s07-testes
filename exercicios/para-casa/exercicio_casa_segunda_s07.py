# Exercício de casa: calculadora (soma, subtração, multiplicação, divisão) Realizado em grupo

def soma (a, b):
    return a + b

def subtracao (a, b):
    return a - b 

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    if b != 0:
        return a / b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual (soma(2, 3), 5)

    def test_soma_negativos(self):
      self.assertEqual(soma(-3, -3), -6)
    
    def test_soma_positivo_negativo(self):
        self.assertEqual(soma (-5, +2),-3)
    
    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)
    

class TestSubtracao (unittest.TestCase):
    def test_sub_positivos(self):
        self.assertEqual (subtracao(3, 2),1)
    
    def test_sub_nagativos(self):
        self.assertEqual (subtracao(-3, -3),0)

    def test_sub_positivo_negativo(self):
        self.assertEqual (subtracao(-5, +2), -7)
    
    def test_sub_zero(self):
        self.assertEqual(subtracao(0,0),0)


class TestMultiplicacao (unittest.TestCase):
    def test_mult_positivos(self):
        self.assertEqual(multiplicacao(3, 2),6)
    
    def test_mult_negativos(self):
        self.assertEqual (multiplicacao(-3,-3),9)
    
    def test_mult_positivo_negativo(self):
        self.assertEqual (multiplicacao(-5, +2),-10)
    
    def test_mult_zero(self):
        self.assertEqual(multiplicacao(0, 0),0)


class TestDivisao (unittest.TestCase):
    def test_div_positivos(self):
        self.assertEqual(divisao(4, 2),2)

    def test_div_negativos(self):
        self.assertEqual(divisao(-3, -3),1)

    def test_div_positivo_negativo(self):
        self.assertEqual(divisao(-6, +3),-2)
    
    def test_div_zero(self):
        self.assertEqual(divisao(2, 0), None)


if __name__ == '__main__': #isso aqui é obrigatório para rodar
    unittest.main()