import Usuario
import Tarjeta

print ("Bienvenido al Banco del malestar")
print ("Para nostros es un placer atenderlo")
diccionario_datos={
  "Nombre":["elias","moises","javier","marcela"],
  "Tasa":["10","11","12","13"],
  "Deuda":["1000","2000","3000","4000"],
  "NuevosCargos":["100","200","300","400"],
  "MontoPago":["0","0","0","0"],
  "ProximoPago":["0","0","0","0"]}


#para probar las funciones hay que descomentar la que se requiera

#funcion1 = Tarjeta.crea_tarjeta()
#Tarjeta.captura_nueva_deuda(diccionario_datos)
#Tarjeta.genera_reporte(diccionario_datos)
#Tarjeta.iteracion(diccionario_datos)
#Tarjeta.liquida_deuda(diccionario_datos)#pago recurrente

diccionario_datos={"Nombre":"Elias","Tasa":"10","Deuda":"3000","NuevosCargos":"0"}
nuevos_cargos = input("Nuevos cargos para generar reporte :$ ")
Usuario.genera_reporte(diccionario_datos,nuevos_cargos)