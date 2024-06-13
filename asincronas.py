import asyncio

#Comer de forma sincrona
def funcion1():
    print('DESAYUNO')

def funcion2():
    print('ALMUERZO')

def funcion3():
    print('CENA')

#Comer de forma asincrona
async def main():
    task = asyncio.create_task(platillos())
    print('DESAYUNO')
    await asyncio.sleep(2)
    print('ALMUERZO')
    await asyncio.sleep(2)
    print('CENA')
    return_value = await task
    print(f'los invitados ya comieron {return_value}')


async def platillos():
    print('HUEVITOS CON PAN')
    await asyncio.sleep(3)
    print('BANDEJA PAISA')
    await asyncio.sleep(3)
    print('PASTA Y FRUTAS')
    
    return 'TERMINAMOS DE COCINAR'

asyncio.run(main())