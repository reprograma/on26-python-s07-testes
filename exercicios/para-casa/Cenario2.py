#Cenário 2 - Cálculo de juros 
# total_dinheiro = 100
# taxa = 0.2
def calculo_juros(total_dinheiro, taxa):
    if not float(total_dinheiro):
        return 0
    
    return round(float(total_dinheiro) * float(taxa)) 