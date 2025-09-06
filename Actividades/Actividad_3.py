def Menu():
    print('Menu de opciones:')
    print('1.Mostrar Dispositivos')
    print('2.Buscar Dispositivo')
    print('3.Consumo y costo mensual total')
    print('4. Salir')

def Insertar_dipositivo(lista_dispositivos):
    num_dispositivos = int(input('Ingrese el numero de dispositivos a registrar: '))
    for i in range(num_dispositivos):
        nombre = input('Ingrese el nombre del dispositivo: ')
        consumo = float(input('Ingrese el consumo en watts: '))
        horas_uso = float(input('Ingrese las horas de uso por dia: '))
        dispositivo = [nombre, consumo, horas_uso]
        lista_dispositivos.append(dispositivo)
        CalcularConsumo(dispositivo)
    costo_por_kwh = float(input('Ingrese el costo por kwh: '))
    return costo_por_kwh

def CalcularConsumo(dispositivo):
        consumo = (dispositivo[1] * dispositivo[2] )/1000
        dispositivo.append(consumo)

def Consumo_total(lista_dispositivos, costo_por_kwh):
    consumo_total = sum(dispositivo[3] for dispositivo in lista_dispositivos)
    costo_total = consumo_total * costo_por_kwh * 30
    print('\nConsumo mensual total: ', str(consumo_total) + 'kWh')
    print('Costo mensual total:',' $'+ str(round(costo_total,2)))
def BuscarDispositivo(lista_dispositivos):
    nombre = input('Ingrese el nombre del dispositivo a buscar: ')
    for dispositivo in lista_dispositivos:
        if dispositivo[0] == nombre:
            print('Dispositivo encontrado:')
            CalcularConsumo(dispositivo)
            print('Nombre: ', dispositivo[0], 'Consumo(W): ', dispositivo[1], 'Horas de uso por dia: ', dispositivo[2],'Consumo(kWh): ', dispositivo[3],sep='\n')
            print('-'*80)
            return
    print("Nombre no encontrado")

def MostrarDispositivos(lista_dispositivos):
    print('--- Lista de dispositivos ---')
    print('Nombre       Consumo(W)   Horas de uso por dia    Consumo (kWh)')
    for dispositivo in lista_dispositivos:
        for dato in dispositivo:
            print(dato,'\t'*1, end=' ')
        print()
    print('-'*80)
Dispositivos = []
opcion = ' '
costo_por_kwh = Insertar_dipositivo(Dispositivos)
MostrarDispositivos(Dispositivos)
while opcion != '4':
    Menu()
    opcion= input('Seleccione una opcion: ')

    if opcion == '1':
        MostrarDispositivos(Dispositivos)
    elif opcion == '2':
        BuscarDispositivo(Dispositivos)
    elif opcion == '3':
        MostrarDispositivos(Dispositivos)
        Consumo_total(Dispositivos, costo_por_kwh)
    elif opcion == '4':
        print('Saliendo del programa...')