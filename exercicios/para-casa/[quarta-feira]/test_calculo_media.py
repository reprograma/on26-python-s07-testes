import unittest
from calculo_media import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def test_media_numeros_positivos(self):
        resultado = calcular_media([1, 2, 3, 4, 5])
        self.assertEqual(resultado, 3.0)  

    def test_media_numeros_negativos(self):
        resultado = calcular_media([-1, -2, -3, -4, -5])
        self.assertEqual(resultado, -3.0)  

    def test_media_numeros_positivos_negativos(self):
        resultado = calcular_media([-1, 2, -3, 4, -5])
        self.assertEqual(resultado, -0.6) 

    def test_media_inteiros_e_floats_misturados(self):
        resultado = calcular_media([1, 2.5, 3, -4.7, 5])
        self.assertAlmostEqual(resultado, 1.36) 

    def test_media_valores_nulos(self):
        resultado = calcular_media([0, 0, 0])
        self.assertEqual(resultado, 0.0) 

if __name__ == '__main__':
    unittest.main()