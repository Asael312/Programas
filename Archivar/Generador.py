# nombre = input('Dame un nombre: ')
# archivo = open ("datos.txt", "w")
# archivo.write( f"Hola, {nombre}\n")
# archivo.write( "Comoestas?")

# alumno = ['Hugo', 'Paco', 'Luis']#Necesita usar un for o csv#
# with open ("datos.txt", "w") as archivo:
    # for dato in alumno:
    #  archivo.write(dato)

#    archivo.write('Juan,AL06846,Industrial\n')
#   archivo.write('Alberto,AL09849,Mecatronica')
# import csv
# with open ("datos.csv","w",newline='') as file:
#      writer = csv.writer(file)
#      writer.writerow(["Nombre","Edad"])
#      writer.writerow(["Ana", 20])
#      writer.writerow(["Juan", 19])
#      writer.writerow(["Pepe", 18])
# archive_name = input('Déme el nombre del archivo: ')
# Frase1 = input('Dame una frase')
# Frase2 = input('Dame otra frase')
# Frase3 = input('Dame una Ultima frase')
# archivo = open(f"{archive_name}.txt","w")
# archivo.write(f"{Frase1}\n")
# archivo.write(f"{Frase2}\n")
# archivo.write(f"{Frase3}\n")
 
# with open (f"{archive_name}.txt","w") as file:
# 
#     for i in range(4):
#         frase = input('Una frase: ')
#         file.write(f"{frase}\n")

# Lectura de archivos

with open ("Nombres.txt","r",newline="") as file:
    for linea in file:
        print(linea)