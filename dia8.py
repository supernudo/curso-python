
# Multiprocesing
#Pull() pone por defecto en numero de procesadores de la maquina
# Pool.map espera a que terminen todos los procesos, prepara todos los
# interpretes y luego lanza todo a la vez
# Concurrent.futures hace lo mismo que Pool, permite cambiar Process / Threads
# ProcessPoolExecutor / ThreadPoolExecutor. Es un poco mas lento que Pool
# as_completed permite obtener los resultados en el momento que termina cada
# worker. ProcessPoolExecutor.submit devuelve futuros, ejetuta todo en el momento
# no espera a preparar todo como map().

from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed
from time import sleep

def f(number):
    sleep(1)
    return "number " + str(number) + ", " + str(datetime.now())

def main1():
    with ProcessPoolExecutor(max_workers=5) as ex:
        results = [ex.submit(f,i) for i in range(10)]
        for result in as_completed(results):
            print(result.result())


# Ejercicio 2
import asyncio
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed
from time import sleep

async def fetch(delay):
    asyncio.sleep(delay)
    #sleep(delay)
    return "number " + str(delay) + ", " + str(datetime.now())

def f2(delay):
    sleep(1)
    #return "number " + str(delay) + ", " + str(datetime.now())
    return asyncio.run(fetch(delay))

def main2():
    with ProcessPoolExecutor(max_workers=5) as ex:
        results = [ex.submit(f2, i) for i in range(10)]
        for result in as_completed(results):
            print(result.result())

if __name__ == '__main__':
    #main1()
    main2()