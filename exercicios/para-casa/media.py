#Teste - Média Aritmética

def media_2 (x, y):
    assert isinstance (x, (int, float)), ' "x" precisa ser int ou float'
    assert isinstance (y, (int, float)), ' "y" precisa ser int ou float'
    return (x + y)/2
