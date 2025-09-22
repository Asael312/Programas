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
        return None


# ===== Manejo de archivos =====
def cargar_inventario(nombre_archivo):
    inventario = {}
    try:
        with open(f"{nombre_archivo}.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    nombre, codigo, stock, precio = datos
                    inventario[nombre] = {
                        "codigo": codigo,
                        "Stock": int(stock),
                        "precio": float(precio)
                    }
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo.")
        open(f"{nombre_archivo}.txt", "w").close()
    return inventario

def guardar_inventario(nombre_archivo, inventario):
    with open(f"{nombre_archivo}.txt", "w") as f:
        for nombre, datos in inventario.items():
            f.write(f"{nombre},{datos['codigo']},{datos['Stock']},{datos['precio']}\n")


# ===== Utilidades =====
def layout(nombre, datos):
    print(f"Producto: {nombre:<15} Código: {datos['codigo']:<10} Stock: {datos['Stock']:<5} Precio: ${datos['precio']:<8.2f}")


# ===== Operaciones =====
def AgregarProducto(diccionario, archivo):
    nombre = input('Ingrese el nombre del producto: ')
    if nombre in diccionario: 
        print('El producto ya existe.')
        return
    codigo = input('Ingrese el código: ')
    for datos in diccionario.values():
        if datos['codigo'] == codigo:
            print('Ya existe un producto con ese código.')
            return
    try:
        stock = int(input('Ingrese stock: '))
        precio = float(input('Ingrese precio unitario: '))
        diccionario[nombre] = {'codigo': codigo, 'Stock': stock, 'precio': precio}
        print('Producto agregado.')
        guardar_inventario(archivo, diccionario)
    except ValueError: 
        print('Stock y precio deben ser numéricos.')

def MostrarInventario(diccionario):
    if not diccionario:
        print('Inventario vacío.')
    else:
        print('\n--- Inventario ---')
        for nombre, datos in diccionario.items(): 
            layout(nombre, datos)

def ActualizarProducto(diccionario, archivo, dato=None, nuevo_stock=None):
    if dato is None:
        dato = input("Ingrese producto a actualizar: ")
    if BuscarProducto(diccionario, dato):
        try:
            if nuevo_stock is None:
                nuevo_stock = int(input("Ingrese nuevo stock: "))
            diccionario[dato]['Stock'] = nuevo_stock
            print('Producto actualizado.')
            guardar_inventario(archivo, diccionario)
            return True
        except ValueError: 
            print('El stock debe ser numérico.')
            return False
    else:
        print('No encontrado.')
        return False

def EliminarProducto(diccionario, archivo):
    dato = input("Ingrese producto a eliminar: ")
    if dato in diccionario:
        diccionario.pop(dato)
        print('Producto eliminado.')
        guardar_inventario(archivo, diccionario)
    else:
        print('Producto no encontrado.')

def BuscarProducto(diccionario, dato=None):
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
    return encontrado

def Preciototal(diccionario):
    total = sum(diccionario[p]['Stock'] * diccionario[p]['precio'] for p in diccionario)
    print(f"El presupuesto total es: ${total:.2f}")
    return total

def venta(diccionario, archivo):
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
            print("Ese producto no existe en el inventario.")
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
        if ActualizarProducto(diccionario, archivo, nombre_encontrado, nuevo_stock):
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
        guardar_inventario(archivo, diccionario)
        carrito.clear()
        print('Venta finalizada.')
    else:
        print('No se vendió nada.')


# ===== Programa principal =====
Contraseña=''
intentos=0
Opcion=0

nomrbre_archivo = input('¿Qué nombre tiene el archivo?: ').strip()
Productos = cargar_inventario(nomrbre_archivo)

while intentos < 3 and Contraseña != 'OXO':
    Contraseña=input("Ingrese la contraseña: ")
    if Contraseña=='OXO':
        while Opcion != 8:
            Opcion=Menu()
            if Opcion == 1:
                MostrarInventario(Productos)
            elif Opcion == 2:
                AgregarProducto(Productos, nomrbre_archivo)
            elif Opcion == 3:
                ActualizarProducto(Productos, nomrbre_archivo)
            elif Opcion == 4:
                EliminarProducto(Productos, nomrbre_archivo)
            elif Opcion == 5:
                BuscarProducto(Productos)
            elif Opcion == 6:
                Preciototal(Productos)
            elif Opcion == 7:
                venta(Productos, nomrbre_archivo)
            elif Opcion == 8:
                print('Saliendo...')
                guardar_inventario(nomrbre_archivo, Productos)
    else:
        print("Contraseña incorrecta.")
        intentos += 1
