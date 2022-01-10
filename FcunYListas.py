#definición de lista y conjunto
lista = list()
conjunto = set()
#definición de la funcipón con parámetro de recepción listaOrdenada y regresa listaOrdenada
def ingresa(listaOrdenada):
    #Ordena la lista
    listaOrdenada.sort()
    #imprime la lista total
    print("Lista Ordenada : ",listaOrdenada)
    #asigna la listaOrdenada al conjunto, para eliminar los duplicados
    conjunto = set(listaOrdenada)
    #imprime el conjunto
    print("conjunto : ", conjunto)
    #reasinga a listaOrdenada el conjunto para tener la lista ordenada y sin duplicados
    listaOrdenada = list(conjunto)
    #For para imprimir uno a uno todos los elementos de la lista
    for o in listaOrdenada:
        print(o)
    return(listaOrdenada)

#solicital usuario el numero de elementos que desea ingresar
cant=input("Cuántos #s deseas ingresar a la lista?: ")

#loop para recabar los numeros ingresados por el usuario y los ingresa a la lista
for f in range (int(cant)) :
    numero = input("Ingrese un núnero : ")
    lista.append(numero)

#llamada a la función, enviando la lista como parámetro
ingresa(lista)

#Impresión final de la lista y conjunto para validar valores
print("lista final: ",lista)
print("conjunto ",conjunto)
'''
Por qué al asignar el conjunto a la lista se desordenan y peor aún, conjunto pierde el valor al llegar al final???
'''