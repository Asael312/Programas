from Funcions import *

lista_contactos=[]      
Opcion=0
while Opcion!=4: 
    Opcion = Mostrar_menu()
    if Opcion==1:
        Agregar_contactos(lista_contactos)
    elif Opcion==2:
        Mostrar_contactos(lista_contactos)
    elif Opcion==3:
        Buscar_contacto(lista_contactos)