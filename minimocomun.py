
num01 = input("Ingresa el valor de primer número : ")
num02 = input("Ingresa el valor de segundo número : ")
l01=set()
l02=set()
incremento = 1
min01=num01
min02=num02
mcm=0
bandera=False
while mcm == 0 :
    min01 = int(num01) * int(incremento)
    min02 = int(num02) * int(incremento)
    l01.add(min01)
    l02.add(min02)
    incremento += 1
    for e in l01:
        bandera=e in l02
        if bandera :
            mcm=e
print("lista 01", l01)
print("lista 02", l02)
print("mcm = ",mcm)



    

