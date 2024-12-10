##En este bloque vamos a aprender logica, con bucles, con if-else, elif...
##elif nos va ayudar a meter varias veces que pasaria si esto no es asi

variablePrueba1 = 5
variablePrueba2 = 6

if variablePrueba1 > variablePrueba2 :
    print("La segunda variable es más pequeña")
else :
    print("La primera variable es más pequeña")
print(" ")
    
## es importante meter un tabulador para dejar ese espacio (4 espacios) y que se vea visualmente

var_1 = 14
var_2 = 21

##Varias condiciones, si esto no es asi, puede ocurrir esto, que no, puede ocurrir esto otro...
if var_1 < var_2 :
    print("Esta condicion nos indica que la variable 2 es más grande que la 1")
    print("Tambien nos indica que el valor de la variable 2, " +str(var_2)+ " es mayor que el valor de la variable 1, " +str(var_1))
    print("Y con ello, podemos observar como esta condicion si se cumple")
elif var_1 == var_2:
    print ("Podemos observar como no hay ninguna variable del mismo tamaño")
    print(" Es decir, ambas variables son iguales")
elif var_1 > var_2:
    print("En este caso, ocurre todo lo contrario, la variable 1 es mayor que la 2")
print(" ")

##Vamos a comprobar si una de las variables cumple con la condición a través del or
var_3 = 4
var_4 = 5
var_5 = 6

if var_3 > 5 or var_4 > 5 or var_5 > 5 :
    print("Existe una variable mayor que 5")
else :
    print("Las variables no son mayores que 5")
print(" ") 

##Vamos a comprobar si las variables cumplen con la condición, todas, con el and
if var_3 >5 and var_4 >5  and var_5 > 5:
    print("Todas las variables son mayores que 5")
else :
    print("Las variables no son mayores de 5 ") 
print(" ")  

## Varias condiciones a tener en cuenta:

if (var_3 or var_4) >6 or var_5 > 6 :
    print("Premio, alguna de las variables son más grandes que 6")
elif  var_3  > 7 or (var_4 or var_5) > 7 :
    print("Alguna de las variables son mayores que 7")
elif (var_3 or var_4) >5 or var_5 > 5 :
    print("Alguna de las variables es mayor que 5 ")
else :
    print("No se cumple nada de lo propuesto")
    
## Vamos con más condiciones
print ("Buenos días usuario ")
mi_cadena = input("")
if "hola" in mi_cadena:
    print("Gracias por saludarme")
elif "adios" in mi_cadena:
    print("Que tengas un buen día")
    
    
##El bucle for nos va a permitir recorrer un bucle completo
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in lista_numeros :
    if numero > 5:
        print(numero)

print(list(range(5))) ## Una lista para ir del 0 al 5

print(list(range(1,5))) ## Una lista para ir de un numero al otro

print(list(range(1, 30, 5))) ##Al añadir el tercer número, los saltos entre estos van a ser de 5

print(list(range(20, 0, -1)))

##List comprension


##While
##Mientras se cumpla la condición que especificamos, estaremos en el bucle

a = 1
while (a<5) :
    print(a)
    a+=1
    
##Problemas con el bucle while, podemos caer en un bucle infinito
##Para eso, se puede utilizar el break con el objetivo de romperlo y evitar 

x = 1
while True:
    x= x+1
    if(x == 10):
        break
print (x)

##Continue - con esta expresión, vamos a colocar el siguiente a la condicion que nosotros metamos en nuestro bucle

y = 0
while y < 20 :
    y += 1
    if(y%2==0):
        continue
    print(y)
    
##Pass no hace nada, solo se utiliza cuando sintacticamente es necesario añadir una sentencia pero no es necesarrio para una accion
