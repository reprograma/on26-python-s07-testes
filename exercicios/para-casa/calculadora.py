def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b

    
import unittest

class TestSoma(unittest.TestCase):
    def teste_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def teste_soma_negativos(self):
        self.assertEqual(soma(-3, -3), -6)

    def teste_zero(self):
        self.assertEqual(soma(0, 0), 0)

    def teste_soma_neg_pos(self):
        self.assertEqual(soma(-2, 1), -1)


class TestSub(unittest.TestCase):
    def teste_subtrai_positivos(self):
        self.assertEqual(sub(3, 2), 1)

    def teste_subtrai_negativos(self):
        self.assertEqual(sub(-3, -5), 2)

    def teste_zero(self):
        self.assertEqual(sub(0, 0), 0)

    def teste_subtrai_neg_pos(self):
        self.assertEqual(sub(4, -1), 5)


class TestMult(unittest.TestCase):
    def teste_mult_positivos(self):
        self.assertEqual(mult(3, 2), 6)

    def teste_mult_negativos(self):
        self.assertEqual(mult(-3, -5), 15)

    def teste_zero(self):
        self.assertEqual(mult(0, 0), 0)

    def teste_mult_neg_pos(self):
        self.assertEqual(mult(4, -1), -4)


class TestDiv(unittest.TestCase):
    def teste_div_positivos(self):
        self.assertEqual(div(3, 3), 1)

    def teste_div_negativos(self):
        self.assertEqual(div(-6, -6), 1)

    def teste_zero(self):
        self.assertEqual(div(0, 0), None)

    def teste_div_neg_pos(self):
        self.assertEqual(div(-10, 2), -5)


if __name__ == "__main__":
    unittest.main()