

# Modulos (continuacion)

# Modulo OS

import os
from os.path import join, getsize
for root, dirs, files in os.walk('./'):
    print(root, dirs, files)

# Modulo 'subprocess'
# Permite llamar a programas nativos (C, system, Windows, Linux,...)
from subprocess import Popen, PIPE
#process = Popen(['C:\Windows\System32\cmd.exe', 'dir'], stdout=PIPE)
#stdout, stderr = process.communicate()
#print(stderr)
#print(stdout)

# Bases de datos
# SQL es un lenguaje de programación para programar bases de datos SQL
# Cumple: Atomicidad, consistencia independencia, durabilidad
# No cumple: disponibilidad
# NoSQL
# Cumplen 2 de 3 CAP: consistencia, disponibilidad y particioado

# Base de datos 'sqlite3'
# Todas las bbdd optimizan velocidad no espacio

print()
print("SQLITE: guardar en BBDD")

import sqlite3
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

sql_command = """
CREATE TABLE employee (staff_number INTEGER PRIMARY KEY, fname VARCHAR(20),
lname VARCHAR(30), gender CHAR(1), joining DATE, birth_date DATE);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO employee (staff_number, fname, lname,gender,
birth_date) VALUES (NULL, "Williams", "Shakespeare", "m", "1961-10-25");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO employee (staff_number, fname, lname, gender,
birth_date) VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");"""
cursor.execute(sql_command)

for i in range(10):
    cursor.execute(sql_command.replace("Frank", "Frank " + str(i)))

connection.commit()
connection.close()

print()
print("SQLITE: leer en BBDD")

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM employee")
print()
print("fetch all:")
result = cursor.fetchall()
for r in result:
    print(r)

cursor.execute("SELECT * FROM employee")
print()
print("fetch one:")
result = cursor.fetchone()
for r in result:
    print(r)

cursor.execute("""DROP TABLE employee""")
print()
print(result)

