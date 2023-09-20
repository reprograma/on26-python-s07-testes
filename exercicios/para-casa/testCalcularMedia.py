import unittest
from calcularMedia import calcularMedia

#CENÁRIOS DE TESTE:
# 1. Lista de números vazia
# 2. Lista onde todos os números são iguais a 0
# 3. Lista onde todos os números são negativos
# 4. Lista que contém números decimais
# 5. Lista com números positivos e negativos

class TestCalcularMedia(unittest.TestCase):
    def testMediaListaVazia(self):
        resultado = calcularMedia([])
        self.assertEqual(resultado, 0)

    def testListaZeros(self):
        resultado = calcularMedia([0, 0, 0])
        self.assertEqual (resultado, 0)

    def testListaNegativos(self):
        resultado = calcularMedia([-2,-4,-3,-9])
        self.assertEqual(resultado, -4.5)

    def testListaDecimais(self):
        resultado = calcularMedia([3.4,5.6,7.5,9.2])
        self.assertEqual(resultado, 6.425)

    def testListaPosENeg(self):
        resultado = calcularMedia([-2,5,-9,1])
        self.assertEqual(resultado, -1.25)


if __name__== "__main__":
    unittest.main()