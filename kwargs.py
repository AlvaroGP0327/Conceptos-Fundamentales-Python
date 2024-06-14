"""Ejemplos para ilustrar el empaquetado 
de argumentos en la forma 'clave':'valor'
**kwargs permite recibir argumentos de la forma
clave=valor para ser convertidos en un diccionario
dentro de la funcion
"""

def ejemplo(**kwargs):
    '''Recibe argumentos de la forma clave=valor
    y los convierte en un diccionario de la forma
    {clave:valor}
    retorna {clave:valor}'''
    
    return kwargs

data = ejemplo(nombre='alvaro',edad=35,pais='colombia',domicilio='philadelphia')
print(type(data))

for key, value in data.items():
    print(f'{key}:{value}')

#Se accede a la data como si fuese un diccionario normal.
print(data['domicilio'])


