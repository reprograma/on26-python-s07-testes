def calcular_media(numeros):
    if not numeros:
      return 0
    elif len(numeros) != 0:
        media = round(sum(numeros) / len(numeros), 2)
        return media

import math
import unittest
from exerciciotestes import calcular_media

#cenários de teste
# 1- lista vazia
# 2- lista com números negativos
# 3- lista com números positivos
# 4- lista com números positivos e negativos
# 5- lista com número zero
# 6- lista com números com resultados em dizimas, impressos com 2 casas decimais
# 7- lista com números decimais
# 8- lista com números com radicais 
# 9- lista com números fatorial

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def test_media_lista_numero_negativo(self):
        resultado = calcular_media([-2,-3,-3,-4,-3])
        self.assertEqual(resultado, -3)

    def test_media_lista_numero_positivos(self):
        resultado = calcular_media([2,3,3,4,3])
        self.assertEqual(resultado, 3)

    def test_media_lista_numero_positivos_negativos(self):
        resultado = calcular_media([-2,5,-3,4,6,2])
        self.assertEqual(resultado, 2)

    def test_media_lista_numeros_zero(self):
        resultado = calcular_media([0,0,0,0])
        self.assertEqual(resultado, 0)    

    def test_media_lista_resultado_dizima(self):
        resultado = calcular_media([6,2,2])
        self.assertEqual(resultado, 3.33)

    def test_media_lista_numero_decimal(self):
        resultado = calcular_media([6.5,2.9,2.3])
        self.assertEqual(resultado, 3.9)

    def test_media_lista_numeros_com_radicais(self):
        nume1 = 25
        nume2 = 16
        nume3 = 9
        raiz1 = math.sqrt(nume1) 
        raiz2 = math.sqrt(nume2)
        raiz3 = math.sqrt(nume3)
        resultado = calcular_media([raiz1, raiz2, raiz3])
        self.assertEqual(resultado, 4)   

    def test_media_lista_numeros_fatorial(self):
        nume1 = 3
        nume2 = 4
        nume3 = 2
        nume4 = 4
        fatorial1 = math.factorial(nume1) 
        fatorial2 = math.factorial(nume2)
        fatorial3 = math.factorial(nume3)
        fatorial4 = math.factorial(nume4)
        resultado = calcular_media([fatorial1, fatorial2, fatorial3, fatorial4])
        self.assertEqual(resultado, 14)  

if __name__ == '__main__':
    unittest.main()