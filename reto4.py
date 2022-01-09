#Escribe un programa que devuelva el precio de un helado solicitado por el cliente de acuerdo al topping:
#Helado con oreo: $19
#Helado con m&m: $25
#Helado con fresas: $22
#Helado con brownie: $28
#En caso de introducir otro topping, se le debe decir al cliente que el producto no esta disponible
print ("Hola Bienvenido a Helados Nahmad")
print ("Las opciones que tenemos para ti son:")
print ("1 Helado con Oreo")
print ("2 Helado con m&m")
print ("3 Helado con fresas")
print ("4 Helado con brownie")
topping = input("Cuál es el # de tu elección: ")
#print (topping)
if int(topping) == 1:
    print("Serían $19 pesos")
elif int(topping) == 2:
    print("Serían $25 pesos")
elif int(topping) == 3:
    print("Serían $22 pesos")
elif int(topping) == 4:
    print("Serían $28 pesos")
else:
    print("lo sentimos producto no disponible")

