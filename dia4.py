

# Varios parametros devueltos son tuplas
def f():
    a = 1
    #return a
    return 1, 2, [3, 5], a

a = f()
print(type(a))
#a[1] =  0

# Los parametros por defecto tipo lista, diccionario o clase se decalran para
# una funcion dada como estaticas, mantienen su valor de una ejecución a otra
def f(foo = []):
    foo.append(len(foo))
    print(foo)

f()
f()

# Se puede inspeccionar el código y variables intaernas de una funcion
print(f.__code__.co_varnames)

# Funcion Lambda
# Ocupa menos memoria y se ejecuta más rápido
f = lambda x: x**2
print(f(10))

# FUNCIONES QUE ACEPTAN COMO PARAMETROS FUNCIONES

# Funciones map
# Map devuelve generadores, aplica la funcion pasada como parametro
# Necesitamos aplicar una funcion al generador para obtener los valores
foo = [i**2 for i in range(10)]
bar = map(str, foo)
print(type(bar))
print(bar)
print(list(bar))

# Funcion ·filter
# Aplica una función tipo True/False
foo = [i**2 for i in range(10)]
bar = filter(lambda x: x > 10, foo)
print(type(bar))
print(bar)
print(list(bar))

# Funcion reduce
# Aplica una función recursivamente
from functools import reduce
foo = [i**2 for i in range(10)]
bar = reduce((lambda x, y: x - y), foo)
print(type(bar))
print(bar)


# Equivalente a sobrecarga
def foo(arg):
    if isinstance(arg, int):
        return arg + 1
    elif isinstance(arg, str):
        return int(arg) + 1
    elif isinstance(arg, list):
        return list(map(lambda x: x + 1, arg))

print(foo(2))
print(foo("2"))
print(foo([2, 3]))

# Esta version permite procesar cualquier tipo de argumento,
# la de arriba no podria con ['1', '2', '3']
# Aplicacion: grafos
def foo(arg):
    if isinstance(arg, int):
        return arg + 1
    elif isinstance(arg, str):
        return int(arg) + 1
    elif isinstance(arg, list):
        return list(map(foo, arg))

print(foo(2))
print(foo("2"))
print(foo([2, 3]))

# Ejercicio: funcion factorial
# factorial(6) = 6 * 5 * 4 *... *1
print()
def factorial(x):
    print(x)
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

x = 3
print("El factorial de", x, "es" ,factorial(x))