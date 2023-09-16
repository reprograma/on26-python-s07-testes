# Damaris Santos
# Entrega 18/09/23

def subtracao(a, b):
  return a - b

import unittest

class TestSubtracao(unittest.TestCase):
    def test_sub_positivos(self):
        self.assertEqual(subtracao(5, 3),2)

    def test_sub_negativos(self):
        self.assertEqual(subtracao(-8, -2),-6)

    def test_sub_zero(self):
        self.assertEqual(subtracao(0, 0), 0)

    def test_sub_mista(self):
        self.assertEqual(subtracao(-9, 11), -20)  

if __name__ == '__main__':
    unittest.main()