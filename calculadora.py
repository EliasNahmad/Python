#Crea una calculadora:
#Se deben solicitar al usuario dos números
#Se puede seleccionar entre diferentes operaciones(suma, resta, multiplicación y división).
#Imprimir resultados
#Considerar división entre cero y caracteres no definidos como operaciones.
print ("Bienvenido a la calculadora básica")
a = input ("Para iniciar por favor introduzca el primer número ")
op = input ("Ahora introduzca el operador ")
b = input ("Para iniciar por favor introduzca el segundo número ")
if op == "+":
    Resultado = int(a) + int(b)
    print("{} {} {} = {}".format(a,op,b,Resultado))
elif op == "-" :
    Resultado = int(a) - int(b)
    print("{} {} {} = {}".format(a,op,b,Resultado))
elif op == "*":
    Resultado = int(a) * int(b)
    print("{} {} {} = {}".format(a,op,b,Resultado))
elif op == "/":
    if int(b)==0:
        print ("Error División entre 0")
    else:
        Resultado = int(a) / int(b)
        print("{} {} {} = {}".format(a,op,b,Resultado))
else:
   print ("Operador no permitido")


