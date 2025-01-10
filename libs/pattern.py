from re import Pattern, compile
from models.DataPattern import InvoiceAdapter

#cspell: disable

chilquinta = InvoiceAdapter[Pattern,Pattern](
    client=compile(r'(\d{5,6}-\d)'),
    measurer= compile(r'(\d{7,8})EmpresaActual'),
    fare= compile(r'tarifa contratada: ([\w*-]*\s?\w*)'),
    period=compile(r'Monto del per[i,í]odo: (\d{2} \w{3} \d{4}) - (\d{2} \w{3} \d{4})'),
    lecture_act= compile(r'EmpresaActual\s*(\d+)\s*kWh'),
    lecture_ant= compile(r'Anterior\s*-\s*(\d+)\s*kWh'),
    reactive_act=compile(r'EmpresaActual\s*(\d+)\s*Kvarh'),
    reactive_ant= compile(r'Anterior\s*-\s*(\d+)\s*Kvarh'),
    power_demand=compile(r'Demanda Leida :\s+(\d*\W?\d)* kW'),
    electricity_consumption=compile(r'Electricidad consumida (\d*.?\d+) kWh'),
    electricity_cost=compile(r'Electricidad consumida \d*.?\d+ kWh \$ (\d*.?\d+)'),
    demand_max=compile(r'demanda máxima\s+(\d*\W?\d)* kW'),
    demand_max_cost=compile(r'demanda máxima\s+\d*\W?\d* kW \$ (\d*.?\d+)'),
    admin_cost=compile(r'servicio \$ (\d*.?\d+)'),
    transport_cost=compile(r'transporte de electricidad \$ (\d*.?\d+)'),
    total_bill=compile(r'\d{5,6}-\d \d{2} \w{3} \d{4}\r\n\s*\$ (\d*.?\d+)'),
)

chilquinta2= InvoiceAdapter[Pattern,Pattern](
    client=compile(r'CLIENTE: (\d{5,6}\s*-\s*\d)'),#rev
    measurer= compile(r'(\d{7,9})\s+\d+\s*Activo'),#rev
    fare= compile(r'[A,B]T\s*-?\s*\d+.?\d*\s*\w{2,3}?'),#rev
    period=compile(r'(\d{2} \w{3} \d{4})\s+al\s+(\d{2} \w{3} \d{4})'),#rev
    lecture_act= compile(r'\d{7,9}\s+\d+\s*Activo Empresa (\d+) \d+ \d+'),#rev
    lecture_ant= compile(r'\d{7,9}\s+\d+\s*Activo Empresa \d+ (\d+) \d+'),#rev
    reactive_act=compile(r'\d{7,9}\s+\d+\s*Reactivo Empresa (\d+) \d+ \d+'),#rev
    reactive_ant=compile(r'\d{7,9}\s+\d+\s*Reactivo Empresa \d+ (\d+) \d+'),#rev
    power_demand=compile(r'Demanda Leida :?\s+(\d*\W?\d)* kW'),
    electricity_consumption=compile(r'(\d+)\s+Electricidad consumida kWh \d*.?\d+'),#rev
    electricity_cost=compile(r'\d+\s+Electricidad consumida kWh (\d*.?\d+)'),#rev
    demand_max=compile(r'(\d*,?\d+)\s+Demanda Máxima kW \d*.?\d+'),#rev
    demand_max_cost=compile(r'\d*,?\d+\s+Demanda Máxima kW (\d*.?\d+)'),#rev
    admin_cost=compile(r'servicio\s+(\d*.?\d+)'),#rev
    transport_cost=compile(r'Transmisión (\d*.?\d+)'),#rev
    total_bill=compile(r'\$\s*(\d*.?\d+) \d* \w{3}'),#rev
)

litoral = InvoiceAdapter[Pattern,Pattern](
    client=compile(r'(\d{5,6}-\d)'),
    measurer= compile(r'(\d{7,8})EmpresaActual'),
    fare= compile(r'tarifa contratada: ([\w*-]*\s?\w*)'),
    period=compile(r'Monto del per[i,í]odo: (\d{2} \w{3} \d{4}) - (\d{2} \w{3} \d{4})'),
    lecture_act= compile(r'EmpresaActual\s*(\d+)\s*kWh'),
    lecture_ant= compile(r'Anterior\s*-\s*(\d+)\s*kWh'),
    reactive_act=compile(r'EmpresaActual\s*(\d+)\s*Kvarh'),
    reactive_ant= compile(r'Anterior\s*-\s*(\d+)\s*Kvarh'),
    power_demand=compile(r'Demanda Leida :\s+(\d*\W?\d)* kW'),
    electricity_consumption=compile(r'Electricidad consumida (\d*.?\d+) kWh'),
    electricity_cost=compile(r'Electricidad consumida \d*.?\d+ kWh \$ (\d*.?\d+)'),
    demand_max=compile(r'demanda máxima\s+(\d*\W?\d)* kW'),
    demand_max_cost=compile(r'demanda máxima\s+\d*\W?\d* kW \$ (\d*.?\d+)'),
    admin_cost=compile(r'servicio \$ (\d*.?\d+)'),
    transport_cost=compile(r'transporte de electricidad \$ (\d*.?\d+)'),
    total_bill=compile(r'\$\s*(\d*.?\d+) \d* \w{3}'),
)