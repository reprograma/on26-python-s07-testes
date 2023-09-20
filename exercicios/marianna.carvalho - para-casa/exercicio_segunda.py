def soma(a, b):
    return a + b
def subtracao(a,b):
    return a - (b)
def multiplicacao(a,b):
    return (a) * (b)
def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

import unittest

class TestSoma(unittest.TestCase):
   def test_soma_positivos(self): 
      self.assertEqual(soma(2, 3), 5)

   def test_soma_negativos(self):
      self.assertEqual(soma(-3, -3), -6)

   def test_soma_zeros(self):
      self.assertEqual(soma(0, 0), 0)

   def test_soma_positivo_negativo(self):
      self.assertEqual(soma(-5, +2), -3)

class TestSubtracao(unittest.TestCase):
   def test_subtracao_positivos(self):
      self.assertEqual(subtracao(5,2), 3)
   def test_subtracao_negativos(self):
      self.assertEqual(subtracao(6, 3), 3)
   def test_subtracao_zero(self):
      self.assertEqual(subtracao(0,0), 0) 

class TestMultiplicacao(unittest.TestCase):
   def test_multiplicacao_positivos(self):
      self.assertEqual(multiplicacao(3,3), 9)
   def test_multiplicacao_negativos(self):
      self.assertEqual(multiplicacao(-2,1),-2)
   def test_multiplicacao_zero(self):
      self.assertEqual(multiplicacao(0,0),0)

class TestDivisao(unittest.TestCase):
    def test_div_positivos(self):
        self.assertEqual(divisao(8, 2), 4)

    def test_div_negativos(self):
        self.assertEqual(divisao(-4, -2), 2)

    def test_div_zeros(self):
        with self.assertRaises(ZeroDivisionError):
            divisao((4, 0), 0)

if __name__ == '__main__':
   unittest.main()

