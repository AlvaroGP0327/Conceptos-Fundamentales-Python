# pedir una recomendacion de libro,pelicula o comida
#CICLO WHILE
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

    

