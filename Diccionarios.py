# Como se recorren los diccionarios.
#cuales son las posibilidades al iterar sobre diccionarios
#que posibilidades hay al manipular las claves y valores (keys:values)
numbersDictionary = {'num1': 1988, 'num2': 1969, 'num3': 1944} #este es un diccionario se caracteriza por CLAVE:VALOR

#Recorrer el diccionario mostrando las clave:valor
print(numbersDictionary.items())
print(numbersDictionary.keys())
print(numbersDictionary.values())

for item in numbersDictionary.items():
    print(type(item))

for key in numbersDictionary.keys():
    print(type(key))

for value in numbersDictionary.values():
    print(type(value))


"""Con este ejercicio me he dado cuenta que los elementos que definen un diccionario
es decir sus pares clave valor (key:values) son en si mismas cada uno un objeto(tipo de dato)
por lo tanto puedo aplicar metodos propios del tipo de objeto que sea la clave o el valor
y operar sobre estos por separado"""