def layout(producto):
    for x,y in producto:
        print(x,y)
        
def MostrarInventario(lista):
    print("Inventario:")
    for producto in lista.keys():
        layout(producto)
def Menu():
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print('5.Presupuesto')
    print("6. Salir")
    Opcion = int(input("Seleccione una opción: "))
    return Opcion
Opcion=0
Productos = {'Laptop':{'codigo':'AL6165','Stock':20,'precio':300}}
while Opcion !=6:
   Opcion=Menu()
   if Opcion == 1:
       producto=input('Ingrese el nombre del producto')
       MostrarInventario(Productos)