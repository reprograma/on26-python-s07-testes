"""Calculadora"""

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b

import unittest


class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)    # números apenas positivos
        self.assertEqual(soma(-3, -3), -6) # números  apenas negativos
        self.assertEqual(soma(0, 0), 0)    # números zero
        self.assertEqual(soma(-6, 4), -2)  # números positivos e negativos

class TestSubtracao(unittest.TestCase):
    def test_subtracao(self):
        self.assertEqual(subtracao(3, 2), 1)     # números apenas positivos
        self.assertEqual(subtracao(-3, 0), -3)   # números  apenas negativos
        self.assertEqual(subtracao(0, 0), 0)     # números zero
        self.assertEqual(subtracao(-6, 4), -10)  # números positivos e negativos

class TestMultiplicacao(unittest.TestCase):
    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 2), 6)     # números apenas positivos
        self.assertEqual(multiplicacao(-3, 0), 0)    # números apenas negativos
        self.assertEqual(multiplicacao(0, 0), 0)     # números zero
        self.assertEqual(multiplicacao(-6, 4), -24)  # números positivos e negativos

class TestDivisao(unittest.TestCase):
    def test_divisao(self):
        self.assertEqual(divisao(6, 2), 3)     # números apenas positivos
        self.assertEqual(divisao(-6, -2), 3)   # números apenas negativos
        self.assertEqual(divisao(0, 0 ), None) # números zero
        self.assertEqual(divisao(-6, 2), -3)   # números positivos e negativos


if __name__ == '__main__':
    unittest.main()