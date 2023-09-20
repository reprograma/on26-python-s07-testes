import unittest
from calculo_media import calcular_media

class TesteCalcularMedia(unittest.TestCase):
    def teste_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def teste_media_lista_completa(self):
        resultado= calcular_media([6,8,4])
        self.assertEqual(resultado,6)
    
    def teste_media_lista_zero(self):
        resultado = calcular_media([0,0,0])
        self.assertEqual(resultado,0)
    
    def teste_media_lista_sem_nota(self):
        resultado = calcular_media([6,2,2])
        self.assertEqual(resultado,3.33)
    
    def teste_media_lista_ponto_extra(self):
        resultado = calcular_media([8,5,5])+1
        self.assertEqual(resultado,7)

    def teste_media_lista_desconto_ponto(self):
        resultado = calcular_media([6,6,8])-2
        self.assertEqual(resultado,4.67)




if __name__ =='__main__':
    unittest.main()