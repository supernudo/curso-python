
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
month = month % 12
print("{:4}-{:02}-{:02}".format(year, month, day))
print(str(year) + "-" + str(month) + "-" + str(day))

# 6* Calcular si un año es bisiesto
print()
print("6* Calcular si un año es bisiesto")
print("---------------------------------")
foo = 2018
print(foo, "NO es un año bisiesto" if foo % 4 else "es un año bisiesto")

# 7* Convierte una cadena DNA en RNA
print()
print("7* Convierte una cadena DNA en RNA")
print("----------------------------------")
foo = "DNA"
print("The DNA and " + foo.replace("D", "R") +
" are responsible for the storage and reading of genetic information")

# 8* Cuanta el numero de veces que se repite una letra
print()
print("8* Cuanta el numero de veces que se repite una letra")
print("----------------------------------------------------")
foo = "supercaliofragilisticoespialidoso"
bar = "s"
print(foo, "tiene", foo.count(bar), "letras", bar)

# 9* Encontrar una palabra dentro de una frase
print()
print("9* Encontrar una palabra dentro de una frase")
print("--------------------------------------------")
foo = "Joe, peazo invento esto de la Gaseosa"
bar = "Gaseosa"
print("La palabra", "\"" + bar + "\"", "esta" if foo.find(bar)!= -1
else "NO esta", "en la frase:", "\"" + foo + "\"")

# 10* Intenta responder a una pregunta
print()
print("10* Intenta responder a una frase")
print("---------------------------------")
print("¿Cual es el sentido de la vida, el Universo y todo lo demás?")
foo = "42"

if int(foo) == 42:
    print(foo, "realmente ES la respuesta")
elif int(foo) == 43:
    print(foo, "realmente casi ES la respuesta")
else:
    print(foo, "realmente NO ES casi la respuesta")
