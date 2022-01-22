diccionario_datos={"Nombre":"Elias","Tasa":"10","Deuda":"3000","NuevosCargos":"0"}
'''
NuevosCargos = 2000
import TarjetaPaq.Usuario
help(TarjetaPaq.Usuario.genera_reporte)
TarjetaPaq.Usuario.genera_reporte(diccionario_datos,NuevosCargos)
'''

import TarjetaPaq.Tarjeta

#para probar las funciones hay que descomentar la que se requiera

#funcion1 = TarjetaPaq.Tarjeta.crea_tarjeta())
help(TarjetaPaq.Tarjeta.crea_tarjeta)
#TarjetaPaq.Tarjeta.captura_nueva_deuda(diccionario_datos)
#help(TarjetaPaq.Tarjeta.captura_nueva_deuda)
#TarjetaPaq.Tarjeta.genera_reporte(diccionario_datos)
#help(TarjetaPaq.Tarjeta.genera_reporte)
diccionario_datos2={
  "Nombre":["elias","moises","javier","marcela"],
  "Tasa":["10","11","12","13"],
  "Deuda":["1000","2000","3000","4000"],
  "NuevosCargos":["100","200","300","400"],
  "MontoPago":["0","0","0","0"],
  "ProximoPago":["0","0","0","0"]}
#TarjetaPaq.Tarjeta.iteracion(diccionario_datos2)
#TarjetaPaq.Tarjeta.liquida_deuda(diccionario_datos)#pago recurrente
