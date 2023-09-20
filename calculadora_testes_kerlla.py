# Calculadora 

# Explicação do exercício: Desenvolva uma calculadora (utilizando a metodologia TDD) que tenha as 4 operações básicas e teste ela usando testes unitários.
# Operações básicas:

# Soma
# Subtração
# Multiplicação
# Divisão

import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(4, 4), 8)

    def test_soma_negativos(self):
        self.assertEqual(soma(-4, -4), -8)

    def test_soma_zeros(self):
        self.assertEqual(soma(0, 4), 4)
        
    def test_soma_positivo_negativo(self):
        self.assertEqual(soma(4, -4), 0)

        
def subtracao(a, b):
    return a - b

class TestSubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertEqual(subtracao(5, 3), 2)

    def test_subtracao_negativos(self):
        self.assertEqual(subtracao(-10, -4), -6)

    def test_subtracao_zero(self):
        self.assertEqual(subtracao(2, 1), 1)
        
    def test_subtracao_positivo_negativo(self):
        self.assertEqual(subtracao(4, -4), 8)


def multiplicacao(a, b):
    return a * b

class TestMultiplicacao(unittest.TestCase):
    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(3, 2), 6)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-2, -4), 8)

    def test_multiplicacao_zero(self):
        self.assertEqual(multiplicacao(2, 0), 0)
        
    def test_multiplicacao_positivo_negativo(self):
        self.assertEqual(multiplicacao(4, -4), -16)
        
def divisao(a, b):
    return a / b

class TestDivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertEqual(divisao(20, 10), 2)

    def test_divisao_negativos(self):
        self.assertEqual(divisao(-20, -10), 2)

    def test_divisao_zero(self):
        self.assertEqual(divisao(0, 1), 0)
        
    def test_divisao_positivo_negativo(self):
        self.assertEqual(divisao(10, -5), -2)


if __name__ == '__main__':
    unittest.main()
