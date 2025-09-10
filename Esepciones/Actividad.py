i=1
lista = []
while i<=3:
    try:
        num = int(input('Dame el'+str(i)+'numero: '))
    except ValueError:
        print('Error: debes ingresar un número valido')
    else:
        lista.append(num)
        i+=1
print(lista)
print(sum(lista)/len(lista))
