import os

#Comando para listar archivos
#usando la palabra "listar"

def listar_archivos(ruta='.'):

    for elemento in os.listdir(ruta):
        print(elemento)

if __name__ == "__main__":
    listar_archivos()