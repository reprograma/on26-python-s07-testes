import math
import unittest
from calcular_media import calcular_media

#Cenários de Teste
# 1- Lista Vazia
# 2- Lista com números negativos
# 3- Lista com números positivos
# 4- Lista com números positivos e negativos
# 5- Lista com número zero
# 6- Lista com números com expoentes > 1
# 7- Lista com números com expoentes < 0
# 8- Lista com números com resultados em dizimas, impressos com 2 casas decimais
# 9- Lista com números decimais
# 10- Lista com números com radicais 
# 11- Lista com números fatorial
# 12- Lista com números irracionais





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

    def test_media_lista_neumero_com_expoentes(self):
        resultado = calcular_media([2**2, 3**2, 3**2, 4**2, 3**2, 1**1,1**1])
        self.assertEqual(resultado, 7)

    def test_media_lista_neumero_com_expoentes(self):
        resultado = calcular_media([3**-2, 4**-2, 3**-2, 4**-2, 3**-2, 2**-1,4**-1])
        self.assertEqual(resultado, 0.17)
        
    def test_media_lista_resultado_dizima(self):
        resultado = calcular_media([6,2,2])
        self.assertEqual(resultado, 3.33)

    def test_media_lista_numero_decimal(self):
        resultado = calcular_media([6.5,2.9,2.3])
        self.assertEqual(resultado, 3.9)
       
    def test_media_lista_numeros_com_radicais(self):
        nume_1 = 25
        nume_2 = 16
        nume_3 = 9
        raiz_1 = math.sqrt(nume_1) 
        raiz_2 = math.sqrt(nume_2)
        raiz_3 = math.sqrt(nume_3)
        resultado = calcular_media([raiz_1, raiz_2, raiz_3])
        self.assertEqual(resultado, 4)   

    def test_media_lista_numeros_fatorial(self):
        nume_1 = 3
        nume_2 = 4
        nume_3 = 2
        nume_4 = 4
        fatorial_1 = math.factorial(nume_1) 
        fatorial_2 = math.factorial(nume_2)
        fatorial_3 = math.factorial(nume_3)
        fatorial_4 = math.factorial(nume_4)
        resultado = calcular_media([fatorial_1, fatorial_2, fatorial_3, fatorial_4])
        self.assertEqual(resultado, 14)  

    def test_media_lista_numero_irracionais(self):
        resultado = calcular_media([math.pi, math.e, (1 + math.sqrt(5)) / 2])
        self.assertEqual(resultado, 2.49)     

        
if __name__ == '__main__':
    unittest.main()