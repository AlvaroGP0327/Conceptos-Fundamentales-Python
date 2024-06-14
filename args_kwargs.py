# Las funciones con argumentos tipo *args admiten
# indetermindado numero de parametros dentro de la funcion
# Se interpretan como sentencias de "empaquetado" y "desempaquetado"
# de argumentos.

def ejemplo(*patos):
    '''Funcion que recibe tres nombres
    de tipo string y retorna una tupla 
    compuesta por los nombres ingresados.
    ejemplo('hugo','paco','luis')
    retorna ('hugo','paco','luis')
    <class tuple>'''
    return patos

def ejemplo_1(patos):
    '''Ejemplo testigo sin implementar el operador (*)
    para evaluar como se comporta la funcion.
    ejemplo('hugo','paco','luis')
    retorna error debido a que no me empaqueta los
    tres datos de tipos string.Y la funcion solo esta aceptando
    un solo argumento.'''
    return patos

def ejemplo_2(*patos):
    '''Ejemplo testigo para pasar como argumento
    una tupla y evaluar como se comporta la funcion
    ejemplo(('hugo','paco','luis'))
    retorna una lista dentro de otra lista
    (('hugo','paco','luis'),)'''
    return patos

def ejemplo_3(*patos):
    '''Ejemplo testigo para pasar como argumento
    una tupla definida y evaluar como se comporta la funcion
    ejemplo(my_tupla)
    retorna de la misma forma que si se pasa la tupla
    del ejemplo_2. '''
    return patos

def ejemplo_4(*patos):
    '''Ejemplo aparte, aplicar al empaquetado de argumentos
    el operador (*) en el retorno de la funcion.
    ejemplo(*args)
    return(*args)
    Esta es una operacion que no es permitida en este contexto.'''

def ejemplo_5(*dias):
    '''Recibir tipo string los dias de la semana
    y empaquetarlos en una lista y operarla dentro 
    de la funcion con un ciclo for.Para demostrar
    que los datos tipo string han sido empaquetados
    dentro de una lista.'''
    for dia in dias:
        print(dia)
    
    return dias

d1,d2,d3,d4,d5,d6,d7 = 'lunes','martes','miercoles','jueves','viernes','sabado','domingo'
print(type(d1))
dias_semana = ejemplo_5(d1,d2,d3,d4,d5,d6,d7)
print(dias_semana)
print(type(dias_semana))

#En conclusion todo parametro que se pase como argumento
#operado con (*) sera 'empaquetado dentro de una tupla'.
#No se admite como operacion valida desempaquetar el iterable
#que se recibe.
#dentro de la funcion se opera con el iterable recibido con *args


