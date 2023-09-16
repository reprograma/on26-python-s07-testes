import unittest


def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3, -3), -6)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 2), 2)

    def test_soma_positivo_negativo (self):
        self.assertEqual (soma(-5, 3),-2) 



def sub(a, b):
    return a - b

class TestSub(unittest.TestCase):
    def test_sub_positivos(self):
        self.assertEqual(sub(9, 3), 6)

    def test_sub_negativos(self):
        self.assertEqual(sub(-7, -3), -4)

    def test_sub_zero(self):
        self.assertEqual(sub(0, 2), -2)

    def test_sub_positivo_negativo (self):
        self.assertEqual(sub(-5, 3),-8) 



def mult(a, b):
    return a * b

class Testmult(unittest.TestCase):
    def test_mult_positivos(self):
        self.assertEqual(mult(3, 7), 21)

    def test_mult_negativos(self):
        self.assertEqual(mult(-3, -2), 6)

    def test_mult_zero(self):
        self.assertEqual(mult(0, 4), 0)

    def test_mult_positivo_negativo (self):
        self.assertEqual(mult(-5, 3),-15)



def divs(a, b):
    return a / b

class Testdivs(unittest.TestCase):
    def test_divs_positivos(self):
        self.assertEqual(divs(21, 7), 3)

    def test_divs_negativos(self):
        self.assertEqual(divs(-9, -3), 3)

    def test_divs_zero(self):
        self.assertEqual(divs(0, 4), 0)

    def test_divs_positivo_negativo (self):
        self.assertEqual(divs(-12, 3), -4)

if __name__ == "__main__":
    unittest.main()
    