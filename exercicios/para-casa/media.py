#Teste - Média Aritmética

def media_2 (x, y):

    """media x e y

    >>> media_2(10, 6.5)
    8.25

    >>> media_2('15', 15)
    Traceback (most recent call last):
    ...
    AssertionError:  "x" precisa ser int ou float
    """
    
    assert isinstance (x, (int, float)), ' "x" precisa ser int ou float'
    assert isinstance (y, (int, float)), ' "y" precisa ser int ou float'
    return (x + y)/2


# teste usando doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
