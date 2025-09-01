Contraseña = ''
intentos = 0
Precio_total = 0
Resumen_de_productos = []

while intentos < 3 and Contraseña != 'OXXO':
    Contraseña = input("Ingrese la contraseña: ")
    if Contraseña == 'OXXO':
        Producto_totales = int(input("Ingrese la cantidad de productos: "))
        Presupuesto = float(input("Ingrese el presupuesto total: "))
        for i in range(Producto_totales):
            opcion = int(input("Ingrese 1 para agregar un producto o 2 para eliminar producto: "))
            if opcion == 1:
                Nombre_del_producto = input("Ingrese el nombre del producto: ")
                Precio_del_producto = float(input("Ingrese el precio del producto: "))
                Cantidad_del_producto = int(input("Ingrese la cantidad del producto: "))
                Resumen_de_productos.append({'Producto': Nombre_del_producto, 'Precio': Precio_del_producto, 'Cantidad': Cantidad_del_producto})
                Precio_total += Precio_del_producto * Cantidad_del_producto
                if Precio_total > Presupuesto:
                    print("El presupuesto no es suficiente para este producto.")
            elif opcion == 2 and Resumen_de_productos:
                print("\nProductos actuales:")
                for idx, prod in enumerate(Resumen_de_productos):
                    print(f"{idx}: {prod['Producto']} (Precio: {prod['Precio']}, Cantidad: {prod['Cantidad']})")
                indice = int(input("Ingrese el número del producto que desea eliminar: "))
                if 0 <= indice < len(Resumen_de_productos):
                    del Resumen_de_productos[indice]
                    print("Producto eliminado.")
                else:
                    print("Índice inválido.")
        continue
    else:
        print("Contraseña incorrecta. No se pueden agregar o eliminar productos.")
        intentos += 1

print("\nResumen de productos:")
for producto in Resumen_de_productos:
    print(f"Producto: {producto['Producto']}, Precio: {producto['Precio']}, Cantidad: {producto['Cantidad']}")