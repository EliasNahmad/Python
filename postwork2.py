''' 
Crea la función crea_tarjeta, esta debe contener la captura de datos de una tarjeta 
     y devolver un diccionario con la información. En caso de que se indique un monto mayor 
     de pago del posible, debe indicar el error con un mensaje y solicitar la información 
     nuevamente.
Crea la función captura_nueva_deuda, la cual debe recibir un diccionario con los datos 
    de una tarjeta y hacer los cálculos vistos en el postwork 1, agregando la nueva deuda como un 
    cargo adicional del diccionario.
Crea la función generar_reporte, esta debe escribir
Crea una función que itere sobre una lista de tarjetas e imprima los reportes de todas.
Crea la función pago_recurrente, la cual proyectará una serie de pagos del mismo monto en una 
    tarjeta, para una deuda que no tendrá nuevos cargos. Hasta convertir el valor de la deuda en 0. 
    Para cada mes proyectado se debe imprimir el reporte correspondiente.
Haz llamadas y prueba las funciones que has creado
'''
Nomb_Tarj = 0
Deuda = 0
Tasa = 0
Nvos_cargos = 0
Monto_pago = 0
diccionario_datos = 0
Prox_Pago = 0
nuevos_cargos = 0.0
diccionario_datos={"Nombre":"Elias","Tasa":"10","Deuda":"3000","NuevosCargos":"0"}


def calcula_prox_pago(Deuda,Tasa):
  Prox_Pago = float(Deuda)
  Prox_Pago += (float(Tasa)/1200)*float(Deuda)
  #print ("Su próximo pago es por {}".format(Prox_Pago))
  return(Prox_Pago)

def genera_reporte(d01):
  print("Nombre : {}".format(d01["Nombre"])) 
  print("Su tasa contratada es : {}%".format(d01["Tasa"])) 
  print("Deuda al día : ${}".format(d01["Deuda"]))
  monto = float(d01["Deuda"])+float(nuevos_cargos)
  d01["NuevaDeuda"]= calcula_prox_pago(monto,d01["Tasa"])
  print("Deuda con intereses : ${}".format(d01["NuevaDeuda"]))
  return(d01["NuevaDeuda"])  

def iteracion(d01):
  consecutivo = 0
  for i in d01["Nombre"]:
    print("Nombre : {}".format(d01["Nombre"][consecutivo]))
    print("Tasa : {}".format(d01["Tasa"][consecutivo]))
    print("Deuda : {}".format(d01["Deuda"][consecutivo]))
    print("Nuevos Cargos : {}".format(d01["NuevosCargos"][consecutivo]))
    consecutivo +=1

def crea_tarjeta():
    Nomb_Tarj = input("Nombre de la tarjeta : ")
    Tasa = input("Cuál es la tasa de interés contratada : ")
    Deuda = input ("Acuanto asciende su deuda : ")
    Nvos_cargos = input("Cuál fue el monto de sus últimos cargos? : ")
    Prox_Pago2 = calcula_prox_pago(Deuda,Tasa)
    numero = 0
    Monto_pago = Prox_Pago2*2
    while float(Monto_pago)>=float(Prox_Pago2):
      print("Su próximo pago es por : ${:.2f}".format(Prox_Pago2))
      Monto_pago = input("Cuánto quiere pagar, recuerde que no puede más del monto de su próximo pago? : ")
      numero += 1
      print("Monto Proximo Pago : ", Prox_Pago2)
      print("Monto Pago : ", Monto_pago)
      diccionario_datos={"Nombre":Nomb_Tarj,"Tasa":Tasa,"Deuda":Deuda,"NuevosCargos":Nvos_cargos,"MontoPago":Monto_pago,"ProximoPago":Prox_Pago2}
    return(diccionario_datos)

def captura_nueva_deuda(d01):
  d01["Deuda"]=calcula_prox_pago(d01["Deuda"],d01["Tasa"])
  print("Su saldo al día de hoy es : ${}".format(d01["Deuda"]))
  nuevos_cargos = input("Por favor introduzca el monto de sus nuevos cargos : ")
  d01["NuevaDeuda"]= calcula_prox_pago(d01["Deuda"]+float(nuevos_cargos),d01["Tasa"])  
  #print(d01.values())
  print("Su saldo actualizado con intereses es : ${:.2f}".format(d01["NuevaDeuda"]))

def liquida_deuda(d01):
  mes = 0
  nuevos_cargos = 0.0
  Pago = float(d01["Deuda"])*.1
  while float(d01["Deuda"])>0:
    d01["Deuda"] = genera_reporte(d01)
    mes += 1
    if Pago > float(d01["Deuda"]):
      Pago = float(d01["Deuda"])
    print("El pago para el mes {} es de ${}".format(mes,Pago))
    d01["Deuda"]=d01["Deuda"]-Pago
#   pausa = input("continua?")



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

#funcion1 = crea_tarjeta()
#captura_nueva_deuda(diccionario_datos)
#genera_reporte(diccionario_datos)
#iteracion(diccionario_datos)
#liquida_deuda(diccionario_datos)#pago recurrente

