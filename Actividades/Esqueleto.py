def Menu():
    print('\n--- MENÚ INVENTARIO ---')
    print('1. Mostrar inventario')
    print('2. Agregar producto')
    print('3. Actualizar producto')
    print('4. Eliminar producto')
    print('5. Buscar producto')
    print('6. Presupuesto total')
    print('7. Venta')
    print('8. Salir')
    try:
        Opcion = int(input("Seleccione una opción: "))
        return Opcion
    except ValueError: 
        print("Opción inválida.")
        return 
def layout(nombre, datos):
    print(f"Producto: {nombre:<15} Código: {datos['codigo']:<10} Stock: {datos['Stock']:<5} Precio: {datos['precio']:<8}")

def AgregarProducto(diccionario):
    nombre = input('Ingrese el nombre del producto: ')
    if nombre in diccionario: 
        print('El producto ya existe.')
        return
    codigo = input('Ingrese le código: ')
    for datos in diccionario.values():
        if datos['codigo'] == codigo:
            print('Ya existe un producto con ese código.')
            return
    try:
        stock = int(input('Ingrese stock: '))
        precio = float(input('Ingrese precio unitario: '))
        diccionario[nombre] = {'codigo': codigo, 'Stock': stock, 'precio': precio}
        print('Producto agregado.')
    except ValueError: 
        print('Stock y precio deben ser numéricos.')

def MostrarInventario(diccionario):
    if not diccionario:
        print('Inventario vacío.')
        Opcion = input('¿Desea agregar un producto? (si/no): ')
        if Opcion == 'si':
            AgregarProducto(diccionario)
    else:
        print('\n--- Inventario ---')
        for nombre, datos in diccionario.items(): 
            layout(nombre, datos)

def ActualizarProducto(diccionario, dato=None, nuevo_stock=None):
    if dato is None:
        dato = input("Ingrese producto a actualizar: ")
    if BuscarProducto(diccionario,dato):
        try:
            if nuevo_stock is None:
                nuevo_stock = int(input("Ingrese nuevo stock: "))
            diccionario[dato]['Stock'] = nuevo_stock
            print('Producto actualizado.')
            return True
        except ValueError: 
            print('El stock debe ser numérico.')
            return False
    else:
        print('No encontrado.')
        input("¿Deseas agregarlo como nuevo? (si/no): ") 
        if Opcion.lower() == 'si':
            AgregarProducto(diccionario)
        return False

def EliminarProducto(diccionario):
    dato = input("Ingrese producto a eliminar: ")
    nuevo_dato=None
    for nombre,datos in diccionario:
        if dato==nombre or dato==datos['codigo']: 
            nuevo_dato=nombre
            diccionario.pop(nuevo_dato)
            print('"Producto eliminado."')
    else: 
        print('Producto no encontrado.')

def BuscarProducto(diccionario,dato=None):
    if dato is None:
        dato = input('Ingrese producto o código a buscar: ')
    encontrado = False
    for nombre, datos in diccionario.items():
        if nombre == dato or datos['codigo'] == dato:
            print('Encontrado:')
            layout(nombre, datos)
            encontrado = True
    if not encontrado:
        print('No encontrado.')
        opcion = input('¿Deseas agregarlo? (si/no): ')
        if opcion.lower().strip() == 'si':
            AgregarProducto(diccionario)
    return encontrado

def Preciototal(diccionario):
    return sum(diccionario[p]['Stock'] * diccionario[p]['precio'] for p in diccionario)

def venta(diccionario):
    carrito = {}
    total = 0
    while True:
        dato = input("Ingrese producto o código a vender (o salir para terminar): ")
        if dato.lower().strip() == 'salir':
            break
        nombre_encontrado = None
        for nombre, datos in diccionario.items():
            if nombre == dato or datos['codigo'] == dato:
                nombre_encontrado = nombre
                break
        if not nombre_encontrado:
            print(f'{nombre_encontrado} no existe en el inventario.')
            continue
        try:
            cantidad = int(input(f"Ingrese cantidad de '{nombre_encontrado}': "))
        except ValueError:
            print('Debe ser un número.')
            continue
        if cantidad <= 0:
            print("Cantidad inválida.")
            continue
        stock_actual = diccionario[nombre_encontrado]['Stock']
        if cantidad > stock_actual:
            print(f"Stock insuficiente (disponible: {stock_actual}).")
            continue
        nuevo_stock = stock_actual - cantidad
        if ActualizarProducto(diccionario, nombre_encontrado, nuevo_stock):
            subtotal = cantidad * diccionario[nombre_encontrado]['precio']
            carrito[nombre_encontrado] = {'cantidad': cantidad, 'subtotal': subtotal}
            total += subtotal
            print(f"{cantidad} {nombre_encontrado} añadido al carrito.")
    if carrito:
        print("\n--- RESUMEN DE VENTA ---")
        for prod, datos in carrito.items():
            print(f"{prod}: {datos['cantidad']} unidades → ${datos['subtotal']:.2f}")
        print(f"Total de la venta: ${total:.2f}")
        print("\n--- INVENTARIO ACTUALIZADO ---")
        MostrarInventario(diccionario)
        carrito.clear()
        print('Venta finalizada.')
    else:
        print('No se vendió nada.')

Contraseña=''
intentos=0
Precio_total=0
Productos ={}
Opcion=0
while intentos < 3 and Contraseña != 'OXXO':
    Contraseña=input("Ingrese la contraseña: ")
    if Contraseña=='OXXO':
        while Opcion !=8:
            Opcion=Menu()
            if Opcion == 1:
                MostrarInventario(Productos)
            elif Opcion == 2:
                AgregarProducto(Productos)
            elif Opcion == 3:
                ActualizarProducto(Productos)
            elif Opcion == 4:
                EliminarProducto(Productos)
            elif Opcion == 5:
                BuscarProducto(Productos)
            elif Opcion == 6:
                Precio_total(Productos)
            elif Opcion == 7:
                venta(Productos)
            elif Opcion == 8:
                print('Saliendo...')
                print(Productos)
    else:
        print("Contraseña incorrecta. No se pueden agregar o eliminar productos.")
        intentos += 1
