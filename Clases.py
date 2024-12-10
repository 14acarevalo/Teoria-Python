##En este ejemplo, se van a trabajar las clases y objetos que son tan importantes en python

class prueba1:
 
 ##Creamos una clase con un contenido vacio, por eso se pone el pass     
   
    ## Esto es el constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def metodo (x,y):
        pass ##Esto pondrá un constructor vacio
        
        
##Creamos una clase con un contenido dentro como es Hola      
class CuentaBancaria:
    def __init__(self):
        print("Hola")

cuenta_1 = CuentaBancaria()

##Creamos una clase con un contenido dentro como es el IBAN y el saldo . Recomendable esta opcion cuando tenenmos muchos argumentos.    

class CuentaBancaria1:
    def __init__(self, iban, saldo=0):
        self.iban = iban
        self.saldo = saldo

cuenta_1 = CuentaBancaria1(iban = "ES123456789", saldo = 30)
print(cuenta_1.iban)
print(cuenta_1.saldo)

##Creamos una clase con un contenido dentro como es el IBAN y el saldo - es igual que la de antes, pero con keywords  

class CuentaBancaria1:
    def __init__(self, iban, saldo=0):
        self.iban = iban
        self.saldo = saldo

cuenta_1 = CuentaBancaria1("ES123456789", 30)
print(cuenta_1.iban)
print(cuenta_1.saldo)

class CuentaBancaria2:
    def __init__(self, iban, saldo = 0):
        self.iban= iban
        self.saldo = saldo
    
    def ingresar_dinero (self, cantidad):
        self.saldo = self.saldo + cantidad
    
    def sacar_dinero (self, cantidad):
        if cantidad >= self.saldo:
            cantidad = self.saldo
        self.saldo -= cantidad
        return cantidad
    
    def transferir_dinero (self, cantidad, cuenta_destino):
        cantidad = self.sacar_dinero(cantidad)
        cuenta_destino.ingresar_dinero(cantidad)
        

cuenta_1 = CuentaBancaria2("ES123456789")
print(cuenta_1.iban)
print(cuenta_1.saldo)

cuenta_1.ingresar_dinero(4000)
print(f"Con el plus que hemos metido, el saldo pasa de 0 a {cuenta_1.saldo}")

cuenta_1.sacar_dinero(200)
print(f"Estoy sacando dinero, paso a tener: {cuenta_1.saldo}")


cuenta_2 = CuentaBancaria2("ES123456789898", 30)

cuenta_1.transferir_dinero(500, cuenta_2)
cuenta_2.saldo

class CuentaBancaria1:
    def __init__(self, iban, saldo=0):
        self.iban = iban
        self.saldo = saldo
        
cuenta_1 = CuentaBancaria2("ES123456789")
print(cuenta_1.iban)
print(cuenta_1.saldo)

cuenta_1.ingresar_dinero(4000)
print(f"Con el plus que hemos metido, el saldo pasa de 0 a {cuenta_1.saldo}")

cuenta_1.sacar_dinero(200)
print(f"Estoy sacando dinero, paso a tener: {cuenta_1.saldo}")

cuenta_2 = CuentaBancaria2("ES123456789898", 30)

cuenta_1.transferir_dinero(500, cuenta_2)
print(f"El saldo de la cuenta de destino es: {cuenta_2.saldo}")
