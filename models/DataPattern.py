from dataclasses import dataclass
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
    period:tuple[datetime,datetime] = []
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
class InvoiceAdapter[TY,PERIOD]:
    """Regex Pattern requirements to match certain Invoice param"""
    client:TY
    measurer:TY
    fare:TY
    period:PERIOD
    lecture_act:TY
    lecture_ant:TY
    reactive_act:TY
    reactive_ant:TY
    power_demand:TY
    electricity_consumption:TY
    electricity_cost:TY
    power_max:TY
    power_max_cost:TY
    admin_cost:TY
    transport_cost:TY
    total_bill:TY
# final

