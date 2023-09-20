def calcular_media(testes):
    soma = 0
    for teste in testes:
        soma += teste.countTestCases()

    media = soma / len(testes)
    return media


def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b


import unittest


class testSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-3, -5), -8)  

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)    

    def test_soma_positivo_negativo(self):
        self.assertEqual(soma(-2, 1), -1)      


class testSubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertEqual(subtracao(2, 3), -1)

    def test_subtracao_negativos(self):
        self.assertEqual(subtracao(-3, -5), 2)  

    def test_subtracao_zero(self):
        self.assertEqual(subtracao(0, 0), 0)    

    def test_subtracao_positivo_negativo(self):
        self.assertEqual(subtracao(-2, 1), -3)


class testMultiplicacao(unittest.TestCase):
    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(2, 3), 6)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-3, -5), 15)  

    def test_multiplicacao_zero(self):
        self.assertEqual(multiplicacao(0, 0), 0)    

    def test_multiplicacao_positivo_negativo(self):
        self.assertEqual(multiplicacao(-2, 1), -2)        


class testDivisao(unittest.TestCase):
    def test_divisao_positivos(self):
        self.assertEqual(divisao(3, 2), 1.5)

    def test_divisao_negativos(self):
        self.assertEqual(divisao(-5, -2), 2.5)  

    def test_divisao_zero(self):
        self.assertEqual(divisao(4, 0), None)    

    def test_divisao_positivo_negativo(self):
        self.assertEqual(divisao(-2, 1), -2)


if __name__ == '__main__':
    testes = [testSoma(), testSubtracao(), testMultiplicacao(), testDivisao()]
    media = calcular_media(testes)

    print(f"A média dos testes é {media}")    