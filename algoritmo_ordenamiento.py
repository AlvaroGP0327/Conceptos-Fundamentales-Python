#Generar una  lista de numeros aleatorios
#Usar el algoritmo de ordenamiento por burbuja

import random

def lista_aleatoria(lim_inf,lim_sup,cantd):
    limite_inferior = lim_inf
    limite_superior = lim_sup
    cantidad_numeros = cantd
    lista_aleatoria = random.sample(range(limite_inferior,limite_superior +1),cantidad_numeros)

    return lista_aleatoria

def algorit_ordenamiento_burbuja(lista_desordenada):
    n = len(lista_desordenada)
    for recorrido in range(n-1):
        for i in range(n-1):
            temporal = 0
            if lista_desordenada[i] > lista_desordenada[i+1]:
                temporal = lista_desordenada[i]
                lista_desordenada[i] = lista_desordenada[i+1]
                lista_desordenada[i+1] = temporal
     
    print('cantidad de recorridos ' + str(recorrido+1))   
    return lista_desordenada

lista_aleatoria = lista_aleatoria(1,99,10)
print(lista_aleatoria)
lista_ordenada = algorit_ordenamiento_burbuja(lista_aleatoria)
print(lista_ordenada)
