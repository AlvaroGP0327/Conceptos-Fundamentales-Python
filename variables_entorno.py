'''Se usan para guardar de forma segura, configuraciones
generales para toda la aplicacion o parte de ella
-Se importa el modulo os, para implementar el metodo
getenv() que es el que permite traer las variables de entorno
desde el archivo .env
-Se crea un archivo .env, en donde se van a guardar las VARIABLES_ENTORNO
-Desde el scripts donde se necesiten las variables de entorno
importar el modulo os y load_dotenv.
-Usar las variables dentro del modulo requerido'''

import os
from dotenv import load_dotenv

load_dotenv()

cargar_cadena_texto = os.getenv("SALUDO")
print(cargar_cadena_texto)
