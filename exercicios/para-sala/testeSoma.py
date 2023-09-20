import unittest

def soma (a, b):
    return a + b

def dividir (a, b):
    if b != 0:
        return a / b

def subtrair (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2,3),5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3, -3), -6)

    def test_soma_zerada(self):
        self.assertEqual(soma(0,0),0)

    def test_soma_diferentes(self):
        self.assertEqual(soma(-2,4),2)

# fazer divisão, subtração e multiplicação
class TestDividir(unittest.TestCase):
    def test_dividir_positivos(self):
        self.assertEqual(dividir(10,2),5)

    def test_dividir_negativos(self):
        self.assertEqual(dividir(-15, -3), 5)

    def test_dividir_zerada(self):
        self.assertEqual(dividir(0,0),None)

    def test_dividir_diferentes(self):
        self.assertEqual(dividir(-4,2),-2)

class TestSubtrair(unittest.TestCase):
    def test_subtrair_positivos(self):
        self.assertEqual(subtrair(4,2),2)

    def test_subtrair_negativos(self):
        self.assertEqual(subtrair(-3, -3), 0)

    def test_subtrair_zerada(self):
        self.assertEqual(subtrair(0,0),0)

    def test_subtrair_diferentes(self):
        self.assertEqual(subtrair(-2,4),-6)

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(5,5),25)

    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-6, -8), 48)

    def test_multiplicar_zerada(self):
        self.assertEqual(multiplicar(0,0),0)

    def test_multiplicar_diferentes(self):
        self.assertEqual(multiplicar(-6,7),-42)

if __name__ == '__main__':
    unittest.main()