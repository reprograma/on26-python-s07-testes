import unittest

def soma(a, b):
    return a + b

class TestAdicao(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3, -3), -6)

    def test_soma_zeros(self):
        self.assertEqual(soma(0, 0), 0)

    def test_soma_positivos_e_negativos(self):
        self.assertEqual(soma(3, -4), -1)


def sub(a, b):
    return a - b

class TestSubtracao(unittest.TestCase):
    def test_sub_positivos(self):
        self.assertEqual(sub(2, 1), 1)

    def test_sub_negativos(self):
        self.assertEqual(sub(-3, -3), 0)

    def test_sub_zeros(self):
        self.assertEqual(sub(0, 0), 0)

    def test_sub_positivos_e_negativos(self):
        self.assertEqual(sub(3, -4), 7)


def multi(a, b):
    return a * b

class TestMultiplicacao(unittest.TestCase):
    def test_multi_positivos(self):
        self.assertEqual(multi(2, 3), 6)

    def test_multi_negativos(self):
        self.assertEqual(multi(-3, -3), 9)

    def test_multi_zeros(self):
        self.assertEqual(multi(0, 0), 0)

    def test_multi_positivos_e_negativos(self):
        self.assertEqual(multi(3, -4), -12)


def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

class TestDivisao(unittest.TestCase):
    def test_div_positivos(self):
        self.assertEqual(div(3, 3), 1)

    def test_div_negativos(self):
        self.assertEqual(div(-3, -3), 1)

    def test_div_zeros(self):
        with self.assertRaises(ZeroDivisionError):
            div((4, 0), 0)

    def test_div_positivos_e_negativos(self):
        self.assertEqual(div(3, -4), -0.75)

if __name__ == '__main__':
    unittest.main()