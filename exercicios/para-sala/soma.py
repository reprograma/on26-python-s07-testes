def soma(a, b):
    return a + b


import unittest


class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2,3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3, -3), -6)


    def test_soma_zeros (self):
        self.assertEqual (soma(0,0),0)

    def test_soma_positivo_negativo(self):
        self.assertEqual (soma(-5, 3), -2)


if __name__ == '__main__':
    unittest.main()


