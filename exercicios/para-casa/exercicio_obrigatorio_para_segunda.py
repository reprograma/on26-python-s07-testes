# ## Calculadora :calling:

# - Explicação do exercício: Desenvolva uma calculadora (utilizando a metodologia TDD) 
# que tenha as 4 operações básicas e teste ela usando testes unitários.
# - Operações básicas: 
#     - Soma 
#     - Subtração
#     - Multiplicação
#     - Divisão

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
    def teste_soma_positivos(self):
        self.assertEqual(soma(2,3), 5)

    def teste_soma_negativos(self):
        self.assertEqual(soma(-3, -4), -7)

    def teste_soma_zero(self):
        self.assertEqual(soma(0,0), 0)

    def teste_soma_pos_neg(self):
        self.assertEqual(soma(-5,8), 3)
        self.assertEqual(soma(-2,1), -1)

class TestSubtracao(unittest.TestCase):
    def teste_subt_positivos(self):
        self.assertEqual(subtracao(5,4), 1)

    def teste_subt_negativos(self):
        self.assertEqual(subtracao(-5,-7), 2)
        self.assertEqual(subtracao(-5,-3), -2)

    def teste_subt_pos_e_neg(self):
        self.assertEqual(subtracao(5,-4), 9)
        self.assertEqual(subtracao(-5,4), -9)

    def teste_subt_zero(self):
        self.assertEqual(subtracao(0,0), 0)

class TestMultiplicacao(unittest.TestCase):
    def teste_mult_positivos(self):
        self.assertEqual(multiplicacao(5,4), 20)

    def teste_mult_negativos(self):
        self.assertEqual(multiplicacao(-5,-7), 35)

    def teste_mult_pos_e_neg(self):
        self.assertEqual(multiplicacao(5,-4), -20)

    def teste_mult_zero(self):
        self.assertEqual(multiplicacao(0,0), 0)
        self.assertEqual(multiplicacao(0,4), 0)

class TestDivisao(unittest.TestCase):
    def teste_div_positivos(self):
        self.assertEqual(divisao(20,2), 10)

    def teste_div_negativos(self):
        self.assertEqual(divisao(-30,-10), 3)

    def teste_div_pos_e_neg(self):
        self.assertEqual(divisao(10,-2), -5)

    def teste_div_zero(self):
        self.assertEqual(divisao(0,1), 0)

if __name__ == '__main__':
    unittest.main()

