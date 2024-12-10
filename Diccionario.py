## Los diccionarios es una estructura de datos en forma de tabla
dict_1 = {}
##Un ejemplo
clave_1 = "a"
valor_1 = 1
clave_2 = "b"
valor_2 = 2
dict_2 = {"clave_1" : "valor_1",
          "clave_2": "valor_2"}

print("Esto es un diccionario " +str(dict_1))

dict_1["k2"] = (1,2,3)
print("dict_1: " +str(dict_1))

##Importante a tener en cuenta en relación a los diccionarios
##Tienen len, para valorar la cantidad de claves que tienen
print(len(dict_1)) ##Saldrá 1 al tener 1 sola llave
##Tienen values, que nos servirá para obtener los valores del diccionario (metodo values())
print("Valores de " +str(dict_1) + " : " +str(dict_1.values()))
##Podemos utilizar el in y el not in para saber si una clave está en el diccionario
# Ejemplo con `in`
diccionario = {'a': 1, 'b': 2, 'c': 3}
print('a' in diccionario)  # True
print('d' in diccionario)  # False

# Ejemplo con `not in`
print('d' not in diccionario)  # True
print('a' not in diccionario)  # False

# Ejemplo con `iter`
diccionario = {'a': 1, 'b': 2, 'c': 3}
iterador_claves = iter(diccionario)

print(next(iterador_claves))  # 'a'
print(next(iterador_claves))  # 'b'
print(next(iterador_claves))  # 'c'

# También puedes iterar sobre los valores o los items (pares clave-valor)
## Para ello, podemos usar la función iter
iterador_valores = iter(diccionario.values())
iterador_items = iter(diccionario.items())

print(next(iterador_valores))  # 1
print(next(iterador_items))    # ('a', 1)

# Ejemplo con `clear` para limpiar el diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario.clear()
print(diccionario)  # {}

# Ejemplo con `copy`
diccionario_original = {'a': 1, 'b': 2, 'c': 3}
diccionario_copia = diccionario_original.copy()
print(diccionario_copia)  # {'a': 1, 'b': 2, 'c': 3}

# Modificar la copia no afecta al original, con copy llevamos a cabo una copia del diccionario
diccionario_copia['d'] = 4
print(diccionario_original)  # {'a': 1, 'b': 2, 'c': 3}
print(diccionario_copia)     # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Ejemplo con `del` nos servirá para eliminar una función en concreto
diccionario = {'a': 1, 'b': 2, 'c': 3}
del diccionario['b']
print(diccionario)  # {'a': 1, 'c': 3}

# También puedes usar `del` para eliminar todo el diccionario
del diccionario
# print(diccionario)  # Esto dará un error porque 'diccionario' ya no existe


##Diferencia entre los set (conjunto) y los diccionarios
## Es importante tener en cuenta que un set va a tener un valor, mientras que el diccionario necesita de un 
## atributo para darle un valor, la expresión es la misma, pero esa es la diferencia, ejemplo: 

##Un set (conjunto) - como ves, tiene los valores, no necesita de atributo ni nada
nombres = {"Alice", "Bob", "Charlie"}
nombres.add("David")
print(nombres)  # {'Alice', 'Bob', 'Charlie', 'David'}

##Un diccionario - necesita de unos atributos y unos valores para poder acceder a ellos, fijate en los dos :
agenda = {'Alice': '123-456', 'Bob': '789-012'}
agenda['Charlie'] = '345-678'
print(agenda)  # {'Alice': '123-456', 'Bob': '789-012', 'Charlie': '345-678'}

##A modo de resumen
##AL igual que ocurre con los diccionarios, nos encontramos con funciones como:
# in, not in, len

##Un elemento disjunto, es un elemento que no tiene nada en común
fans_gym = {"Felix" , "Pepe"}
fans_crossfit = {"Josue" , "Antonio"}
##¿Coincide alguno?? no, al aplicar isdisjoint hablamos de que son disjuntos, diferentes, por eso es true
print(fans_gym.isdisjoint(fans_crossfit))

##Cambiamos el ejemplo
fans_gym1 = {"Felix" , "Josue"}
fans_crossfit1 = {"Josue" , "Antonio"}
##¿Coincide alguno?? si, al aplicar isdisjoint hablamos de que son disjuntos pero coincide Josue, por eso es false
print(fans_gym1.isdisjoint(fans_crossfit1))

##Si hablamos de subconjunto
fans_lobezno = {"Churre", "Fer"}
fans_marvel = {"Alfredo" , "Garaba" }
print(fans_lobezno.issuperset(fans_marvel))

##Union
print(fans_lobezno.union(fans_marvel))

##Inteserccion - los que coinciden
print(fans_lobezno.intersection(fans_marvel)) ##Saldrá vacío set(), no coincide ninguno

##Diferencia - los que no están en uno ni en el otro
fans_lobezno1 = {"Churre", "Fer" , "Alfredo" , "Garaba"}
fans_marvel1 = {"Alfredo" , "Garaba" }
print(fans_lobezno1.difference(fans_marvel1))
print(fans_lobezno1 - (fans_marvel1))

## Esto nos muestra los que no están, se puede usar .difference y el menos (-), arriba los dos ejemplos







