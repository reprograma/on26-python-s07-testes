# Damaris Santos
# Entrega 18/09/23

def divisao(a, b):
    if a != b:
      return a / b

import unittest 

class TestDivisao(unittest.TestCase):
    def test_divisão_positivos(self):
        self.assertEqual(divisao(10, 2), 5)

    def test_div_negativos(self):
        self.assertEqual(divisao(-14, -7), 2)

    def test_div_misto(self):
        self.assertEqual(divisao(-12, 3), -4)

    def test_div_zero(self):
        self.assertEqual(divisao(0, 0), None) #não se pode dividir por 0

if __name__ == '__main__':
    unittest.main()