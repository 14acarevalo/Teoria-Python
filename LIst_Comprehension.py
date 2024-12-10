##Estas listas se convierten en una forma elegante de crear y definir listas basadas en otras existentes
##Evita lineas muy largas para que el codigo sea facil de leer

nums = range (1, 20)
odds = []
for numero in nums:
    if numero % 2 != 0:
       print(str(odds.append(numero)))
       print(str(numero))
        
odds = [numero for numero in nums if numero %2 == 0]
print("Los numeros pares son: " +str(odds))

list_numeros = [1,2,3,4,5,6,7,8,9,10]

new_list = [numero1 for numero1 in list_numeros ]
for numero1 in new_list:
    print(str(numero1))

print(" ")
##Parte práctica para empezar a asimilar los ejercicios de list_comprension

##Ejercicio 1 - Dada una lista de números, crea una nueva lista que contenga el cuadrado de cada número.

list_nueva = [1,2,3,4,5,6,7,8,9,10]
print("Lista con valores nuevos")
crear_lista = [number for number in list_nueva]
for number in crear_lista:
    print(str(number))
print(" ")

##Aqui hemos creado la lista normal y corriente, pero vamos a trabajar sobre ella, para duplicar su valor
list_nueva = [1,2,3,4,5,6,7,8,9,10]

crear_lista = [number*2 for number in list_nueva]
for number in crear_lista:
    print(str(number))
    
print(" ")
##Ahora vamos con sacar los numeros pares con un valor normal y un valor doble
list_nueva = [1,2,3,4,5,6,7,8,9,10]
print("Numeros pares: ")
crear_lista = [number for number in list_nueva if number % 2 == 0]
for number in crear_lista:
    print(str(number))
print(" ") 
  
print("Numeros pares con valor doble: ")
list_nueva = [1,2,3,4,5,6,7,8,9,10]

crear_lista = [number*2 for number in list_nueva if number % 2 == 0]
for number in crear_lista:
    print(str(number))
print(" ")    
##Vamos a crear listas con el valor/longitud de sus palabras: 
list_palabras = ["Alberto" , "Sandra" , "Pablo" , "Fernando" , "Isabel" , "Familia"]
new_list_palabras = [palabra for palabra in list_palabras]
for palabra in new_list_palabras:
    print(f"La longitud de la palabra {palabra} es: " )
    print(len(palabra))
print(" ")

##Vamos a pasar en una nueva lista, palabras de minuscula a mayuscula
list_palabras_minuscula = ["alberto" , "sandra" , "pablo" , "fernando" , "isabel" , "familia"]
conversion_mayusuculas = [conversion.upper() for conversion in list_palabras_minuscula]
for conversion in conversion_mayusuculas:
    print(f"La palabra {conversion} convertida a mayusculas, queda asi: " +conversion)
print(" ")

##Imprimir números mayores que 5
list_actualizada = [1,2,3,4,5,6,7,8,9,10,1, -1, 4, 6, 4, 3]
list_mayor5 = [numeros for numeros in list_actualizada]
for numeros in list_mayor5:
    if numeros >= 5:
        print(str(numeros))


##List comprension sirve basicamente para hacer una lista a partir de otra, nada más

##Sigamos practicando y aprendiendo 
comienzo = [x for x in range (10)]
print("En esta lista vamos a sacar números del 0 al 9: " +str(comienzo))

pares = [condicion for condicion in range (0, 11) if condicion % 2== 0]
print("Sacamos todos los pares de una lista del 0 al 11: " +str(pares))

cuadrado = [alberto**2 for alberto in range (0,11)] ##como puedes observar, puedes poner el nombre que quieras a la condicion
print("En esta lista vamos a sacar los cuadrados de una serie de números comprendidos entre 0 y 10: " +str(cuadrado))

##Vamos a mezclar las últimas condiciones/supuestos:

mezcla = [condicion**2 for condicion in range (0, 11) if condicion%2 != 0]
print("En esta opcion, vamos a sacar los impares dentro de un bucle del 0 al 10, pero sacando su cuadrado" +str(mezcla))

##Vamos a meter una multiple condicion

multipleCondicion = [ (x,y) for x in range (1,10) for y in range (1,5)]
print("En esta salida, obtendremos como se convinan los números dentro de cada rango e intervalo: " +str(multipleCondicion))

multipleCondicion2 = [(x,y,z) for x in range (1, 3) for y in range (4,6) for z in range (7, 9)]
print(multipleCondicion2)
##Y asi infinitas veces con el objetivo de sacar esos intervalos y esas condiciones dentro de el rango especificado


##Vamos a sacar unas listas algo más complejas

palabras = ["alberto" , "estudiar" , "python"]
inicial = [letra[1] for letra in palabras]
print("Sacamos la segunda letra de cada una de las palabras de nuestra lista de palabras" +str(inicial))


