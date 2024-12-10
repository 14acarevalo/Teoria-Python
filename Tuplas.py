## Tuplas ##

##Una tupla se define como un conjunto de valores, es muy parecido a la lista, pero cambia la forma en la que se desarrolla
##La diferencia fundamental de tupla a lista, es que la tupla no se va a poder modificar NUNCA el valor de dicha tupla

my_tuple = tuple()
my_other_tuple = () ##Diferencia entre tupla y lista, los parentesis

my_tuple = (30, 1.85, "Alberto", "Campanero", "Alberto") 
print(my_tuple)
print(type(my_tuple))

##Vamos a solicitar ciertos datos de mi tupla anterior
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1])
print(my_tuple[2])
##print(my_tuple[6]) ##Será un error porque en mi tupla anterior no hay 6 caracteres - IndexError

print(my_tuple.count("Alberto")) ##Contará las veces que esta este valor
print(my_tuple.count("Arevalo"))
print(my_tuple.count("Campanero"))

print(my_tuple.index("Campanero")) ##Indice, posicion
print(my_tuple.index("Alberto")) ##Encuentra el primero

my_other_tuple = (22, 184, "Pablo", "Campanero")
my_tuple2 = my_tuple +my_other_tuple
print(my_tuple2)

##Las tuplas no se pueden modificar, insertar, ni eliminar datos NO SON INMUTABLES, lo que podemos hacer como se ve aqui es fusionarlas
##Si queremos que una tupla sea mutable, tendremos que fusionarlas

print(my_tuple[1 : 3]) ##Va a imprimir los elementos que se encuentran en ese intervalo

##Vamos a convertir tuplas en listas

conversion = list(my_tuple)
print(type(conversion))

conversion[4] = "Arevalo"
print(conversion)
conversion.insert(2, 1.86)
print(conversion)


##Ahora lo pasamos a tupla
conversion = tuple(conversion)
print(type(conversion))
##Si quieres cambiar una tupla, pasala a lista y despues a tupla

del conversion ##Aqui lo que hacemos es quitar la definición de la tupla

##Desempaquetando tuplas

creamos_tupla = ("Alberto", 30, 1.85, "Coordinador Deportivo")
nombre, edad, estatura, trabajo = creamos_tupla

print(nombre)
print(edad)
print(estatura)
print(trabajo)