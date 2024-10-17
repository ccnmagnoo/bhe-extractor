from dataclasses import dataclass
from re import Pattern, compile

#cspell: disable
type PatternModel = dict[str,Pattern[str]]

@dataclass
class InvoicePattern:
    """Regex Pattern requirements to match certain Invoice param"""
    client:Pattern[str]
    measurer:Pattern[str]
    fare:Pattern[str]
    period:Pattern[str]
    lecture_act:Pattern[str]
    lecture_ant:Pattern[str]
    reactive_act:Pattern[str]
    reactive_ant:Pattern[str]
    power_demand:Pattern[str]
    electricity_consumption:Pattern[str]
    electricity_cost:Pattern[str]
    power_max:Pattern[str]
    power_max_cost:Pattern[str]
    admin_cost:Pattern[str]
    transport_cost:Pattern[str]

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
)