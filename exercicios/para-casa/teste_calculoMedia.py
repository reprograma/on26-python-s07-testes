import unittest
from exerc_calculo_media_sabado import calcular_media

class TesteCalularMedia(unittest.TestCase):
    def teste_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def teste_media_positivas(self):
        resultado = calcular_media([1,2,3])
        self.assertEqual(resultado, 2)

    def teste_media_negativas(self):
        resultado = calcular_media([-4,-10,-6,-4])
        self.assertEqual(resultado, -6)

    def teste_media_float_positivas(self):
        resultado = calcular_media([-3.2, -4.5, 8.0, 9.6])
        self.assertEqual(resultado, 2.47)

    def teste_media_float_negativas(self):
        resultado = calcular_media([-5.3, -8.7, -3.3, -9.9])
        self.assertEqual(resultado, -6.8)

    def teste_media_positivo_negativo(self): #sendo eles 4 notas, 2 positivas e 2 negativas
        resultado = calcular_media([9, -3.2, 7, -6.7])
        self.assertEqual(resultado, 1.53)

    def teste_media_apenas_1_numero(self):
        resultado = calcular_media([1])
        self.assertEqual(resultado, 1)

if __name__ == "__main__":
    unittest.main()