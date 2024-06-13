'''Consiste en dividir un proceso en "hilos"
que comparten recursos y memoria y en donde es
posible compartir variables.'''
'''Algoritmo:
*Definir una lista con las paginas que quiero extraer
*Crear una funcion que reciba una url y retorne la respuesta de la pagina
*Crear un thread por cada pagina de la lista
*Agregar cada thread a una lista de threads'''

import threading
import requests

def hilos():
    print("hola desde el hilo")

#mi_hilo = threading.Thread(target=hilos)
#mi_hilo.start()

paginas = ['https://docs.godotengine.org/en/stable/',
           'https://docs.python.org/3/',
           'https://www.postgresql.org/',
           'https://ed.team/',
           'https://roadmap.sh/']

listado_hilos = []
def obtener_pagina_web(url):
    respuesta = requests.get(url)
    print(f"Descargada la pagina: {url}")
    return respuesta


def lista_de_hilos():
    #Agregar un hilo a la lista e iniciarlos
    for url in paginas:
        hilo = threading.Thread(target=obtener_pagina_web,args=(url,))
        hilo.start()
        listado_hilos.append(hilo)
    
    #Esperar que todos los hilos se ejecuten
    #para continuar el programa
    for hilo in listado_hilos:
        hilo.join()
    
    print("Las paginas han sido descargadas")

if __name__ == '__main__':
    lista_de_hilos()




