from re import Pattern, compile

#cspell: disable
type PatternModel = dict[str,Pattern[str]]

chilquinta = {
    'cliente':compile(r'(\d{5,6}-\d)'),
    'medidor': compile(r'(\d{7,8})EmpresaActual'),
    'lectura_actual': compile(r'EmpresaActual\s*(\d+)\s*kWh'),
    'lectura_anterior': compile(r'Anterior\s*-\s*(\d+)\s*kWh'),
    'reactiva_actual':compile(r'EmpresaActual\s*(\d+)\s*Kvarh'),
    'reactiva_anterior': compile(r'Anterior\s*-\s*(\d+)\s*Kvarh'),
    }