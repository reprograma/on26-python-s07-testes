from contextlib import AbstractContextManager
from typing import Any
import unittest 
from calculo_media import calcula_media

class TestCalculaMedia(unittest.TestCase) :
    def test_media_vazia(self):
        resultado = calcula_media([])
        self.assertEqual(resultado, 0)




if __name__ == "__main__" :
    unittest.main()