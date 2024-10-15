from re import Pattern, compile

type PatternModel = dict[str,Pattern[str]]

chilquinta = {
    'medidor': compile('{\d{7,8}}EmpresaActual')
}