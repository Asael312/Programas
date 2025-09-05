# Mostrar números del 1 al 5.
i = 1
while i <= 5:
    print(i)
    i += 1
# Pedir contraseña hasta que sea correcta.

contraseña = ""
while contraseña != "mi_contraseña":
    contraseña = input("Introduce la contraseña: ")

print("Contraseña correcta.")

# Mostrar cuenta regresiva de 10 a 1.

i = 10
while i >= 1:
    print(i)
    i -= 1

# Pedir un número hasta que sea mayor a 100.

num = 0
while num <= 100:
    num = int(input("Introduce un número mayor a 100: "))

print("Número válido:", num)

# Sumar números hasta que el usuario escriba 0.

suma = 0
while True:
    num = int(input("Introduce un número (0 para salir): "))
    if num == 0:
        break
    suma += num

print("Suma total:", suma)

# Mostrar una tabla de multiplicar mientras el número sea positivo.

num = int(input("Introduce un número para ver su tabla de multiplicar: "))
while num > 0:
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    num = int(input("Introduce otro número positivo (o un número negativo para salir): "))

# Repetir “Hola” 5 veces con contador.

i = 1
while i <= 5:
    print("Hola")
    i += 1

# Pedir un número y mostrar sus divisores.

num = int(input("Introduce un número: "))
print("Divisores de", num, ":")
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1

# Pedir letras hasta que el usuario escriba “x”.

letra = ""
while letra != "x":
    letra = input("Introduce una letra (x para salir): ")
    letras += letra
    print("Letras introducidas:", letras, sep=', ')

print("Has salido del bucle.")

# Calcular la suma de los primeros 10 números naturales.

suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1

print("La suma de los primeros 10 números naturales es:", suma)