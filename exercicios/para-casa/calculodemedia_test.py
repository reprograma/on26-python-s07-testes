import unittest
from exercicios_de_media import calcular_media

#Testes 

# 1 - Lista de valores vazios
# 2 - Lista de valores positivos
# 3 - Lista de valores negativos
# 4 - Lista de valores decimais 
# 5 - Lista de valores inteiros 

class TestCalcularMedia(unittest.TestCase):
    def teste_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)
    
    def teste_media_lista_positivos(self):
        resultado = calcular_media([9, 2, 4, 6, 3])
        self.assertEqual(resultado, 4.8)
   
    def teste_media_lista_negativos(self):
        resultado = calcular_media([-3, -7, -8, -1, -4])
        self.assertEqual(resultado, -4.6)
    
    def teste_media_lista_decimais(self):
        resultado = calcular_media([2.3, 6.7, 9.5, 8.2, 5.4])
        self.assertEqual(resultado, 6.42)
    
    def teste_media_lista_inteiros(self):
        resultado = calcular_media([-1, 7, 8, -3, -4])
        self.assertEqual(resultado, 1.40)

if __name__ == '__main__':
    unittest.main()



    