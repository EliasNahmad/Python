class Vehiculo():
    #metodos

    def __init__(self,velocidad,num_ruedas,medio,mensaje):
        self.velocidad = velocidad
        self.num_ruedas = num_ruedas
        self.medio = medio
        self.mensaje = mensaje

    def __str__(self):
        return "Hola soy un vehiculo con {}, velocidad {} y me desplazo en el {}".format(self.num_ruedas,self.velocidad,self.medio)
 
    def avanzar(self):
        print("Este es un {}".format(self.mensaje))

    #propiedades
    __velocidad = 0
    __num_ruedas = 0
    __medio = 0
    __mensaje = ""

#instaciar un objeto de la clase
barco = Vehiculo("baja","0","Agua","BARCO")
auto = Vehiculo("media","4","Calle","AUTO")
avion = Vehiculo("alta","6","Aire","AVION")
print("Barco : ",barco)
print("Auto : ",auto)
print("Avion : ",avion)

barco.avanzar()
