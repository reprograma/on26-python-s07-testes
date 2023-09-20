def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a/b

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2,3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3,-3), -6)

    def test_soma_zero(self):
        self.assertEqual(soma(0,2), 2)

    def test_soma_pos_neg(self):
        self.assertEqual(soma(4,-3),1)

class TestSubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertEqual(subtracao(5,3),2)

    def test_subtracao_negativos(self):
        self.assertEqual(subtracao(-5,-3), -2)

    def test_subtracao_zero(self):
        self.assertEqual(subtracao(0,2),-2)

    def test_subtracao_pos_neg(self):
        self.assertEqual(subtracao(-3,5),-8)

class TestMultiplicacao(unittest.TestCase):
    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(5,3), 15)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-5,-3),15)

    def test_multiplicacao_zero(self):
        self.assertEqual(multiplicacao(0,6), 0)
    
    def test_multiplicacao_pos_neg(self):
        self.assertEqual(multiplicacao(-3,6),-18)

class TestDivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertEqual(divisao(9,3), 3)

    def test_divisao_negativos(self):
        self.assertEqual(divisao(-10,-2), 5)

    def test_divisao_zero(self):
        self.assertEqual(divisao(0,6), 0)
    
    def test_divisao_pos_neg(self):
        self.assertEqual(divisao(-6,2),-3)


if __name__ == '__main__':
    unittest.main()