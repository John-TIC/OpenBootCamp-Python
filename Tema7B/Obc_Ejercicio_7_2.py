import time

def validar_hora():
    """
    Para una jornada laboral que finaliza a las 7 pm. La función vVerifica si el horario de trabajo ha terminado y se puede regresar
     a casa o, en caso contrario nos dice cuanto falta (horas, minutos y segundos) para concluir la jornada laboral.
    """
    hora_act = time.localtime()
    
    if ((hora_act[3])> 19):
        print('Es hora de ir a casa')
    else:
        print('Restan ' + str(19 - hora_act[3]) + ' horas, ' + str(60 - hora_act[4]) + ' minutos y '
              + str(60 - hora_act[5]) + ' segundos de jornada laboral')

def main():
    validar_hora()

if __name__ == '__main__':
    main()