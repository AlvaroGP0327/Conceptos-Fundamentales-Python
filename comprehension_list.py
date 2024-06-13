'''Estructura de una lista por comprension:
nombre_lista_generada = [expresion_generadora for n in lista_madre]'''
'''Toma cada elemento de una lista, lo evalua en una expresion
y genera un nuevo elemento que se va pertenecer a una nueva lista'''

listado1 = [2,4,6,8,10]
listado2 = []

listado2 = [n + 1 for n in listado1]
print(listado2)

listado3 = [n for n in listado2 if n > 3]
print(listado3)