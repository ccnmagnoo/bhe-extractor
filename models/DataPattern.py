from dataclasses import dataclass
from re import Pattern, compile

#cspell: disable
type PatternModel = dict[str,Pattern[str]]

@dataclass
class InvoicePattern:
    cliente:Pattern[str]
    medidor:Pattern[str]
    lectura_act:Pattern[str]
    lectura_ant:Pattern[str]
    reactiva_act:Pattern[str]
    reactiva_ant:Pattern[str]

chilquinta = InvoicePattern(
    cliente=compile(r'(\d{5,6}-\d)'),
    medidor= compile(r'(\d{7,8})EmpresaActual'),
    lectura_act= compile(r'EmpresaActual\s*(\d+)\s*kWh'),
    lectura_ant= compile(r'Anterior\s*-\s*(\d+)\s*kWh'),
    reactiva_act=compile(r'EmpresaActual\s*(\d+)\s*Kvarh'),
    reactiva_ant= compile(r'Anterior\s*-\s*(\d+)\s*Kvarh'),
)