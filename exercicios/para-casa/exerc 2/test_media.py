import unittest #importando o modulo
from media import media


class TestMedia(unittest.TestCase): #fazendo a minha class herdar o test case do modulo
    def test_media_10_e_15_deve_retornar_12emeio(self):
        self.assertEqual(media(10, 15), 12.5)


unittest.main(verbosity=2)
