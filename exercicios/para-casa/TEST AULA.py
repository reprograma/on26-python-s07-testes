import unittest

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b): #ideia compartilhada em chamada na sala de aula.
    if b == 0:
        raise ZeroDivisionError
    return a/b

class TestSoma(unittest.TestCase):
    def test_soma_positivos (self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3, -3), -6)


class TestSubtracao(unittest.TestCase):
    def test_sub_positivos(self):
        self.assertEqual(subtracao(5, 2), 3)
    
    def test_sub_negativos(self): 
        self.assertEqual(subtracao(-5, 2), -7)
        self.assertEqual(subtracao(-5, -2), -3)
    # prof, não senti necessidade de fazer com o 0 na subtração, porque, ainda que zero não seja positivo, ele se enquadra no primeiro def.

class TestMultiplicacao(unittest.TestCase):
    def test_multi_positivos(self):
        self.assertEqual(multiplicacao(5, 7), 35)

    def test_multi_negativos_positivos(self): 
        self.assertEqual(multiplicacao(-5, 6), -30) #por propriedade comutativa, o inverso funciona da mesma maneira
    
    def test_multi_negativos(self):
        self.assertEqual(multiplicacao(-2, -3), 6)

    def test_multi_zero(self):
        self. assertEqual(multiplicacao(2, 0), 0)

class TestDivisao(unittest.TestCase):
    def test_div_positivos(self):
        self.assertEqual(divisao(9, 3), 3)
    
    def test_div_positivos_negativos(self):
        self.assertEqual(divisao(10, -2), -5)
    
    def test_div_negativos_positivos(self):
        self.assertEqual(divisao(-6, 2), -3)
    
    def test_div_negativos(self):
        self.assertEqual(divisao(-5, -2), 2.5)
    
    def test_div_numerador_zero(self):
        self.assertEqual(divisao(0, 2), 0)
                
        
if __name__ == '__main__':
    unittest.main()


