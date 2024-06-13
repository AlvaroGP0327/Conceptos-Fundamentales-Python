from sys import getsizeof
import timeit
'''Tienen una sintaxis parecida a las
listas por comprension.
Con la diferencia que las listas por comprension
retornan una lista y los generadores retornan un objeto'''
'''La lista por comprension crea todos los elementos de la
lista y los guarda en memoria. 
El generador de expresion guarda en memoria el algoritmo
para generar una lista.'''
'''El tamano del generador es mucho menor en memoria que
el de la lista'''
'''La lista se crea en mucho menos tiempo que el generador'''
'''Los tiempos de recorrido son menores en las listas.'''

lista_cuadrados = [i ** 2 for i in range(10)]
generador_cuadrados = (i ** 2 for i in range(10))
#Ejercicio para ilustrar la diferencia
#Crear dos listas de numeros del 0 al 1000 multiplicados por 5
#Uno por medio de lista y otro por generador

def medir_lista():
    lista = [x * 5 for x in range(1000)]
    return lista

def medir_generador():
    generator = (x * 5 for x in range(1000))
    return generator

def iterar_lista():
    for x in medir_lista():
        pass

def iterar_generador():
    for x in medir_generador():
        pass       

print('espacio en memoria')
print(getsizeof(medir_lista()))
print(getsizeof(medir_generador()))

print('tiempos de recorrido')
recorrer_lista = timeit.timeit(iterar_lista,number=1)
recorrer_generador =  timeit.timeit(iterar_generador,number=1)
print(recorrer_lista)
print(recorrer_generador)