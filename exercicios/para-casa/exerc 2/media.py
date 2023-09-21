#Teste - Média Aritmética

def media (x, y):

    """media x e y

    >>> media(10, 15)
    12.5

    >>> media('10', 15)
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
