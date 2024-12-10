#En este apartado, vamos a trabajar con las listas de python

empty_list = [] ## Este seria el claro ejemplo de una lista vacia
print(empty_list)

list_1 = [1,2,3,4,5,6]
print(list_1)

list_2 = ["Alberto" , "Fernando" , "Isabel" , "Pablo" , "Sandra" , "Maxima"]
print(list_2)

list_3 = ["Alberto" , 1 , "Sandra" , 2 , "Coche" , 3 ]
print(list_3)

list_4 = [str(list_1) + str(list_2) + " Isabel" , 4 , "Fernando" , True , "Maxima"]
print(list_4)

list_5 = list('abcd') ##Con este comando transformamos un código en una lista
print(str(list_5))

print(list_3 *3) ##Con esto vamos a multiplicar nuestra lista por el número de veces que queramos, en este caso 3

##Para trabajar con valores númericos, el orden, ver el más grande, más pequeño... tenemos unos comandos
## len(list) - sacará la longitud de la lista
## max(list) - sacará el valor más grande
## min(list) - sacará el valor más pequeño
## list(seq) - 

print("La longitud de la lista 3 es igual a: " +str(len(list_3))) ##Con valores númericos hace falta el str
print("El valor más pequeño de la lista 2, es igual a: " +min(list_2)) ##Con valores string NO hace falta el str
print("El valor más grande de la lista 1, es igual a: " +str(max(list_1))) ##Valor númerico el cual hace falta el str
print("El valor más grande de la lista 2, es igual a: " +max(list_2)) ##Con valores string NO hace falta el str

##Importante tener en cuenta que cuando se mezclan valores int, string... se lia un poco todo y no funciona

##Vamos a trabajar con otros comandos
## mi_lista.append("e") añade ese valor al final de la lista
print(str(list_1))
list_1.append(14)
print(str(list_1))
list_1.append([1,2,3,4,5,6,7,8]) ##En caso de listas, usaremos este
print(str(list_1))

##extend
list_1.extend([1,2,3,4,5,6,7,8]) ##Pero si nosotros queremos extender los valores, es decir, meter varios, usamos esto
print(str(list_1)) 
##insert - con este comando lo que vamos a hacer es añadir un elemento por otro pero jugando con la posicion como el array
list_1.insert(1, 99)
print(str(list_1))
list_1.insert(2, 37)
print(str(list_1))

## remove va a eliminar
list_1.remove(4)
print(str(list_1))
## pop va a ser eliminar, pero eliminará la posicion, es decir, el indice

list_1.pop(0)
print(str(list_1))

## clear, va a limpiar la lista entera
list_45 = [1,2,3,4,5,6]
print (str(list_45))
list_45.clear()
print(str(list_45))

##count nos va a servir para contar las veces que se repite un parametro
contador = list_1.count(3)
print(str(contador))


