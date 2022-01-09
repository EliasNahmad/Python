''' 
Haz un programa que solicite al usuario los siguientes datos 
- Nombre de la tarjeta
- Tasa de interés
- Deuda
- Pago a realizar
- Nuevos cargos

El programa deberá devolver un resumen de la información y calcular el monto del próximo pago mensual.
El programa deberá considerar que no es posible realizar un pago superior al total de la deuda del mes pasado.
Para los fines de este trabajo, considera las siguientes fórmulas. interes_mensual = tasa_interes/12 
deuda_recalculada = (deuda - pago)*(1+interes_mensual) nueva_deuda = deuda_recalculada + cargos

'''
print ("Bienvenido al Banco del malestar")
print ("Para nostros es un placer atenderlo")
Nomb_Tarj = input("Nombre de la tarjeta : ")
Tasa = input("Cuál es la tasa de interés contratada : ")
Deuda = input ("Acuanto asciende su deuda : ")
Nvos_cargos = input("Cuál fue el monto de sus últimos cargos? : ")
print ("Nombre de la Tarjeta : ", Nomb_Tarj)
print ("Tasa de interés contratada : ",Tasa)
print ("Deuda Actual : ",Deuda)
print ("Nuevos Cargos : ",Nvos_cargos)
Prox_Pago = float(Deuda)
Prox_Pago += (float(Tasa)/1200)*float(Deuda)
print ("Su próximo pago es por {}".format(Prox_Pago))
Desea_Pago = input ("Desea Realizar su pago S/N : ")
if Desea_Pago=="n" or Desea_Pago=="N" :
  print ("Gracias por preferir el Banco del Malestar, vuelva pronto")
else:
  Pago = input ("Favor de ingresar el monto que desea pagar : ")
  if float(Pago) > float(Prox_Pago):
    print ("Su pago no puede ser mayor a la deuda total {}".format (Prox_Pago))
  else:
    print ("Gracias por su Pago")
    print ("Saldo de deuda actualizado : {}".format(float(Prox_Pago)-float(Pago)))
    Prox_Pago = float(Prox_Pago)-float(Pago)
if float(Prox_Pago) == 0.0:
      print ("Su cuenta al corte del mes pasado está en 0's, Felicidades")

print ("Actualizando saldo...calculando...")
Prox_Pago = float(Prox_Pago) + float(Nvos_cargos)
print ("Su saldo actualizado es : $",Prox_Pago)
print ("Gracias por preferir el Banco del Malestar, vuelva pronto")


