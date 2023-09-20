import unittest

from calculo_media import calcular_media
# Lista vazia
# Zero
# Positivos
# Negativos
# Mista com positivos e negativos
# Lista float numero aproximado
# Divisão
# Multiplicação
# Potenciação




# Cenários de Teste
# 1. uma lista composta por zeros - resultado zero
# 2. uma lista vazia - resultado zero 

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def test_media_lista_zero(self):
        resultado = calcular_media([0, 0, 0])
        self.assertEqual(resultado, 0)
    
    def test_media_lista_positivos(self):
        resultado = calcular_media([6, 12, 18, 24, 29])
        self.assertEqual(resultado, 17.8)

    def test_media_lista_negativos(self):
        resultado = calcular_media([-12, -23, -2])
        self.assertEqual(resultado, -12.33)

    def test_media_lista_mista(self):
        resultado = calcular_media([-5, 25, -35])
        self.assertEqual(resultado, -5)

    def test_media_lista_float(self):
        resultado = calcular_media([3, 5, 9])
        self.assertEqual(resultado, 5.67)

    def test_media_lista_divisao(self):
        resultado = calcular_media([3/2, 5/2, 9/3])
        self.assertEqual(resultado, 2.33)

    def test_media_lista_multiplicacao(self):
        resultado = calcular_media([4*2, 5*3, 6*4])
        self.assertEqual(resultado, 15.67)

    def test_media_lista_potenciacao(self):
        resultado = calcular_media([2**2, 3**3, 4**4])
        self.assertEqual(resultado, 95.67)

if __name__ == '__main__':
    unittest.main()

