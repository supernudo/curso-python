
# Classes II

# Herencia
# Permiter reutilizar codigo, no sirve para herencia de tipos?
# La funcion print puede se diferente en un CLI o GUI

class A:

    def __init__(self):
        self.a = 0

    def func(self):
        print("Estoy en A")

a = A()
a.func()

# Herencia de A en B
# Funciona muy parecido a C++
# __init__ no es el constructor, es __new__
class B(A):

    def __init__(self):
        super(B, self).__init__()
        self.b = 1
print()
b = B()
b.func()
print(b.a)

class A:

    def __init__(self):
        print("init A")
        self.f()

    def f(self):
        print("A.f()")

class B(A):

    def __init__(self):
        # Super evita el problema del diamante
        #super(B, self).__init__() # Python 2.x
        super().__init__() # Python 3.x
        print("init B")
        self.f()

    def f(self):
        print("B.f()")

# No funciona como en C++, C# o Java:
# init A
# A.f()
# init A
# A.f()
# init B
# B.f()
# Porque B esta llamando self.f()
# NO interesa replicar el comportamiento de C++, C# o Java
print()
A()
B()

# La herencia en Python permite reutilizar codigo, no sirve para herencia
# de funcioes, el polimorfismo es implicito en Python

class A:

    def __init__(self):
        self.a = 0

    def func(self):
        print("Estoy en A")

class B(A):

    def __init__(self):
        super(B, self).__init__()
        self.b = 123
    def func(self):
        print("Estoy en B")
    #def __str__(self):
    #    # Todos las clases tienen el metodo __str__
    #    return str(self.b)

print()
b = B() # Instacia de la clase B u objeto de la clase B
print(b)

# Redefinicion de operadores
# Se pueden redefinir todos los operadores
# Tambien crear nuevos pero no facilmente
class Integer:

    def __init__(self, a):
        self.value = a
    def __add__(self, other):
        return self.value - other.value
    def __mul__(self, other):
        return self.value % other.value

print()
a = Integer(10)
b = Integer(2)
# Si a o b no fueran instancias de la clase Integer no contendrian .value
# y no funcionaria
print(a + b)
print(a * b)

# Ejercicio: clase String que se sume con ella misma y con los strig de python
# Al sumar primero pruba a (add) b y luego b (radd) b
class String:

    def __init__(self, value):
        self.value = str(value)
    def __add__(self, other):
        if isinstance(other, str):
            return self.value + other
        if isinstance(other, int):
            return self.value + str(other)
        else:
            return self.value + other.value
    def __radd__(self, other):
        if isinstance(other, str):
            return self.value + other
        if isinstance(other, int):
            return  str(other) + self.value
        else:
            return  other.value + self.value

print()
a = String("hola")
b = String("2")
print(a + b)
print(a + " hola que tal")
print(a + 1)
print(1 + a)

# Modulos
# Ficheros y directorios empaquetados
# Contienen clases y funciones
# Python puede ejecutar código cuando importas un modulo
# El código a ejecutar se mete en el fichero __init__.py
# En el init se realizan ciertas comprobaciones, las dependencias con el OS
# (bloqueos, ...)
# Es más facil buscar un módulo existente que me de la solucion
# que implementar la solución --> "import easy"

# Importar modulos: 3 formas
#import OS
#from OS import path
#import os.path as osp

# Modulos más utilizados
# Modulo "re"
print()

from re import match, search, findall
texto = "Vamos con afán todos a la vez a buscar con ainco las bolas de dragón"
if match("Vamos", texto):
    print("Empieza por 'Vamos'")

if search("afán", texto):
    print("Contiene 'afán'")

print(findall(" ([a-zA-Z]{3}) ", texto))

# Las expresiones regex son costosas en ejecución porque por debajo se genera
# el código fuente equivalente
# Si se va a utilizar una expresión regex muchas veces mejor hacer un compilado

import re
pattern = re.compile(" ([a-zA-Z]{3}) ")
if (pattern.search("Vamos con afán")):
    print("Empieza por 'Vamos con afán'")

# Modulo "time" (pegado al HW)
# Modulo "datetime" (formato humano)

from time import gmtime, strftime, strptime
t = gmtime()
print()
print(t)
print(strftime("%a, %d %b %Y %H:%M:%S +0000", t))
#print(strftime("30 Nov 00", "%d %b %Y"))

# repr() saca un string leible por python (ctr-c, ctrl-v)
from datetime import datetime
print(datetime.now())
#print(datetime.strptime())
#print(repr())

# Modulo "math"
# 0.1 x 10 = 0.999999999999999999999999
# Esto es por el formato que utiliza para optimizar en velocidad de los float
# se da la precisión máxima del sistema 0.99999999 para un PC es lo mismo que
# 1.0

from math import fsum, exp, log, tan, atan
print(log(exp(2.53)))

# No da exacto por que hay muchas operaciones intermedias que acumulan error
print(tan(atan(1.71)))

# Modulo "intertools"
# Creación, manipulación y combinación de iteradores
# El generador es un iterador

from itertools import chain, product
print(list(chain("ABC", "DEFG")))
print(list(product("123", "ABC"))) # Saca todas las combinaciones posibles

# Modulo functools
# Sirve para manejar funciones, funciones que operan sobre funciones - decoradores

# Patron de diseño memorize
# Funcion que tarda mucho en devolver y la llamo aleatoriamente, varias veces
# Memoriza los resultados anteriores
# Ejemplo: pagina web cacheada

#from functools import lru_cache, partial
#@lru_cache(maxsize=1024)

# Inciso sobre decoradores
# Son envoltorios de funciones
# No utlizar para valores random o funciones que pueden retornan diferetes
# valores para mismos parametros de entrada
# Ejemplo: get_time() devolveria simpre lo de la primera llamada

def decorador(f):
    def wrap():
        print("Modificado")
        f()
    return wrap

@decorador
def f():
    print("....")

print()
f()

# Es equivalente
print()
def f():
    print("....")

new_f = decorador(f)
new_f()









