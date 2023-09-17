import math, unittest


def soma (a,b):
    soma = a + b
    if a or b == float:
        return round(soma, 1)
    else:
        return soma
    
def subt (a,b):
    subt = a - b
    if a or b == float:
        return round(subt, 1)
    else:
        return subt

def multi(a,b):
    multi = a * b
    if a or b == float:
        return round(multi, 2)
    else:
        return multi
    
def div(a,b):
    if b != 0:
        div = a / b
        return round(div, 2)
    
    if a == 0:
        div == 0
   

class TesteSoma(unittest.TestCase):
    def teste_soma_positivo(self):
        self.assertEqual(soma(5,15), 20)

    def teste_soma_negativo(self):
        self.assertEqual(soma(-50, -3), -53)

    def teste_soma_positivo_float(self):
        self.assertEqual(soma(3.5,5.3), 8.8)

    def teste_soma_negativo_float(self):
        self.assertEqual(soma(-3.5, -6.2), -9.7)

    def teste_soma_zero(self):
        self.assertEqual(soma(0,0), 0)
        
class TesteSubtracao(unittest.TestCase):
    def teste_subt_positivo(self):
        self.assertEqual(subt(8,2), 6)

    def teste_subt_negativo(self):
        self.assertEqual(subt(8,-4), 12)

    def teste_subt_positivo_float(self):
        self.assertEqual(subt(3.4, 7.2), -3.8)

    def teste_subt_negativo_float(self):
        self.assertEqual(subt(5.8, -9.8), 15.6)

    def teste_subt_zero(self):
        self.assertEqual(subt(0,0), 0)

class TesteMulti(unittest.TestCase):
    def teste_multi_positivos(self):
        self.assertEqual(multi(3,5), 15)
    
    def teste_multi_negativos(self):
        self.assertEqual(multi(4, -6), -24)

    def teste_multi_positivos_float(self):
        self.assertEqual(multi(3.6, 9.8), 35.28)

    def teste_multi_negativos_float(self):
        self.assertEqual(multi(-4.7, 3.9), -18.33)

    def teste_multi_zero(self):
        self.assertEqual(multi(0,0), 0)

class TesteDivi(unittest.TestCase):
    def teste_divi_positiva(self):
        self.assertEqual(div(10,5), 2)
    
    def teste_div_negativa(self):
        self.assertEqual(div(-32,4), -8)
    
    def teste_div_positiva_float(self):
        self.assertAlmostEqual(div(55,3), 18.33)

    def teste_div_negativa_float(self):
        self.assertEqual(div(-43, 7), -6.14)

    def teste_div_zero1(self):
        self.assertEqual(div(2,0), None)

    def teste_div_zero2(self):
        self.assertEqual(div(0,9), 0)


if __name__ == "__main__":
    unittest.main()
#nativo da bibilioteca ele precisa ser escrito para que seja chamado