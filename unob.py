#programa para preguntar el nombre
nombre = input ("Cuál es tu nombre? ") #se declara la variable "nombre"
#input genera la iteracción solicitando al usuario interaccion, se recomienda incluir mensaje para que el usuario entienda
print ("Hola ", nombre)
Cumpl = input("En qué año naciste? ")
edad = 2021 - int(Cumpl)
print ("entonces tienes ", edad, "años")
print (type(Cumpl))
