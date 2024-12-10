import time

# Dormir durante 2 segundos
print("Esperando 2 segundos...")
time.sleep(2)
print("¡Despierto!")

# Obtener el tiempo actual en segundos desde el epoch
timestamp = time.time()
print("Timestamp actual:", timestamp)

# Convertir el timestamp a una estructura de tiempo legible
estructura_tiempo = time.localtime()
print("Fecha y hora actual:", time.strftime("%Y-%m-%d %H:%M:%S", estructura_tiempo))


import sys

# Mostrar la versión actual de Python
print("Versión de Python:", sys.version)

# Agregar un directorio al path de búsqueda de módulos
sys.path.append("/nuevo/directorio")
print("Nuevas rutas:", sys.path)

# Salir del programa
# sys.exit("Cerrando el programa")


import random

# Generar un número entero aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print("Número aleatorio entre 1 y 10:", numero_aleatorio)

# Seleccionar un elemento al azar de una lista
opciones = ["rojo", "verde", "azul"]
seleccion = random.choice(opciones)
print("Selección aleatoria:", seleccion)

# Mezclar una lista al azar
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print("Lista mezclada:", lista)


numero_magico = random.randint(1, 14)
print(f"El número mágico es igual a :{numero_magico}")

eleccion = ["vectra", "hyundai", "toyota"]
escoger = random.choice(eleccion)
print(f"El coche con el que voy a salir es: {escoger}")

number = random.random()
print(f"Numero flotante: {number}")




## Si nosotros queremos importar un archivo ya creado por nosotros, será todo igual
## El archivo creado tiene que terminar en py, como estoy haciendo con todos los documentos de python
## una vez creado pondremos import Logica

import Logica
import a
import modulo
import modulo


## Con lo que se va a jugar una vez importado, son con las diferentes funciones que existen dentro de este

# Si el archivo Logica.py contiene esta función
def suma(a, b):
    return a + b

import Logica

resultado = Logica.suma(3, 4) ## Como puedes observar, se llama al archivo y la función que se desea trabajar
print(resultado)


## Si quiero importar algo especifico de una carpeta - ten en cuenta que un archivo python no puede llevar -

from Ejercicios.Clases import display

################################################################################
    # Para el trabajo con librerias, existe una funcion, open ()
    
# f = open (file_path, `r`)

# La instrucción f = open(file_path, 'r') en Python realiza las siguientes acciones:

# open(file_path, 'r'): Esta función abre un archivo. El parámetro file_path es la ruta del archivo que deseas abrir, y 'r' indica que el archivo se abrirá en modo de lectura (read mode).

# 'r' (modo de lectura): Significa que el archivo se abrirá solo para leer. Si el archivo no existe, lanzará un error. Otros modos disponibles incluyen:
# 'w': Modo escritura. Crea un archivo nuevo o sobrescribe uno existente.
# 'a': Modo de adjuntar (append). Añade contenido al final del archivo si ya existe.
# 'b': Modo binario, utilizado para archivos no textuales como imágenes o videos.
# f: El archivo abierto se asigna a la variable f, lo que te permite realizar operaciones sobre ese archivo, como leer su contenido.

file_path = "archivo.txt"  # Nombre del archivo que quieres abrir
f = open(file_path, 'r')  # Abre el archivo en modo de lectura

# Leer el contenido del archivo
contenido = f.read()

print(contenido)

# No olvides cerrar el archivo después de usarlo
f.close()

    

