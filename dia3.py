

print()
print("Listas")
print("------")
foo = [i**2 for i in range(10)]
print(foo)

print()
print("Diccionarios")
print("------------")
foo = {i: i**2 for i in range(10)}
print(foo)

print()
print("Tuplas")
print("------")
foo = tuple(i**2 for i in range(10))
print(foo)

print()
print("Generadores")
print("-----------")
# Se crea/evalua de uno en uno, no se reserva memoria para todos los elementos
# Los generadores se reccoren una vez, no hay segunda vuelta
# Para utilizarlo varias veces convertir a una lista o tupla
# El generador ocupa siempre lo mismo independientemente del numero de elmentos
# El generados es mas lento que la lista, hace más peticiones al SO. Las listas
# definidas en una linea reserva toda la memoria de un bloque
foo = (i**2 for i in range(10))
bar = list(foo)
print(foo)

for i in foo:
    print(i)

print("vuelta 2 ...")
for i in foo:
    print(i)

print(bar)

#from sys import getsizeof
#from timeit import timeit

# FIXME: install timeit
#print(timeit([i**2 for i in range(10)]))
#print(timeit([i**2 for i in range(1000)]))


print()
print("Funciones")
print("---------")


def f(x):
    return x ** 2

print(f(10))


# Parametros infinitos
def f(*x):
    print(x)

print(f(1, 2, 3, "a", [1, 2, 3, 4]))


# Imprime el último argumento
def f(*x):
    print(x[-1])

print(f(1, 2, 3, "a", [1, 2, 3, 4]))


# Los argumentos son elementos duplicables, los argumentos pueden tener
# un valor por defecto
def duplicar(arg1, arg2=5, arg3=2):
    print(arg1, arg2, arg3)
    print(arg1 * arg2)


duplicar("a", 2)
duplicar([1, 2, "3"], 2)
duplicar([1, 2, "3"])

# Los parametros se pueden asignar a un valor especificamente en cualquier orden
duplicar(1, arg3=2, arg2=0)


# Función mas generica que se puede hacer
# ** permite sumar diccioarios
def f(*args, **kwargs):
    print(args, kwargs)

f(1, 2, 3, foo=3)


# Ejercicio: imprimir un argumento variable
#def f(*args, **kwargs):
def f( *args, veces="valor por defecto", **kwargs):
    print(veces)

f(1, 2, 4, veces="imprime esto")
f(1, 2, 4)

# Función AUN mas generica que se puede hacer
# ** permite sumar diccioarios
def f(a, b, c, *args, d=1, e=1, f=1, **kwargs):
    print(a, b, c, args, d, e, f, kwargs)


# Ejercicio: una funcion que imprima la posición de una letra de entrada en una
# cadena de entrada
def f(letra, cadena, veces=1):
    print("la letra", letra, "esta en la posición", cadena.find(letra))

f("a", "gomaespuminosa")
f("a", "gomaespuminosa", veces=0)



def f2(letra, cadena, veces=1):
    if veces == 1:
        print("la letra", letra, "ser repite", cadena.count(letra), "veces")

    pos = cadena.find(letra)
    while(pos != -1):
        print("la letra", letra, "esta en la posición", pos)
        pos += cadena[pos:].find(letra)



print()
#f2("a", "gomaespuminosa")
#f2("a", "gomaespuminosa", veces=1)

# Solucion + uso de variables globales/locales

variable_global = 1

def buscar(letra, cadena, veces=1):
    # Variable global
    global variable_global
    variable_global = 9
    # Variable local
    variable = 0
    result = 0
    for i in range(veces):
        pos = cadena.find(letra)
        result += pos
        cadena = cadena[pos + 1:]
    return result + veces - 1

print(buscar("a", "alfalfa fatal", 2))
