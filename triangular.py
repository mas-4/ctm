from vec import Vec
from vecutil import zero_vec

def triangular_solve_n(rowlist: list[Vec], b: list[int]) -> Vec:
    D: set = rowlist[0].D
    n: int = len(D)
    assert D == set(range(n)), "There are gaps in D"
    x: Vec = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - (rowlist[i] * x)) / rowlist[i][i] # type: ignore
    return x

def triangular_solve(rowlist: list[Vec], label_list: list, b: list[int]) -> Vec:
    """
    >>> label_list = ['a','b','c','d']
    >>> D = set(label_list)
    >>> rowlist=[Vec(D, {'a':4, 'b':-2, 'c':0.5, 'd':1}), Vec(D,{'b':2, 'c':3, 'd':3}), Vec(D,{'c':5, 'd':1}), Vec(D,{'d':2.})]
    >>> b = [6, -4, 3, -8]
    >>> triangular_solve(rowlist, label_list, b)
    Vec({'d','a','b','c'},{'d': -4.0, 'b': 1.9, 'c': 1.4, 'a': 3.275})
    """
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(D))):
        c = label_list[j]
        row = rowlist[j]
        x[c] = round((b[j] - x*row)/row[c],5) # type: ignore
    return x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
