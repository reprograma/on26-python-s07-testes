## ATIVIDADE SOBRE TESTES - SEMANA 07 - LAIS MEIRELES ALVES ##

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

import unittest

class TesteSoma(unittest.TestCase):
    def test_soma_positivos(self): #função que testa soma entre números positivos
        self.assertEqual(soma(2,3),5)

    def test_soma_negativos(self): #função que testa soma entre números negativos
        self.assertEqual(soma(-5,-3),-8)

    def test_soma_zero(self): #função que testa soma com zero
        self.assertEqual(soma(0,0),0)

    def test_soma_pos_neg(self): #função que testa soma entre números positivos e negativos
        self.assertEqual(soma(-8,4),-4)

## Tarefa de casa vai ser completar essa calculadora com as quatro operações (subtração, multiplicação e divisão) de acordo com o TDD

class TesteSubtracao(unittest.TestCase):
    def test_subtracao(self): #função que testa subtração entre números positivos
        self.assertEqual(subtracao(10,2),8)
        
    def test_subtracao_negativos(self): #função que testa subtração entre números negativos
        self.assertEqual(subtracao(-2,-5),3)

    def test_subtracao_zero(self): #função que testa subtração com zero
        self.assertEqual(subtracao(0,0),0)

    def test_subtracao_pos_neg(self): #função que testa subtração entre números positivos e negativos
        self.assertEqual(subtracao(8,-2),10)

class TesteMultiplicacao(unittest.TestCase):
    def test_multiplicacao(self): #função que testa multiplição entre números positivos
        self.assertEqual(multiplicacao(2,2),4)
    
    def test_multiplicacao_negativos(self): #função que testa multiplição entre números negativos
        self.assertEqual(multiplicacao(-2,-2),4)

    def test_multiplicacao_zero(self): #função que testa multiplição com zero
        self.assertEqual(multiplicacao(0,0),0)

    def test_multiplicacao_pos_neg(self): #função que testa multiplição entre números positivos e negativos
        self.assertEqual(multiplicacao(5,-2),-10)

class TesteDivisao(unittest.TestCase):
    def test_divisao(self): #função que testa divisão entre números positivos
        self.assertEqual(divisao(10,2),5)

    def test_divisao_neg(self): #função que testa divisão entre números negativos
        self.assertEqual(divisao(-10,-2),5)

    def test_divisao_zero(self): #função que testa divisão com zero no numerador
        self.assertEqual(divisao(0,2),0)

    def test_divisao_pos_neg(self): #função que testa divisão entre números positivos e negativos
        self.assertEqual(divisao(-20,2),-10)

    def test_divisao_decimal(self): #função que testa divisão entre números inteiros e fracionados
        self.assertEqual(divisao(5,0.1),50)

    # def test_divisao_dizima_decimal(self):
    #     self.assertEqual(divisao(10,3),3.3)

if __name__ == "__main__":
    unittest.main()




