def soma(a, b):
    return a + b

def sub(c, d):
    return c - d

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
       return a / b
    else:
        return f"Não é possível dividir um número por zero."
    
    
    

import unittest

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(3, 4), 7)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3, -3), -6)
    
    def soma_zero(self):
        self.assertEqual(soma(0,0), 0)

    def test_soma_negativos_positivos(self):
        self.assertEqual(soma(-6, 4), -2)

class TestSubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertEqual(sub(4, 2), 2)

    def test_subtracao_negativos(self):
        self.assertEqual(sub(-2, -4), 2)
    
    def test_subtracao_zero(self):
        self.assertEqual(sub(0, 0), 0)
    
    def test_subtracao_negativos_positivos(self):
        self.assertEqual(sub(2, -4), 6)

class TestMultiplicacao(unittest.TestCase):
    def test_multiplicacao_positivos(self):
        self.assertEqual(mult(4, 2), 8)

    def test_multiplicacao_negativos(self):
        self.assertEqual(mult(-2, -4), 8)
    
    def test_multiplicacao_zero(self):
        self.assertEqual(mult(0, 0), 0)
    
    def test_multiplicacao_negativos_positivos(self):
        self.assertEqual(mult(2, -4), -8)

class TestDivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertEqual(div(4, 2), 2)

    def test_divisao_negativos(self):
        self.assertEqual(div(-4, -2), 2)
    
    def test_divisao_zero(self):
        self.assertEqual(div(0, 0), 0)
    
    def test_divisao_negativos_positivos(self):
        self.assertEqual(div(2, -4), -0.5) 


if __name__ == '__main__':
    unittest.main()