d1 = {}
d2 = dict() 


#Crear diccionario con datos
d3 = {"Usuario": "usser123", "Correo": "us12@bedu.org", "Compañia": "Bedu"} 
#Es importante señalar que la información se almacena en pares en formato llave:valor
print(d3)
#Se pueden obtener las llaves y valores en formato de lista.

# Se pueden obtener las llaves en una lista
d3.keys() 
print(d3.keys())
# Se pueden obtener los valores en una lista
d3.values() # Lista de valores
print(d3.values())
#Agregar datos a diccionario

#Se pueden agregar entradas en un diccionario
d3['ciudad']= "CDMX"
#Se puede acceder a los valores del diccionario usando su llave
d3['Genero']="Masc"
print(d3['ciudad'])
print(d3)
#Tambien podemos extraer datos usando pop
a = d3.pop('ciudad')
print(a)
#'''