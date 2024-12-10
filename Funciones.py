print("PITO jijijijiijijiji")
##Vamos a crear funciones en este apartado con el fin de facilitar el codigo, hacerlo más simple y adecuado a lo que se pide.

def imprimir_impares(lista_de_numeros):
    for num in lista_de_numeros:
        if num % 2 != 0:
            print(str(num))
            
##Esto siempre va a imprimir lo que este en la funcion y lo que nosotros llamamemos. Es importante tener en cuenta que siempre
##SIEMPRE, SIEMPRE va a aparecer el def

##def es una abreviacion de definicion - def   inicion


##Para invocar a las listas, es necesario poner el nombre de la funcion -> nombre_funcion (argumento...n)
lista = [1,2,3,4,5,6,7,8,9,10]
imprimir_impares(lista) ## Es como java, haces el método imprimir_impares() y añades la nueva lista/argumento
print(" ")
##Si ponemos esto asi, saldrá este el error ----- imprimir_impares()


##Definición de argumentos: 
def imprimir_saludo():
    print("Hola")

imprimir_saludo()
print(" ")

##Definición de varios argumentos de entrada

def varios_argumentos(a, b):
    return a + b

resultado = varios_argumentos(3, 2)
print("El resultado de la suma de 3+2 es igual a: " +str(resultado))

##Documentacion de funciones:
def doc_funcion ():
    """
    A través de esto, lo que se hace es documentar una funcion determinada
    es decir, añadimos información sobre los diferentes items y puntos a
    tener en cuenta con el objetivo de documentar todo
    """
help(doc_funcion) ##Para poder explicarla, tendremos que poner help()

##En python, los datos primitivos como son el numero entero, un caracter o un flotante pasan por VALOR
##Pero las listas, tuplas y diccionarios... se actualizan y pasan por REFERENCIA

##Hasta ahora, hemos venido trabajando funciones como entidades al igualarlas 

def sumar_elementos (list_numeros):
    return sum(list_numeros)

lista = [1,2,3,4,5,6]
resultado = sumar_elementos(lista) ##Aqui estamos igualando una entidad a la funcion

print("El resultado de sumar todos y cada uno de los elementos de la lista, es igual a: " +str(resultado))


##La utilidad de las funciones lambda se lleva a cabo para argumentar información:

# Lista de ejemplo
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares usando una función lambda
pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
print("Números pares:", pares)

# Filtrar números impares usando una función lambda
impares = list(filter(lambda x: x % 2 != 0, lista_numeros))
print("Números impares:", impares)


##Scope




    


