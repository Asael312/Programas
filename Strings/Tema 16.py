texto1 = 'hola'
texto2 = '\"MUNDO\"'
texto4 = 123
texto3 = texto1 + "   " + texto2 + str(texto4)
lista = ['Juan', 'pedro']
nombre = 'JUAN'
for nomb in lista:
    nomb.lower()
    if nombre.lower in lista:
        print('si esta')
if nombre.lower in lista:
    print('si esta')

print(texto3)
print(type(texto3))
print(texto3[7])
print(texto3[0:4:1])
print(texto3[0:4:2])
print(texto3.capitalize())
print(texto3.title())
print(texto3.find('HOLA'))
print(texto3.lower())
print(texto3.upper())
texto5 = texto3.replace('MUNDO','COMPADRE')
print(texto5)
print(texto5.strip())
email = 'hola@mundo.com'
print(email.split('@')[0])
email = 'Hola,como,estas'
nombres = email.split(',')
lista_completa = []
for nombre in nombres:
    print (nombre)
print()
name = 'Jose'
clase = 'Matematicas'
print(f"hola {name}, bienvenido a la clase de {clase} {1+3}")
print("hola {}, bienvenidoa la clase {} {}".format(nombre,clase,1+3))
