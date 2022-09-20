

class Vehiculo():
    color="blanco"
    ruedas=4
    puertas=5

class Coche(Vehiculo):
    velocidad=120
    cilindrada=4

x = Coche()
x.velocidad=200
x.color
x.puertas=8
x.ruedas
x.cilindrada= 6

print("La velocidad es: ",x.velocidad)
print("el color es: ", x.color)
print("Cantidad de puertas ",x.puertas)
print("Total de ruedas ",x.ruedas)
print("Cilindrada ",x.cilindrada)
