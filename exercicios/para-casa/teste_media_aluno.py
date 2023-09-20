import unittest
from media_aluno import calcular_media

class TestCalculoMedia(unittest.TestCase):

    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def test_media_notas_positivas(self):
        notas_aluno = [8.5, 9.0, 7.5, 6.0, 9.5]
        resultado = calcular_media(notas_aluno)
        self.assertAlmostEqual(resultado, 8.1, places=1)

    def test_media_notas_negativas(self):
        notas_aluno = [-8.5, -9.0, -7.5, -6.0, -9.5]
        resultado = calcular_media(notas_aluno)
        self.assertAlmostEqual(resultado, -8.1, places=1)

    def test_media_mistura_notas(self):
        notas_aluno = [8.5, -9.0, 7.5, -6.0, 9.5]
        resultado = calcular_media(notas_aluno)
        self.assertAlmostEqual(resultado, 2.1, places=1)

    def test_media_erros_de_digitacao(self):
        notas_aluno = [8.5, 9.0, 'A', 6.0, 9.5]
        with self.assertRaises(TypeError):
            calcular_media(notas_aluno)

if __name__ == '__main__':
    unittest.main()

