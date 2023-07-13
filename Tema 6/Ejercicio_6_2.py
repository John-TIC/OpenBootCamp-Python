class Alumno():
    nombre = None
    nota = None

    def __init__(self):
        self.nombre = 'Alumno'
        self.nota = 0.0
        
    def asignar_nombre(self):
        self.nombre = input('Por favor indique el nombre del alumno ==> ')

    def asignar_nota(self):
        self.nota = float(input('Por favor registre la nota para el alumno ==> '))

    def aprobo_sino(self):
        if (self.nota >= 3):
            print('El alumno ' + self.nombre + ' Aprobó')
        else:
            print('El alumno ' + self.nombre + ' No Aprobó')

a = Alumno()
a.asignar_nombre()
a.asignar_nota()
print('Para el alumno ' + a.nombre + ' la nota es ==> {0:.2f}' . format(a.nota))
a.aprobo_sino()