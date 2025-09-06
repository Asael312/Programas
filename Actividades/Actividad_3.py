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
    consumo = round((dispositivo[1] * dispositivo[2]) / 1000, 2)
    if len(dispositivo) < 3:
        dispositivo[3] = consumo
    else:
        dispositivo.append(consumo)
    if len(dispositivo) < 4:
        dispositivo[4] = round(consumo * costo_por_kwh, 2)
    else:
        dispositivo.append(round(consumo * costo_por_kwh, 2))
    # El costo mensual se calcula aparte, no se almacena aquí

def Consumo_mensual_total(lista_dispositivos, costo_por_kwh):
    consumo_total_dia = sum(dispositivo[3] for dispositivo in lista_dispositivos)
    consumo_total_mes = round(consumo_total_dia * 30, 2)
    costo_total_mes = round(consumo_total_mes * costo_por_kwh, 2)
    print('\nConsumo mensual total: ', consumo_total_mes, 'kWh')
    print('Costo mensual total: $', costo_total_mes)
    return consumo_total_mes, costo_total_mes

def BuscarDispositivo(lista_dispositivos):
    nombre = input('Ingrese el nombre del dispositivo a buscar: ')
    for dispositivo in lista_dispositivos:
        if dispositivo[0] == nombre:
            print('Dispositivo encontrado:')
            print('Nombre: ', dispositivo[0])
            print('Consumo: ', round(dispositivo[1],2), 'W')
            print('Horas de uso por día: ', Horas_y_minutos(dispositivo[2]))
            print('Consumo diario: ', round(dispositivo[3],2), 'kWh')
            print('-'*40)
            return
    print("Nombre no encontrado")
def Horas_y_minutos(horas):
    h = int(horas)
    m = int((horas - h) * 60)
    return f"{h} horas y {m} minutos"

def MostrarDispositivos(lista_dispositivos):
    print('--- Lista de dispositivos ---')
    print('{:<15} {:>12} {:>18} {:>16}'.format('Nombre', 'Consumo(W)', 'Horas/día', 'Consumo(kWh)'))
    for dispositivo in lista_dispositivos:
        print('{:<15} {:>12.2f} {:>18} {:>16.2f}'.format(
            dispositivo[0], dispositivo[1], Horas_y_minutos(dispositivo[2]), dispositivo[3]
        ))
    print('-'*65)

Dispositivos = []
opcion = ' '
costo_por_kwh = Insertar_dipositivo(Dispositivos)
MostrarDispositivos(Dispositivos)
while opcion != '4':
    Menu()
    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        MostrarDispositivos(Dispositivos)
    elif opcion == '2':
        BuscarDispositivo(Dispositivos)
    elif opcion == '3':
        MostrarDispositivos(Dispositivos)
        consumo_mensual, costo_mensual = Consumo_mensual_total(Dispositivos, costo_por_kwh)
    elif opcion == '4':
        print('---Resumen final---')
        print('Consumo mensual total: ', consumo_mensual, 'kWh')
        print('Costo mensual total: $', costo_mensual)
        print('Saliendo del programa...')
    