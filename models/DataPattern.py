from dataclasses import dataclass, field
from datetime import datetime
from typing import Callable
from re import Pattern, compile

#cspell: disable
type PatternModel = dict[str,Pattern]

#data loader transform
# function who recieve an input type, and a tranfromer function
type Transformer[IN,OUT] = Callable[[IN,Callable[[IN],OUT]],OUT]

@dataclass
class Invoice:
    """invoice with electric bill"""
    client:str = ''
    measurer:int = 0
    fare:str = ''
    period:tuple[datetime,datetime] = ()
    lecture_act:int = 0
    lecture_ant:int = 0
    reactive_act:int = 0
    reactive_ant:int = 0
    power_demand:float = 0.0
    electricity_consumption:float = 0.0
    electricity_cost:int = 0
    power_max:float = 0.0
    power_max_cost:int = 0
    admin_cost:int = 0
    transport_cost:int = 0
    total_bill:int = 0

@dataclass
class InvoiceAdapter[T,P = T]:
    """Regex Pattern requirements to match certain Invoice param
    - **T**: all params type
    - **P**: period lecture type, default = *T*
    """
    client:T = field(default_factory=T)
    measurer:T = field(default_factory=T)
    fare:T = field(default_factory=T)
    period:P = field(default_factory=P)
    lecture_act:T = field(default_factory=T)
    lecture_ant:T = field(default_factory=T)
    reactive_act:T = field(default_factory=T)
    reactive_ant:T = field(default_factory=T)
    power_demand:T = field(default_factory=T)
    electricity_consumption:T = field(default_factory=T)
    electricity_cost:T = field(default_factory=T)
    power_max:T = field(default_factory=T)
    power_max_cost:T = field(default_factory=T)
    admin_cost:T = field(default_factory=T)
    transport_cost:T = field(default_factory=T)
    total_bill:T = field(default_factory=T)
# final

