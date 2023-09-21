import unittest
from calculo_media import calcular_media


#Cenários de Teste
#1. uma lista composta por zeros - resultado zero
#2. uma lista vazia - resultado zero


class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)



if __name__ == '__main__':
    unittest.main()

