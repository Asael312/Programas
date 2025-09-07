def Menu():
    print('Menu de opciones:')
    print('1. Mostrar Dispositivos')
    print('2. Buscar Dispositivo')
    print('3. Consumo y costo mensual total')
    print('4. Salir')

def Insertar_dipositivo(lista_dispositivos):
    num_dispositivos = int(input('Ingrese el numero de dispositivos a registrar: '))
    for i in range(num_dispositivos):
        nombre = input('Ingrese el nombre del dispositivo: ')
        consumo = float(input('Ingrese el consumo en watts: '))
        horas_uso = float(input('Ingrese las horas de uso por dia: '))
        dispositivo = [nombre, consumo, horas_uso]
        lista_dispositivos.append(dispositivo)
    costo_por_kwh = float(input('Ingrese el costo por kWh: '))
    for dispositivo in lista_dispositivos:
        CalcularConsumo(dispositivo, costo_por_kwh)
    return costo_por_kwh

def CalcularConsumo(dispositivo, costo_por_kwh):
    kWh_dia = round((dispositivo[1] * dispositivo[2]) / 1000, 2)
    kWh_mes = round(kWh_dia * 30, 2)
    costo_mes = round(kWh_mes * costo_por_kwh, 2)
    return kWh_dia, kWh_mes, costo_mes

def Consumo_mensual_total(lista_dispositivos, costo_por_kwh):
    consumo_total_mes = sum(CalcularConsumo(d, costo_por_kwh)[1] for d in lista_dispositivos)
    costo_total_mes = sum(CalcularConsumo(d, costo_por_kwh)[2] for d in lista_dispositivos)
    print('\nConsumo mensual total: ', consumo_total_mes, 'kWh')
    print('Costo mensual total: $', costo_total_mes)
    return consumo_total_mes, costo_total_mes

def BuscarDispositivo(lista_dispositivos, costo_por_kwh):
    nombre = input('Ingrese el nombre del dispositivo a buscar: ')
    for dispositivo in lista_dispositivos:
        if dispositivo[0] == nombre:
            print('Dispositivo encontrado:')
            print('Nombre: ', dispositivo[0])
            print('W: ', round(dispositivo[1],2))
            print('Horas de uso por día: ', Horas_y_minutos(dispositivo[2]))
            kWh_dia, kWh_mes, costo_mes = CalcularConsumo(dispositivo, costo_por_kwh)
            print('Consumo diario: ', round(kWh_dia,2), 'kWh')
            print('Consumo mensual: ', round(kWh_mes,2), 'kWh')
            print('Costo mensual: $', round(costo_mes,2))
            print('-'*40)
            return
    print("Nombre no encontrado")
def Horas_y_minutos(horas):
    h = int(horas)
    m = int((horas - h) * 60)
    return str(h) + "h" + str(m) + "min"

def MostrarDispositivos(lista_dispositivos, costo_por_kwh):
    print('--- Lista de dispositivos ---')
    print('Nombre', 'W', 'h/día', 'kWh/día','kWh/mes','$/mes' ,sep=' '*8)
    for dispositivo in lista_dispositivos:
        kWh_dia, kWh_mes, costo_mes = CalcularConsumo(dispositivo, costo_por_kwh)
        print(dispositivo[0], dispositivo[1], Horas_y_minutos(dispositivo[2]),'  ', str(kWh_dia),'  ', str(kWh_mes), '  ', str(costo_mes), sep=' '*5)
    print('-'*65)

Dispositivos = []
opcion = ' '
costo_por_kwh = Insertar_dipositivo(Dispositivos)
MostrarDispositivos(Dispositivos, costo_por_kwh)
while opcion != '4':
    Menu()
    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        MostrarDispositivos(Dispositivos, costo_por_kwh)
    elif opcion == '2':
        BuscarDispositivo(Dispositivos, costo_por_kwh)
    elif opcion == '3':
        MostrarDispositivos(Dispositivos, costo_por_kwh)
        consumo_mensual, costo_mensual = Consumo_mensual_total(Dispositivos, costo_por_kwh)
    elif opcion == '4':
        print('---Resumen final---')
        print('Consumo mensual total: ', consumo_mensual, 'kWh')
        print('Costo mensual total: $', costo_mensual)
        print('Saliendo del programa...')
