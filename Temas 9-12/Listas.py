# Crea una lista con los días de la semana e imprime el tercer día.
Semana=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(Semana[2])
# Declara una lista con 5 números y calcula la suma total.
numeros = [10, 20, 30, 40, 50]
print(sum(numeros))
# Pide al usuario 5 nombres, guárdalos en una lista y muéstralos en orden inverso.
nombres = []
for i in range(5):
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)
print("Nombres en orden inverso:")
print(nombres[::-1])
# Cambia un valor específico de una lista (ej. “Berano” → “Verano”).
nombres = ["Invierno", "Primavera", "Verano", "Otoño"]
nombres[2] = "Verano"
print(nombres)
# Usa índices negativos para mostrar el último y penúltimo elemento de una lista.
print("Último elemento:", nombres[-1])
print("Penúltimo elemento:", nombres[-2])
# Agrega un nuevo elemento al final de una lista con .append().
nombres.append("Heriberto")
print("Lista después de agregar un elemento:", nombres)
# Elimina el primer elemento de una lista con .pop(0).
nombres.pop(0)
print("Lista después de eliminar el primer elemento:", nombres)
# Ordena una lista de números y muéstrala en pantalla.
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print("Lista ordenada:", numeros)
# Verifica si un número ingresado por el usuario está en una lista predefinida.
numero = int(input("Introduce un número: "))
if numero in numeros:
    print("El número está en la lista.")
else:
    print("El número no está en la lista.")
# Crea una lista vacía y permite al usuario añadir elementos hasta escribir “fin”.
nueva_lista = []
while True:
    elemento = input("Introduce un elemento (o 'fin' para terminar): ").lower()
    if elemento == "fin":
        break
    nueva_lista.append(elemento)
print("Lista final:", nueva_lista)