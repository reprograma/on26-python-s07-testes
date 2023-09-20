import unittest
from calculomedia import media

class teste_media_listas(unittest.TestCase):
    
    def Test_Lista_Vazia(self):
        lista_vazia = []
        media_esperadaV= 0
        calculo_mediaV= media(lista_vazia)
        self.assertEqual(calculo_mediaV,0)

    def Test_lista_unitaria(self):
        lista_unitaria=[1]
        media_esperada_unitaria=1
        calaculo_media_unitaria=media(lista_unitaria)
        self.assertEqual(calaculo_media_unitaria,1)

    def Test_Lista_Num_Repetidos(self):
        lista_numerosR = [7,7,7,7,7,7,7,7]
        media_espera_numerosR=7
        calculo_media_repetidos= media(lista_numerosR)
        self.assertEqual(calculo_media_repetidos,7)

    def Test_Lista_Num_Fora_Intervalo(self):
        lista_num_fora_intervalo=[100, 200]
        media_esperada_fi=None
        calculo_media_fi=media(lista_num_fora_intervalo)
        self.assertEqual(calculo_media_fi,150)

if __name__=='__main__':
    unittest.main()