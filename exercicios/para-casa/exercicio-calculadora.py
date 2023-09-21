#criando o código a ser testado:

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero!"
    else:
        return a / b


# importando o framework:
import unittest

# criando a classe de teste e importante a biblioteca de testes:
class TestSoma(unittest.TestCase):

    # criando o método de teste:
    def teste_soma_positivos(self):
        # chamando a função a ser testada e informando o resultado esperado:
        self.assertEqual(soma(2, 3), 5)

    def teste_soma_negativos(self):
        self.assertEqual(soma(-3, -6), -9)

    def teste_soma_sinais_diferentes(self):
        self.assertEqual(soma(4, -7), -3)

    def teste_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)
        

class TestSubtracao(unittest.TestCase):
    
    def teste_subtracao_positivos(self):
        self.assertEqual(subtracao(8, 4), 4)

    def teste_subtracao_negativos(self):
        self.assertEqual(subtracao(-1, -6), 5)

    def teste_subtracao_sinais_diferentes(self):
        self.assertEqual(subtracao(-1, 6), -7)
    
    def teste_subtracao_zero(self):
        self.assertEqual(subtracao(9, 0), 9)


class TestMultiplicacao(unittest.TestCase):
    
    def teste_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(3, 8), 24)

    def teste_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-3, -5), 15)
    
    def teste_multiplicacao_sinais_diferentes(self):
        self.assertEqual(multiplicacao(-3, 5), -15)

    def teste_multiplicacao_zero(self):
        self.assertEqual(multiplicacao(5, 0), 0)


class TestDivisao(unittest.TestCase):
    
    def teste_divisao_positivos(self):
        self.assertEqual(divisao(10, 2), 5)

    def teste_divisao_negativos(self):
        self.assertEqual(divisao(-8, -4), 2)

    def teste_divisao_sinais_diferentes(self):
        self.assertEqual(divisao(8, -4), -2)

    def teste_divisao_zero(self):
        self.assertEqual(divisao(13, 2), 6.5)


# chamada para executar o teste:
if __name__ == '__main__':
    unittest.main()