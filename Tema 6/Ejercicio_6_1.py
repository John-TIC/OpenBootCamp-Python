class Vehiculo():
    color = 'Azul'
    ruedas = 5
    puertas = 4

class Coche(Vehiculo):
    velocidad = 50
    cilindrada = 1599

c = Coche()
print(c)
print(dir(c))
