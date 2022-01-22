

def calcula_prox_pago(Deuda,Tasa):
  """Calula el interes a pagar de acuerdo a la deuda y tasa recibidos"""
  Prox_Pago = float(Deuda)
  Prox_Pago += (float(Tasa)/1200)*float(Deuda)
  return(Prox_Pago)

def genera_reporte(d01,nuevos_cargos):
  """Esta funcion permite imprimir la informacion del 
  tarjetabiente que se le envie en el directorio y nuevos cargos"""
  print("Nombre : {}".format(d01["Nombre"])) 
  print("Su tasa contratada es : {}%".format(d01["Tasa"])) 
  print("Deuda al día : ${}".format(d01["Deuda"]))
  print("Sus últimos cargos son por : ${}".format(nuevos_cargos))
  monto = float(d01["Deuda"])+float(nuevos_cargos)
  d01["NuevaDeuda"]= calcula_prox_pago(monto,d01["Tasa"])
  print("Deuda Total con intereses : ${:.2f}".format(d01["NuevaDeuda"]))
  return(d01["NuevaDeuda"])  
