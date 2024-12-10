a = "Comienzo"
print (a)
"""Tienes que darle a run Python file """
"""puedes crear un atajo para que sea más fácil de ejecutar """
"""te recomiendo ponerle ctrl + p + p """

print (\
    "Linea demasiado larga\
       lo podemos dividir asi ")

b = "otra variable"
c =10

print (b)
print (" ")
print (c)

b = "abcd"
print ("Ahora b vale: " +b)

#Como puedes observar, puedes igualar el valor de varias variables
a = b = c = d = e = 20

print(a + b + c + d)

#Como puedes observar, puedes asignar diferentes valores como si fuera un array

a , b , c , d = 1, "alberto" , True , 20

print (a)
print (b)
print (c)
print (d)

z = None
print (z) #Esta variable estaria vacia por tener None

#Una variable jamás podrá empezar con un número, ejemplo
# 1var = 10; Si borras el comentario verás que sale un error
var1 = 10
var_1 = 10

#Si queremos concatenar un valor a tipo string, tendremos que poner str(nombre de la variable)

variableInt = 14
variableString = "20"

print ("La variable se convierte en string " +str(variableInt))
print("Ejemplo, como son strings no se van a sumar, pero " +variableString + " + " +str(variableInt)+ " no se suman, son strings")

#Para valorar el tipo de variable, utilizaremos

numero = 10
numero2 = 10.2
numero3 = 10+10j

print ("Este número es: " +str(numero)+ " " +str(type(numero)))
print ("Este número es: " +str(numero2)+ " " +str(type(numero2)))
print ("Este número es: " +str(numero3)+ " " +str(type(numero3)))

# Operandos que tenemos que tener en cuenta 

g = 10
h = 2
print ("Suma de " +str(g)+ " + " +str(h)+ " = " +str(g+h))
print ("Resta de " +str(g)+ " - " +str(h)+ " = " +str(g-h))
print ("Multiplicacion de " +str(g)+ " x " +str(h)+ " = " +str(g*h))
print ("Division decimal de " +str(g)+ " / " +str(h)+ " = " +str(g/h)) #Como puedes observar, aqui se verá 5.0
print ("Divison entera de " +str(g)+ " // " +str(h)+ " = " +str(g//h)) #Como puedes observar, aqui se verá 5
print ("Modulo de " +str(g)+ " % " +str(h)+ " = " +str(g%h))
print ("Potencias de " +str(g)+ " pow " +str(h)+ " = " +str (pow(h, g)))
print ("Potencia 2.0 de " +str(g)+ " ** " +str(h)+ " = " +str(h**g))

print (" ")
print ("Para concatenar variables")

k = 10
w = "10"
suma = k + int(w)
print ("Vamos a pasar la variable g a int " +str(int(w)))
print ("Una vez concatenadas, vamos a realizar una suma " +str(suma))

#Para importar una libreria

import math







