from typing import Literal

from models.DataPattern import InvoiceAdapter
from libs.pattern import chilquinta as chil1_p, litoral as lit_p, chilquinta2 as chil2_p
from libs.transformer import chilquinta as chil1_t,chilquinta2 as chil2_t, litoral as lit_t



type Provider = Literal['Chilquinta_1','Chilquinta_2','CGE','Litoral','Energía Casablanca']
type Tools = Literal['transformer','pattern']

CONTEXT:dict[Provider,dict[Tools,InvoiceAdapter]] = {
    'Chilquinta_1':{'pattern':chil1_p, 'transformer':chil1_t},
    'Chilquinta_2':{'pattern':chil2_p, 'transformer':chil2_t},
    'Litoral':{'pattern':lit_p,'transformer':lit_t}
}