# def tabla (n):
#     for i in range (1,11):
#        print(n,'x',i,'=',n*i)
# tabla(5)

# def nombre_y_edad(nombre,edad):
#    print('   Hola  ')
#   print('Tu nombre es: ', nombre)
#    print('Tu edad es: ', edad)
# nombre_y_edad('Asael',18)

# def Lista():
#    lista=[55,98,61,25,84,36]
#    lista.sort(reverse=True)
#    print(lista)
#Lista()
def Mostrar_menu():
    print('--- Agenda de contactos ---','1. Agregar contacto','2. Mostrar contactos','3. Buscar contacto','4. Salir',sep='\n')

def Agregar_contactos(lista):
    contacto=[]
    nombre=input('Ingrese el nombre del contacto: ')
    telefono=input('Ingrese el telefono del contacto: ')
    correo=input('Ingrese el correo del contacto: ')
    contacto.append(nombre)
    contacto.append(telefono)
    contacto.append(correo)
    lista.append(contacto)
        
def Mostrar_contactos(lista):
    print('--- Lista de contactos ---')
    for contacto in lista:
        print(f'Nombre: {contacto[0]:<15} Telefono: {contacto[1]:<15} Correo: {contacto[2]:<15}')
    print('-'*50)
def Buscar_contacto(lista):
    nombre=input('Ingrese el nombre del contacto a buscar: ')
    for contacto in lista:
        if contacto[0]==nombre:
            print('Contacto encontrado:')
            print(f'Nombre: {contacto[0]:<15} Telefono: {contacto[1]:<15} Correo: {contacto[2]:<15}')
            print('-'*50)
            return
    print('Contacto no encontrado')
    print('-'*50)

lista_contactos=[]      
Opcion=0
while Opcion!=4:
    Mostrar_menu()
    Opcion=int(input('Ingrese una opcion: '))
    if Opcion==1:
        Agregar_contactos(lista_contactos)
    elif Opcion==2:
        Mostrar_contactos(lista_contactos)
    elif Opcion==3:
        Buscar_contacto(lista_contactos)