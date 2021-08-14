from typing import Union
from linlib.vec import Vec

def lin_comb(vlist: list[Vec], clist: list[Union[float,int]]) -> Union[int,float]:
    assert len(vlist) == len(clist)
    return sum([coeff*v for (coeff,v) in zip(clist,vlist)])
