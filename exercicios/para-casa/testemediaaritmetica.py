import unittest
from mediaaritmetica import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)
    
    def test_numeros_positivos(self):
        resultado = calcular_media([5, 5, 5])
        self.assertEqual(resultado, 5)

    def test_numeros_negativos(self):
        resultado = calcular_media([-6, -4, -2])
        self.assertTrue(resultado, -4)
   
    def test_resultado_errado(self):
        resultado = calcular_media([5, 5, 5])
        self.assertNotEqual(resultado, 6)


if __name__ == "__main__":
    unittest.main()