# Las funciones con argumentos tipo *args admiten
# indetermindado numero de parametros dentro de la funcion

def ejemplo(*patos):
    print(patos)

#ejemplo('hugo','paco','luis')

def almuerzo(*comida):
    print('Entonces usted almorzo:')
    for com in comida:
        print(com)
    print('Y te vas a comer esta cantidad de tipos:')
    print(len(comida))

#almuerzo('arroz','carne','frijoles','chicharron','aguadepanela')

    
#empaquetar y desempaquetar argumentos

def tren(*vagones):
    #Esta funcion empaqueta los argumentos en una tupla
    #y los retorna
    return vagones

def tren_desarmado(vagones):
    #No se admite deesempaquetar el iterable que recibe
    return vagones

resultado = tren('vagon1','vagon2','vagon3')
print(resultado)
print(type(resultado))

vagones_nuevos = ['vagon4','vagon5','vagon6']
resultado2 = tren_desarmado(vagones_nuevos)
print(resultado2)
print(type(resultado2))
