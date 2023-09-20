import unittest

from codigo_fonte import calculaMedia
 

class testCalculaMedia (unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calculaMedia([])
        self.assertEqual(resultado,[])

    def test_media_lista_str_float(self):
        resultado = calculaMedia(['1.5',2.5, 2.5])
        self.assertAlmostEqual(resultado, 2.166)

    def test_media_lista_int_float(self):
        resultado = calculaMedia([2, 2.3, 3.5])
        self.assertEqual(resultado, 2.6)

    def test_media_lista_tupla_lista(self):
        resultado = calculaMedia([('10'), 20])
        self.assertEqual(resultado,[('10'), 20])

if __name__ == '__main__':
    unittest.main()

#realizado em grupo