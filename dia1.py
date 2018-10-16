
# hola
lista = [1, 2, 3, 4, 5, 6]
var = "hello world!!"
print(var, lista)
print("hello world"[0:3])
print(var[0:3], var[3:])
print(var[0:7:2])
print(lista[::-1])
print(var[::-1])

var = "abcdefghijk"
lista = [1, 2, 3, 4]

# == comprueba en memoria
if var == "abcdefghijk"[0:]:
    print("True")
else:
    print("False")

# is comprueba la naturaleza tambien, tiene la misma dirección de memoria
var = None
if var is not None and True or False:
    print("True")
else:
    print("False")


for i in range(3, 10, 2):
    print(i)

var = "abcdefghijk"
for i in var:
    print(i, end='')
print()


for i in var:
    if i == 'h':
        continue
    print(i, end='')


lista = list(range(10))

for i in lista:
    if not(i%2):
        print(i)

print(lista[::2])

## Diccionarios
# keys: numeros, caracteres y tuplas (1, 2, 3)
# listas son no hasheables [1, 2, 3]
# tuplas, listas "read only"
d = {"edad": 40, "direccion": "Alcalá de Henares"}
print(d["edad"])

str1 = "a"
str2 = "b"

lst1 = [1, 2]
lst2 = [2, 3]

dic1 = {"a": 1}
dic2 = {"a": 2, "b": 3}

print(str1 + str2)
print(lst1 + lst2)
#print({**dic1 + **dic2})
dic1.update(dic2)
print(dic1)

dic2.update(dic1)
print(dic1)