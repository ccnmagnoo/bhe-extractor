from re import Pattern, compile

#cspell: disable
type PatternModel = dict[str,Pattern[str]]

chilquinta = {
    'cliente':compile(r'^\s*(\d{5,6}-?\d?)$'),
    'medidor': compile(r'^\s*(\d{7,8})\s*EmpresaActual\s*(\d+)\s*Kwh'),
    'lectura_actual': compile(r'Actual\s*(\d+)\s*Kwh'),
    'lectura_anterior': compile(r'^Anterior\s*-\s*(\d+)\s*Kwh'),
}