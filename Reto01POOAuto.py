class Vehiculo():
    #metodos
    def describe(self):
        print("Hola soy un vehiculo con {}, viajo a {} kms/hr y tengo el {}% de comustible" .
            format(self.num_ruedas,self.velocidad,self.combustible))

    def __init__(self,velocidad,num_ruedas,combustible):
        self.velocidad = velocidad
        self.num_ruedas = num_ruedas
        self.combustible = combustible

    def __str__(self):
        return "Hola soy un vehiculo con {}, viajo a {} kms/hr y tengo el {}% de comustible".format(self.num_ruedas,self.velocidad,self.combustible)
        #return "me llamo {} y tengo {}".format(self.nombre,self.edad)
    #propiedades
    velocidad = 0
    num_ruedas = 0
    combustible = 0

#instaciar un objeto de la clase
auto1 = Vehiculo("120","4","100")
auto2 = Vehiculo("100","3","30")
auto3 = Vehiculo("20","2","0")
print("Vehiculo 1 : ",auto1)
print("Vehiculo 2 : ",auto2)
print("Vehiculo 3 : ",auto3)
#auto1.velocidad = 120
#auto1.num_ruedas = 4
#auto1.combustible = 100
#auto1.describe()
