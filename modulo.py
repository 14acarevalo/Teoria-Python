##Los modulos, nos permiten importar clases procedentes de otros tipos

##La más conocida es math - para operaciones matemáticas

##Ten en cuenta que puedes importar cualquier clase con import y añadiendo el nombre de la clase de python import ejemplo.py

import math

import math
print(math.ceil(4.2))  # Salida: 5
##Este ejemplo, lo que hace es redondear hacia arriba el más cercano

import math
print(math.floor(4.7))  # Salida: 4 
##Redondea hacia abajo, el más cercano

import math
print(math.trunc(4.9))  # Salida: 4
##Elimina la parte decimal

import math
print(math.pow(2, 3))  # Salida: 8.0
##Eleva la potencia

import math
print(math.sin(math.pi / 2))  # Salida: 1.0
##Devuelve el seno

import math
print(math.sqrt(16))  # Salida: 4.0
##Este lo que hace es sacar la raiz cuadrada del número

import math
print(math.asin(1))  # Salida: 1.5707963267948966
##Devuelve el arcoseno

import math
print(math.acos(0))  # Salida: 1.5707963267948966
##Devuelve el arco coseno

import math
print(math.atan(1))  # Salida: 0.7853981633974483
##Devuelve el arco tangente

##Ejemplos:
print("Vamos hacia arriba, ya que el número original es 5.1 utilizando math.ceil: ")
print(math.ceil(5.1))
print("Vamos hacia abajo, ya que el número original es 5.9, utilizando math.floor: ")
print (math.floor(5.9))
print("Vamos a eliminar el decimal, pasando de 5.7 a, utilizando math.trunc: ")
print(math.trunc(5.7))
print("Vamos a utilizar potencias, el primer número es el que usaremos para trabajar sobre este, el segundo será el número de veces que lo vamos a multipicar por si mismo ")
print(math.pow(2, 4))
print("Vamos a sacar la raiz cuadrada del número 28: ")
print(math.sqrt(28))
print("Vamos a sacar la raiz cuadrada del número 16: ")
print(math.sqrt(16))

print("")
##Ejercicios: 

##Ejercicio 1: Redondeo
##Escribe un programa que lea un número decimal del usuario, y luego imprima:
##El número redondeado hacia arriba usando math.ceil.
##El número redondeado hacia abajo usando math.floor.
##El número truncado usando math.trunc

numero = 5.7
print("Ejercicio 1- En este ejercicio, vamos a realizar un redondeo hacia arriba, hacia abajo y eliminaremos el decimal: " +str(numero))
print(f"En primer lugar vamos a intentar sacar el redondeo hacia arriba del numero {numero}, siendo este: {math.ceil(5.7)}")
print(f"En segundo lugar, vamos a realizar el redondeo hacia abajo del numero {numero}, siendo este: {math.floor(5.7)}")
print(f"En último lugar, vamos a proceder a eliminar el decimal del numero {numero}, siendo este: {math.trunc(5.7)}")
print(" ")
##Ejercicio 2: Potencias y Raíces
##Escribe un programa que calcule:
##La potencia de un número dado, x^y, usando math.pow.
##La raíz cuadrada de un número dado usando math.sqrt.

print("Ejercicio 2 - En este programa lo que se busca es trabajar con potencias y raices, asi que vamos allá!!! ")
print(f"La potencia del número 2, es igual a:  {math.pow(2, 3)}")
print(f"La raiz cuadrada del número 16, es igual a: {math.sqrt(16)}")
print("")

print("Variante ejercicio 2: ")
number = int(input("Usuario, introduce un número: "))
elevado = int(input("¿A cuanto lo vas a elevar?: "))
numberRaiz = int(input("Introduce un número para llevar a cabo su raíz cuadrada: "))
print(f"La potencia del número {number} elevada a {elevado} es igual a {math.pow(number, elevado)}")
print(f"La raiz cuadrada del numero {numberRaiz} es igual a: {math.sqrt(numberRaiz)}")

import random 
##Hablamos de cosas aleatorias

from random import random, seed

seed(0) ##Esto nos sirve a nosotros para introducir los numeros aleatorios siempre fijos

for i in range(4):
    print(random())
    
from random import random, seed


for i in range(4):
    print(random())



