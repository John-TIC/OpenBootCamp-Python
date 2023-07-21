from pickle import *

class Vehiculo:
    def __init__(self, linea, marca):
        self.linea = linea
        self.marca = marca

    def __str__(self):
        return self.linea + " " + self.marca


perfil_empleado = Vehiculo("Twingo 1.5", 'Renault')
print(perfil_empleado)

f = open('Obc_Ejercicio_8_2.bin', 'w+b')
dump(perfil_empleado, f)
f.close()

f = open('Obc_Ejercicio_8_2.bin', 'rb')
perfil_primerempleo = load(f)

print(perfil_primerempleo)
f.close()