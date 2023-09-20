import unittest

from cod import calculaMedia

class testCalculaMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calculaMedia([])
        self.assertEqual(resultado, 0)

    def test_media_lista_string_float(self):
         resultado = calculaMedia(['1.0', 2.0, 3.0])
         self.assertEqual(resultado, 2)
    
    def test_media_lista_int_float(self):
        resultado = calculaMedia([1, 2.0, 3.0])
        self.assertEqual(resultado, 2.0)

    def test_media_lista_tupla_lista(self):
        resultado = calculaMedia([('10'), 20, 30])
        self.assertEqual(resultado,[('10'), 20])

if __name__ == '__main__':
    unittest.main()

# se a lista tiver uma entrada em str
# se 