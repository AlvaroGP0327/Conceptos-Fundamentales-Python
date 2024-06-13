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
    with multiprocessing.Pool(2) as pool:
        worker_up = pool.apply_async(count_up)
        worker_down = pool.apply_async(count_down)
        #esperar a que los procesos terminen
        worker_up.get()
        worker_down.get()
    finalizar()