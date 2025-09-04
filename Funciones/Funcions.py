def Mostrar_menu():
    print('--- Agenda de contactos ---','1. Agregar contacto','2. Mostrar contactos','3. Buscar contacto','4. Salir',sep='\n')
    return int(input('Ingrese una opcion: '))

def Agregar_contactos(lista):
    contacto=[]
    nombre=input('Ingrese el nombre del contacto: ')
    telefono=input('Ingrese el telefono del contacto: ')
    correo=input('Ingrese el correo del contacto: ')
    contacto.append(nombre)
    contacto.append(telefono)
    contacto.append(correo)
    lista.append(contacto)
    print('\n','Contacto agregado exitosamente')
    layout_contacto(contacto)
        
def Mostrar_contactos(lista):
    print('--- Lista de contactos ---')
    for contacto in lista:
        layout_contacto(contacto)
    
def layout_contacto(contacto):
    print(f'Nombre: {contacto[0]:<15} Telefono: {contacto[1]:<15} Correo: {contacto[2]:<15}')
    print('-'*50)

def Buscar_contacto(lista):
    nombre=input('Ingrese el nombre del contacto a buscar: ')
    for contacto in lista:
        if contacto[0]==nombre:
            print('Contacto encontrado:')
            layout_contacto(contacto)
            return
    print('Contacto no encontrado')
    print('-'*50)

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
def menu():
    print('--- Calculo de areas ---','1. Area del cuadrado','2. Area del rectangulo','3. Area del circulo','Salir',sep='\n')
    return input('Ingrese una opcion: ')
def area_cuadrado(lado):
    return lado*lado
def area_rectangulo(base,altura):
    return base*altura
def area_circulo(radio):
    return 3.14*radio*radio