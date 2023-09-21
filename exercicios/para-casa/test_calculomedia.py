import unittest
from calculo_media import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def test_media_lista_num_posit(self):
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        resultado = calcular_media(numeros)
        self.assertAlmostEqual(resultado, 5.5)

    def test_media_lista_num_misturados(self):
        numeros = [-5, 0, 2, 3, -1]
        resultado = calcular_media(numeros)
        self.assertEqual(resultado, -0.2)

    def test_media_lista_num_negt(self):
        numeros = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        resultado = calcular_media(numeros)
        self.assertEqual(resultado, -5.5)

if __name__ == "__main__":
    unittest.main()

    