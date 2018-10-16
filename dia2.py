
# 1* Palindromo
print()
print("1* Palabra palindroma")
print("---------------------")
#input = "abcba"
foo = "abcde"
if foo == foo[::-1]:
    print("palindromo! :)")
else:
    print("no palindromo :(")



# 2* Numero capicua
print()
print("2* Numero capicua")
print("-----------------")
#foo = 234
foo = 555
# Optimizacion al utilizar str una sóla vez
bar = str(foo)
print(foo, "es capicua! :)" if bar == bar[::-1] else "no capicua :(")

# 3* Caracteres diferentes de dos cadenas
print()
print("3* Caracteres diferentes de dos cadenas")
print("---------------------------------------")
foo = "abd"
bar = "abcd"

# foo debe ser la cadena más larga
if len(bar) > len(foo):
    tmp = foo
    foo = bar
    bar = tmp

counter = 0
found = False
for i in foo:
    print(i)
    for j in bar:
        print(i, j)
        if i == j:
            found = True
    if not found:
        counter = counter + 1
    found = False

print(counter)
print()


counter = 0
found = False
for i, j in zip(foo, bar):
    print("con zip", i, j)
    if i != j:
        counter += 1

print(counter)

# 4* Dia mes año
print()
print("4* Imprimir el numero de un mes")
print("-------------------------------")
dic = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6, "jul": 7,
"ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}
foo = "enero"
print (foo, "es el mes número", dic[foo[:3]])

# 5* Sumar mes a una fecha en formato YYYY-MM-DD
print()
print("5* Sumar mes a una fecha en formato YYYY-MM-DD")
print("----------------------------------------------")
foo = "2018-12-01"
year, month, day = int(foo[:4]), int(foo[5:7]), int(foo[-2:])
print(year, month, day)
month += 1
month = (month ) % 12
print("{:4}-{:02}-{:02}".format(year, month, day))
print(str(year) + "-" + str(month) + "-" + str(day))
