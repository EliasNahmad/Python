'''
# declara la lista y la imprime completa
lista = [1,2,3,4]
print (lista) 

#agregó el 17 y se imprime de nuevo toda la lista
lista.append(17)
print (lista)

#agregamos el 3.14 e imprimimos la lista pero elemento por elemento
lista.append(3.14)
for numero in lista:
    print(numero)

#se ordena la lista
lista.sort()
#Se imprime la lista elemento por elemento
for numero in lista:
    print(numero)

lista = ["e","a","o","u"]
print (lista) 

#agregó el "i" y se imprime de nuevo toda la lista
lista.append("i")
print (lista)

for numero in lista:
    print(numero)

#se ordena la lista
lista.sort()
#Se imprime la lista elemento por elemento
for numero in lista:
    print(numero)

#se ordena la lista
lista.sort(reverse=True)
#Se imprime la lista elemento por elemento
for numero in lista:
    print(numero)
  '''
lista=["cafe dormido","pan feliz","cacahuate cansado","fresa depresiva","manteconcha feliz"]
print(lista)

lista.sort()
print(lista)

print(lista[0])

lista.append("nacho enfermo")
print(lista)

lista.sort()
print(lista)