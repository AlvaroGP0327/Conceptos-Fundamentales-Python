''' Capacidad de la computadora de ejecutar varias
tareas (procesos al mismo tiempo)
Se emplea el modulo multiprocesing que permite
crear y administrar multiples procesos en paralelo.'''

'''Algoritmo:
*Creas una lista de objetos de proceso que se van a iniciar
a medida que recorres la lista de procesos.
*Cada proceso ejecuta su tarea de forma independiente.
Algunas tareas pueden tardar más que otras dependiendo de la carga de trabajo
y de los recursos disponibles.
*Luego, cuando llamas al método join() en cada proceso en la lista,
el programa principal espera a que cada proceso termine su ejecución
antes de continuar con la siguiente instrucción en el programa principal.
Una vez que todos los procesos hayan terminado,
el programa principal continúa su ejecución'''

import multiprocessing
from random import randint
from time import sleep
'''Programa que cuenta del 1 al 10 en positivo
y negativo, dejando entre numero y otro una pausa
de duracion aleatoria
contar hacia adelante y hacia atras son dos procesos'''

def count_up():
    i:int = 0
    while i <= 10:
        print(f"UP: {i}")
        sleep(1)
        i += 1

def count_down():
    i = 0
    while i >= -10:
        print(f"DOWN: {i}")
        sleep(2)
        i -= 1
def finalizar():
    print("Los procesos han terminado")

if __name__ == "__main__":
    #creacion del objeto Proceso
    worker_up = multiprocessing.Process(target=count_up)
    worker_down = multiprocessing.Process(target=count_down)
    
    #inicializacion
    worker_up.start()
    worker_down.start()
    #unir los subprocesos en un proceso principal
    #hasta que no se terminen todos los procesos
    #no continua el programa
    worker_up.join()
    worker_down.join()
    finalizar()
