import unittest #importando o modulo
from media import media


class TestMedia(unittest.TestCase): #fazendo a minha class herdar o test case do modulo
    def test_media_10_e_15_deve_retornar_12emeio(self):
        self.assertEqual(media(10, 15), 12.5)
    
    def test_media_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            media('10', 15)

    def test_media_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            media(10, '15')

    def test_media_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 10),
            (10, 5, 7.5),
            (8, 10, 9),
            (5, 9, 7),
            (1.5, 1.5, 1.5),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(media(x, y), saida)




unittest.main(verbosity=2)
