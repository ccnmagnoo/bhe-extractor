from dataclasses import dataclass, field
from datetime import datetime
from re import Pattern, compile
from typing import Callable

#cspell: disable
type PatternModel = dict[str,Pattern]

#data loader transform
# function who recieve an input type, and a tranfromer function
type Transformer[IN,OUT] = Callable[[IN,Callable[[IN],OUT]],OUT]

@dataclass
class Invoice:
    """invoice with electric bill"""
    client:str
    measurer:int
    fare:str
    period:tuple[datetime,datetime]
    lecture_act:int
    lecture_ant:int
    reactive_act:int
    reactive_ant:int
    power_demand:float
    electricity_consumption:float
    electricity_cost:int
    power_max_cost:int
    admin_cost:int
    transport_cost:int
    total_bill:int

@dataclass
class InvoiceAdapter[T,P = T]:
    """Regex Pattern requirements to match certain Invoice param
    - **T**: all params type
    - **P**: period lecture type, default = *T*
    """
    client:T
    measurer:T
    fare:T
    period:P
    lecture_act:T
    lecture_ant:T
    reactive_act:T
    reactive_ant:T
    power_demand:T
    electricity_consumption:T
    electricity_cost:T
    power_max:T
    power_max_cost:T
    admin_cost:T
    transport_cost:T
    total_bill:T
# final

