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
    power_max:float
    power_max_cost:int
    admin_cost:int
    transport_cost:int
    total_bill:int

@dataclass
class InvoiceAdapter[T]:
    """Regex Pattern requirements to match certain Invoice param"""
    client:T
    measurer:T
    fare:T
    period:T
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

type InvoicePattern = InvoiceAdapter[Pattern[str]]

type InvoiceTransformer = InvoiceAdapter[Callable]

chilquinta = InvoicePattern(
    client=compile(r'(\d{5,6}-\d)'),
    measurer= compile(r'(\d{7,8})EmpresaActual'),
    fare= compile(r'tarifa contratada: ([\w*-]*\s?\w*)'),
    period=compile(r'Monto del per[i,í]odo: (\d{2} \w{3} \d{4}) - (\d{2} \w{3} \d{4})'),
    lecture_act= compile(r'EmpresaActual\s*(\d+)\s*kWh'),
    lecture_ant= compile(r'Anterior\s*-\s*(\d+)\s*kWh'),
    reactive_act=compile(r'EmpresaActual\s*(\d+)\s*Kvarh'),
    reactive_ant= compile(r'Anterior\s*-\s*(\d+)\s*Kvarh'),
    power_demand=compile(r'Demanda Leida :\s+(\d*\W?\d)* kW'),
    electricity_consumption=compile(r'Electricidad consumida (\d+) kWh'),
    electricity_cost=compile(r'Electricidad consumida \d+ kWh \$ (\d*.?\d+)'),
    power_max=compile(r'demanda máxima\s+(\d*\W?\d)* kW'),
    power_max_cost=compile(r'demanda máxima\s+\d*\W?\d* kW \$ (\d*.?\d+)'),
    admin_cost=compile(r'servicio \$ (\d*.?\d+)'),
    transport_cost=compile(r'transporte de electricidad \$ (\d*.?\d+)'),
    total_bill=compile(r'\d{5,6}-\d \d{2} \w{3} \d{4}\r\n\s*\$ (\d*.?\d+)'),
)

chilquinta_t = InvoiceAdapter[Callable](
    client = lambda input: input[0],
    measurer = lambda input:int(input[0]),
    fare = lambda input: input[0],
    
    
)
# final

