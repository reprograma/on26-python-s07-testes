def soma(a, b):
  return a + b

def divisao(a, b):
  return a / b

def multiplicacao(a, b):
  return a * b

def subtracao(a, b):
  return a - b

import unittest

class teste_soma(unittest.TestCase): #Testes de soma
  def teste_soma_positivos(self):
    self.assertEqual(soma(2,3), 5)
  
  def teste_soma_negativos(self):
    self.assertEqual(soma(-5, -3), -8)

  def teste_soma_zero(self):
    self.assertEqual(soma(0,1), 1)

  def teste_soma_diferentes(self):
    self.assertEqual(soma(-5,2), -3)

class teste_subtracao(unittest.TestCase): #Testes subtração
  def teste_subtracao_positivos(self):
    self.assertEqual(subtracao(2,3), -1)

  def teste_subtracao_negativos(self):
    self.assertEqual(subtracao(-5, -3), -2)

  def teste_subtracao_diferentes(self):
    self.assertEqual(subtracao(-5, +3), -8)

  def teste_subtracao_zero(self):
    self.assertEqual(subtracao(0,1), -1)

class teste_divisao(unittest.TestCase): #Testes divisão
  def teste_divisao_positivos(self):
    self.assertEqual(divisao(10,5), 2)

  def teste_divisao_divisaoegativos(self):
    self.assertEqual(divisao(-10, -5), 2)

  def teste_divisao_diferentes(self):
    self.assertEqual(divisao(-10, +5), -2)

  def teste_divisao_zero(self):
    self.assertEqual(divisao(0,1), 0)


class teste_multiplicacao(unittest.TestCase): #Testes multiplicação
  def teste_multiplicacao_positivos(self):
    self.assertEqual(multiplicacao(2,3), 6)

  def teste_multiplicacao_negativos(self):
    self.assertEqual(multiplicacao(-5, -3), 15)

  def teste_multiplicacao_diferentes(self):
    self.assertEqual(multiplicacao(-5, +3), -15)

  def teste_multiplicacao_zero(self):
    self.assertEqual(multiplicacao(0,1), 0)

if __name__ == '__main__':
  unittest.main()

