from typing import Literal

from models.DataPattern import InvoiceAdapter
from libs.pattern import chilquinta as chil_p
from libs.transformer import chilquinta as chil_t


type Provider = Literal['Chilquinta','CGE','Litoral','Energía Casablanca']
type Tools = Literal['transformer','pattern']

CONTEXT:dict[Provider,dict[Tools,InvoiceAdapter]] = {
    'Chilquinta':{'pattern':chil_p, 'transformer':chil_t}
}