import unittest
from atividade_testes_media import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def test_media_lista_zeros(self): #Teste que calcula a média no caso em que todos os números da lista são zero
        resultado = calcular_media ([0,0,0])
        self.assertEqual(resultado, 0)

    def test_media_numeros_pares(self):
        resultado = calcular_media([2,4,2,8,2]) #Teste que calcula a média no caso de números pares
        self.assertEqual(resultado, 3.6)

    def test_media_float(self): #Teste que calcula a média no caso em que todos os números são números com casas decimais
        resultado = calcular_media([1.5, 2.5, 8.5])
        self.assertAlmostEqual(resultado, 4.167, places=3)

if __name__ == "__main__":
    unittest.main()
    