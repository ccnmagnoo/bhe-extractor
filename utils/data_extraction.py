from datetime import datetime
from typing import Callable, Literal

# utils

def extract_factory[T:type](ty:T,normalizer:Callable[[str],T]|None = None)->Callable[[list[str]],T]:
    """return function to data extract and transform
    only for  float, int, str
    """
    if normalizer is not None:
        extract_fun: T = lambda it: ty(normalizer(it[0])) if len(it)>0 else None
        return extract_fun

    extract_fun: T = lambda it: ty(it[0]) if len(it)>0 else None

    return extract_fun

def raw_to_datetime(period:list[tuple[str,str]])->tuple[datetime,datetime]:
    """take input str tuple with dates (actual,before) and turn it into datetime class"""
    raw = period[0]
    res = tuple(map(compose_date,raw))
    res = tuple(map(lambda dt:datetime.strptime(dt,'%d %m %Y'),res
            )
        )

    return res

type Month = Literal['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
MONTH:dict[Month,str] = {'ene':'01','feb':'02','mar':'03','abr':'04','may':'05','jun':'06','jul':'07','ago':'08','sep':'09','oct':'10','nov':'011','dic':'12'}

def es_month_to_num(short:Month):
    "given 3 chars month return correlative month number 01-12"
    return MONTH[short]

def compose_date(d:str)->str:
    """given dd MMM YYYY date return dd mm YYYY"""
    d_list = d.split(' ')
    d_list[1] = es_month_to_num(d_list[1])
    return ' '.join(d_list)