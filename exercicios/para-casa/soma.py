def soma (a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    return a / b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-5, -3), -8)

class TestSubtracao(unittest.TestCase):
    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)

class TestMultiplicacao(unittest.TestCase):
    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(5, 3), 15)

class TestDivisao(unittest.TestCase):
    def test_divisao(self):
        self.assertEqual(divisao(4, 2), 2)


if __name__ == '__main__':
    unittest.main()