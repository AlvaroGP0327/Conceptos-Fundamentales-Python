'''El objetivo de este archivo es servir como
referencia para la sintaxis de la tradicional
estructura de control de flujo match-case.
Ademas de establecer un ciclo infinito mediante
la sentencia while True. Que se rompe cuando
se ejecute un break dentro del ciclo while.
Se observa que las funciones se pueden llamar
dentro de la estructura de control'''

def libro():
    print('LEA MATEMATICAS')

def pelicula():
    print('VEA TITANIC')

def comida():
    print('COMA ALBONDIGAS')

def menu():
    while True:
        print('''QUE RECOMENDACION QUIERES''')
        print('''1 Libro
            2 Pelicula 
            3 Comida''')
        eleccion = input()

        match eleccion:
            case '1':
                libro()
            case '2':
                pelicula()
            case '3':
                comida()
            case '4':
                print('SALIENDO DEL SISTEMA....')
                break

    

