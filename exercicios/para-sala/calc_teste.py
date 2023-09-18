
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-5, -3), -8)
    
    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)

class TestSubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertEqual(subtracao(3, 2), 1)
        self.assertEqual(subtracao(2, 3), -1)
    
    def test_subracao_negativos(self):
        self.assertEqual(subtracao(-2, -3), 1)
        self.assertEqual(subtracao(-3, -2), -1)

    def test_subracao_zero(self):
        self.assertEqual(subtracao(0, 0), 0)

class TestMultiplicacao(unittest.TestCase):
    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(3, 2), 6)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-3, -2), 6)
        self.assertEqual(multiplicacao(-3, 2), -6)
    
    def test_multiplicacao_zero(self):
        self.assertEqual(multiplicacao(0, 0), 0)
        self.assertEqual(multiplicacao(0, 3), 0)

class TestDivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertEqual(divisao(10, 2), 5)
    
    def test_divisao_negativos(self):
        self.assertEqual(divisao(-10, 2), -5)

    def test_divisao_zero(self):
        self.assertEqual(multiplicacao(0, 3), 0)

if __name__ == "__main__":
    unittest.main()