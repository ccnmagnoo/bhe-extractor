from dataclasses import dataclass
from re import Pattern, compile

#cspell: disable
type PatternModel = dict[str,Pattern]

@dataclass
class InvoicePattern:
    """Regex Pattern requirements to match certain Invoice param"""
    client:Pattern
    measurer:Pattern
    fare:Pattern
    period:Pattern
    lecture_act:Pattern
    lecture_ant:Pattern
    reactive_act:Pattern
    reactive_ant:Pattern
    power_demand:Pattern
    electricity_consumption:Pattern
    electricity_cost:Pattern
    power_max:Pattern
    power_max_cost:Pattern
    admin_cost:Pattern
    transport_cost:Pattern
    total_bill:Pattern

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
    total_bill=compile(r'\d{5,6}-\d\W*\$\s*(d\*.?d\*)'),
)