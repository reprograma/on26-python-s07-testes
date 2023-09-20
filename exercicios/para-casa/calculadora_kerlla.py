# Desenvolva uma calculadora (utilizando a metodolodia TDD) que tenha as 4 operações básicas
# e teste ela usando testes unitários.

# Operações básicas:
# Soma
# Subtração
# Multiplicação
# Divisão

import unittest

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Não é permitido dividir por zero.")
    return a / b

class TestCalculadora(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(3, 4), 7)

    def test_soma_negativos(self):
        self.assertEqual(soma(-2, -3), -5)

    def test_soma_zeros(self):
        self.assertEqual(soma(0, 0), 0)

    def test_soma_positivos_negativos(self):
        self.assertEqual(soma(-1, 2), 1)

    def test_subtracao_positivos(self):
        self.assertEqual(subtracao(10, 5), 5)

    def test_subtracao_negativos(self):
        self.assertEqual(subtracao(-6, -2), -4)

    def test_subtracao_positivos_negativos(self):
        self.assertEqual(subtracao(4, -3), 7)

    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(6, 5), 30)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-8, -4), 32)

    def test_multiplicacao_positivos_negativos(self):
        self.assertEqual(multiplicacao(8, -8), -64)

    def test_divisao_positivos(self):
        self.assertEqual(divisao(16, 4), 4)

    def test_divisao_negativos(self):
        self.assertEqual(divisao(-8, -2), 4)

    def test_divisao_positivos_negativos(self):
        self.assertEqual(divisao(12, -4), -3)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divisao(10, 0)

if __name__ == '__main__':
    unittest.main()
