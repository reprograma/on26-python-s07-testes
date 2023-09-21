import unittest
from calculo_media import calcular_media

# Cenários de teste
## 1. uma lista vazia - resultado zero
## 2. uma lista composta por zeros - resultado zero
## 3. uma lista composta apenas por números negativos - resultado negativo
## 4. uma lista composta apenas por números positivos - resultado positivo
## 5. uma lista composta por números positivos e negativos (cenário 1) - resultado negativo
## 6. uma lista composta por números positivos e negativos (cenário 2) - resultado positivo
## 7. uma lista composta por str - resultado erro (TypeError)
## 8. argumentos booleanos para função calcular_media() - resultado erro (TypeError)
## 9. lista composta por um único elemento - retorna o próprio elemento

# Cenário descartado:
## uma lista composta por ao menos um número tipo float - resultado float
###     def test_media_lista_float(self):
###         resultado = calcular_media([1.0, 2, 3, 4, 5])
###         self.assertEqual(resultado,3.0)
###         print(type(resultado))
# foi descartado quando se percebeu que o retorno da função calcular_media(), e portanto, 
# o tipo da variável "resultado" em qualquer cenário de teste é float

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        resultado = calcular_media([])
        self.assertEqual(resultado, 0)

    def test_media_lista_zeros(self):
        resultado = calcular_media([0,0,0])
        self.assertEqual(resultado,0)

    def test_media_lista_negativos(self):
        resultado = calcular_media([-1,-2,-3])
        self.assertEqual(resultado,-2)

    def test_media_lista_positivos(self):
        resultado = calcular_media([1,2,3])
        self.assertEqual(resultado,2)
    
    def test_media_lista_positivosenegativos_cenario1(self):
        # em que a soma dos módulos dos números negativos da lista é maior que a soma dos números positivos
        resultado = calcular_media([1,2,3,-3,-6,-9])
        self.assertEqual(resultado,-2)

    def test_media_lista_positivosenegativos_cenario2(self):
        # em que a soma dos módulos dos números negativos da lista é menor que a soma dos números positivos
        resultado = calcular_media([-1,-2,-3,3,6,9])
        self.assertEqual(resultado,2)

    def test_media_lista_str(self):
        with self.assertRaises(TypeError):
            calcular_media(['hello', 'world'])

    def test_media_bool(self):
        with self.assertRaises(TypeError):
            calcular_media(True, False)

    def test_media_lista_elemento(self):
        resultado = calcular_media([1])
        self.assertEqual(resultado,1)

if __name__ == '__main__':
    unittest.main()
