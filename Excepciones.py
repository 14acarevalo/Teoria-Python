#VALUE ERROR
print("Explicación: Se lanza un ValueError porque abc no puede ser convertido a un entero.")

try:
    num = int("abc")  # Intentando convertir una cadena no numérica a entero
except ValueError:
    print("Error: No se puede convertir 'abc' a un número entero.")
    
#TYPEERROR 
print ("Explicación: Se lanza un TypeError porque no se pueden concatenar tipos de datos diferentes (cadena y entero).")

try:
    result = '2' + 2  # Intentando sumar una cadena y un número
except TypeError:
    print("Error: No se puede sumar una cadena y un número.")

#ZERODIVISIONERROR

print("Explicación: Se lanza un ZeroDivisionError porque la división por cero no está definida.")

try:
    result = 10 / 0  # Intentando dividir por cero
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
    
#INDEXERROR

print("Explicación: Se lanza un IndexError porque el índice 5 no existe en la lista (que solo tiene índices 0, 1 y 2).")

my_list = [1, 2, 3]
try:
    print(my_list[5])  # Intentando acceder a un índice fuera de rango
except IndexError:
    print("Error: Índice fuera de rango.")

#IMPORTERROR
# print("He puesto todo comentado porque salia errores")
print("Explicación: Se lanza un ImportError porque el módulo que se intenta importar no está disponible.")

#try:
    #import modulo_inexistente  - Intentando importar un módulo que no existe
#except ImportError:
   # print("Error: No se pudo importar el módulo.")
   
#NAMEERROR

#CUANDO UNA VARIABLE NO HA SIDO DEFINIDA
try:
    print(undifined_variable)  # Intentando acceder a una variable que no ha sido definida
except NameError:
    print("Error: La variable 'undifined_variable' no está definida.")
