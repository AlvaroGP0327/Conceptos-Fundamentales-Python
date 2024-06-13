'''La pieza central de la programacion
asincrona es la corrutina.Que es un objeto
cuya ejecucion puede pausarse y retomarse
mas tarde.'''
'''Las corrutinas solo pueden ser
llamadas desde otras corrutinas
o usando el metodo especial run()'''
'''No se puede extraer directamente 
el retorno de una corrutina, puesto 
que estas retornan es un objeto corrutina'''
'''Para extraer el retorno de una corrutina
hace falta usar la palabra reservada await'''

import asyncio

async def saludar():
    print('hola mundo')

async def uno():
    return 1

#Intentar llamar una corrutina desde otra
async def main():
    resultado = await uno()
    print(resultado)

asyncio.run(main())