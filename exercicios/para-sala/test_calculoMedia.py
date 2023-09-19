import unittest
from calculo_media import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)



if __name__ == '__main__':
    unittest.main()