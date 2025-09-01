# Sistema de registro en gimnasio

# Paso 1: Preguntar cuántos clientes se registrarán
num_clientes = int(input("¿Cuántos clientes se registrarán? "))

# Paso 2: Variables acumuladoras
ingresos_totales = 0
suma_edades = 0
contador_clientes = 0
resumen_clientes = ""
cont_basica = 0
cont_premium = 0
cont_vip = 0
cliente_mas_joven = ""
cliente_mayor = ""
edad_mas_joven = 999999
edad_mayor = -9999999
tarifa = 0
# Paso 3: Ciclo para registrar a cada cliente
for i in range(num_clientes):
    nombre =input('Ingrese el nombre del cliente(escribe salir para cancelar): ')
    if nombre == 'salir':
        break
    edad = int(input('¿Que edad tiene el cliente? (escribe 0 para cancelar): '))
    if edad == 0:
        break  
    membresia = input('¿Que membresia tiene?(basica, premium, vip)[escribe salir para cancelar]: ')
    if membresia == 'salir':
        break
    persona = input('¿Que tipo de persona es?(estudiante, profesor, ninguno)[escribe salir para cancelar]: ')
    if persona == 'salir':
        break
    print('-'*36)
    breakpoint()
# Tarifas de menor de edad
    if edad <= 18 and  membresia == 'basica':
        tarifa = 200
        cont_basica += 1
    elif edad <= 18 and (membresia == 'premium' or membresia == 'vip'):
        print("Membresía no válida para menores de edad.")
        continue
# Tarifas para adultos
    elif 18 < edad <= 40:
        if membresia == 'basica':
            tarifa = 300
            cont_basica+=1
        elif membresia == 'premium':
            tarifa = 500
            cont_premium+=1
        elif membresia == 'vip':
            tarifa = 700
            cont_vip+=1
# Tarifas adultos 2
    elif 41 <= edad <= 59:
        if membresia == 'basica':
            tarifa = 250
            cont_basica+=1
        elif membresia == 'premium':
            tarifa = 450
            cont_premium+=1
        elif membresia == 'vip':
            tarifa = 600
            cont_vip+=1
# Tarifa adulto mayor
    elif edad >= 60:
        if membresia == 'basica':
            tarifa = 250*0.80
            cont_basica+=1
        elif membresia == 'premium':
            tarifa = 450*0.80
            cont_premium+=1
        elif membresia == 'vip':
            tarifa = 600*0.80
            cont_vip+=1
    # Descuentos
    if persona == 'estudiante':
        tarifa *= 0.85  # Aplica 15% de descuento
    elif persona == 'profesor':
        tarifa *= 0.80  # Aplica 20% de descuento
    elif persona == 'ninguno':
        tarifa *= 1  # Sin descuento

    # Acumuladores
    ingresos_totales += tarifa
    suma_edades += edad
    contador_clientes += 1
    # Cliente más joven y de mayor edad
    if edad_mas_joven  or edad < edad_mas_joven:
        edad_mas_joven = edad
        cliente_mas_joven = nombre
    if edad_mayor  or edad > edad_mayor:
        edad_mayor = edad
        cliente_mayor = nombre
    # Resumen
    resumen_clientes += "Nombre: " + nombre + " | Edad: " + str(edad) + " | Membresía: " + membresia + " | Pago: $" + str(tarifa) + "\n"

print('\n' + '='*36)
print("  REPORTE FINAL - GIMNASIO")
print("="*36)
print("Total de clientes registrados: " + str(contador_clientes))
print("Resumen de clientes:")
print(resumen_clientes)
print("-"*36)
print("Total de ingresos: $" + str(round(ingresos_totales, 2)))
if contador_clientes > 0:
    print("Promedio de edad:", round(suma_edades/contador_clientes, 2), "años")
else:
    print("Promedio de edad: N/A")
print("Clientes por membresía - Básica: " + str(cont_basica) + "  Premium: " + str(cont_premium) + "  VIP: " + str(cont_vip))
print("Cliente más joven: " + cliente_mas_joven + " con " + str(edad_mas_joven) + " años")
print("Cliente de mayor edad: " + cliente_mayor + " con " + str(edad_mayor) + " años")
print("="*36)