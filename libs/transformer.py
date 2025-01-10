
from typing import Callable
from models.DataPattern import InvoiceAdapter
from utils.data_extraction import extract_factory,raw_to_datetime

chilquinta = InvoiceAdapter[Callable,Callable](
    client = extract_factory(str),
    measurer = extract_factory(int),
    fare = extract_factory(str),
    period=raw_to_datetime,
    lecture_act=extract_factory(int),
    lecture_ant=extract_factory(int),
    reactive_act=extract_factory(int),
    reactive_ant=extract_factory(int),
    power_demand=extract_factory(float,lambda it:it.replace(',','.')),
    electricity_consumption=extract_factory(int,lambda it:it.replace('.','')),
    electricity_cost=extract_factory(float,lambda it:it.replace('.','')),
    demand_max=extract_factory(float,lambda it:it.replace(',','.')),
    demand_max_cost=extract_factory(float,lambda it:it.replace('.','')),
    admin_cost=extract_factory(float,lambda it:it.replace('.','')),
    transport_cost=extract_factory(float,lambda it:it.replace('.','')),
    total_bill=extract_factory(float,lambda it:it.replace('.','')),
)
chilquinta2 = InvoiceAdapter[Callable,Callable](
    client = extract_factory(str),
    measurer = extract_factory(int),
    fare = extract_factory(str),
    period=raw_to_datetime,
    lecture_act=extract_factory(int),
    lecture_ant=extract_factory(int),
    reactive_act=extract_factory(int),
    reactive_ant=extract_factory(int),
    power_demand=extract_factory(float,lambda it:it.replace(',','.')),
    electricity_consumption=extract_factory(int,lambda it:it.replace('.','')),
    electricity_cost=extract_factory(int,lambda it:it.replace('.','')),
    demand_max=extract_factory(float,lambda it:it.replace(',','.')),
    demand_max_cost=extract_factory(int,lambda it:it.replace('.','')),
    admin_cost=extract_factory(int,lambda it:it.replace('.','')),
    transport_cost=extract_factory(int,lambda it:it.replace('.','')),
    total_bill=extract_factory(float,lambda it:it.replace('.','')),
)

litoral = InvoiceAdapter[Callable,Callable](
    client = extract_factory(str),
    measurer = extract_factory(int),
    fare = extract_factory(str),
    period=raw_to_datetime,
    lecture_act=extract_factory(int),
    lecture_ant=extract_factory(int),
    reactive_act=extract_factory(int),
    reactive_ant=extract_factory(int),
    power_demand=extract_factory(float,lambda it:it.replace(',','.')),
    electricity_consumption=extract_factory(int,lambda it:it.replace('.','')),
    electricity_cost=extract_factory(float,lambda it:it.replace('.','')),
    demand_max=extract_factory(float,lambda it:it.replace(',','.')),
    demand_max_cost=extract_factory(float,lambda it:it.replace('.','')),
    admin_cost=extract_factory(float,lambda it:it.replace('.','')),
    transport_cost=extract_factory(float,lambda it:it.replace('.','')),
    total_bill=extract_factory(float,lambda it:it.replace('.','')),
)
#