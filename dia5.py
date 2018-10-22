
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




