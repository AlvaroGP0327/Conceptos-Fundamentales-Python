'''Script para ilustrar el paso de parametros
a una funcion que puede ser por valor o por
referencia.Los objetos en Python se pasan siempre
por referencia a memoria.'''
'''El modulo typin de python ofrece anotaciones
de tipo mas avanzadas.'''
x = 5
def cambiar_variable(var:int) -> int:
    var+= 5
    return var

lista = [1,2,3,4]
def cambiar_lista(listado:list)->list:
    listado.append(5)
    return listado
