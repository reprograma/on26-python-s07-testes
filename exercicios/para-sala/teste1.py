def soma(a, b):
    return a + b

def subtacao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


import unittest


class testSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)


    def test_soma_negativos(self):
        self.assertEqual(soma(-3, -5), -8)  

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)    

    def test_soma_zero(self):
        self.assertEqual(soma())      


if __name__ == '__main__':
    unittest.main()        