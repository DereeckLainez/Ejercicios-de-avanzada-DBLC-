#trabajo de union de ejercicios en clase usando el self

import os
os.system('cls' if os.name == 'nt' else 'clear')

class EjerciciosEnClase:
    def __init__(self, nombre, perro, gato, a, b, Operacion, TotalCompra, Descuento, Isv, ValorCompra, SubTotal, Total, AnioActual, AnioNacimiento, Edad, TablaMultiplicar, Num, Diametro, MiPerro, Suma, Resta, Multi, Div, x, y, Potencia, Residuo, Raiz):
        self.nombre = nombre
        self.perro = perro
        self.gato = gato
        self.a = a
        self.b = b
        self.Operacion = Operacion
        self.TotalCompra = TotalCompra
        self.Descuento = Descuento
        self.Isv = Isv
        self.ValorCompra = ValorCompra
        self.SubTotal = SubTotal
        self.Total = Total
        self.AnioActual = AnioActual
        self.AnioNacimiento = AnioNacimiento
        self.Edad = Edad
        self.TablaMultiplicar = TablaMultiplicar
        self.Num = Num
        self.Diametro = Diametro
        self.MiPerro = MiPerro
        self.Suma = Suma
        self.Resta = Resta
        self.Multi = Multi
        self.Div = Div
        self.x = x
        self.y = y
        self.Potencia = Potencia
        self.Residuo = Residuo
        self.Raiz = Raiz

    def Condicionales(self):
        self.a = int(input("Ingrese un número: "))
        if self.a % 2 == 0:
            print(f"El numero {self.a} es par")
        else:
            print(f"El numero {self.a} es impar")

    def Ejercicio01(self):
        self.TotalCompra = 0
        self.Descuento = 0
        self.Isv = 0.15

        self.ValorCompra = float(input("Ingrese el valor de la compra por un producto: "))
        if self.ValorCompra >= 1000:
            self.Descuento = 0.25
        else:
            self.Descuento = 0
        self.TotalCompra = self.ValorCompra - (self.ValorCompra * self.Descuento)
        self.TotalCompra = self.TotalCompra + (self.TotalCompra * self.Isv)
        print(f"El total de la compra por un producto es: {self.TotalCompra}")

    def Ejercicio02(self):
        self.AnioActual = 2025
        self.AnioNacimiento = float(input("Por favor ingrese su año de nacimiento: "))
        self.Edad = self.AnioActual - self.AnioNacimiento

        print("Su edad actualmente es: ", self.Edad)

        if self.Edad >= 21:
            print("Usted es mayor de edad")
        else:
            print("Usted es menor de edad en el rango de los 21 años")

        if self.Edad >= 18:
            print("Usted es ciudadano, ya puede ejercer su derecho al voto")
        else:
            print("Usted es menor de edad, no puede ejercer su derecho al voto")

    def Ejercicio03(self):
        self.TablaMultiplicar = int(input("Por favor ingrese el numero de la tabla de multiplicar que quiere ver: "))
        print("TABLA DE MULTIPLICAR DEL", self.TablaMultiplicar)
        for i in range(1, 11):
            print(self.TablaMultiplicar, "x", i, "=", self.TablaMultiplicar * i)

    def Ejercicio04(self):
        self.i = 1
        self.Num = int(input("Por favor ingrese el numero de la tabla de multiplicar que desea ver: "))
        print("La tabla de multiplicar del ", self.Num, " es: ")
        while self.i <= 10:
            print(self.Num, "x", self.i, "=", self.Num * self.i)
            self.i += 1

    def EjercicioCicloFor(self):
        for i in range(11):
            print(i)

    def EjercicioTablaDel5(self):
        print("TABLA DE MULTIPLICAR DEL 5")
        for i in range(1, 11):
            print("5 x", i, "=", 5 * i)

    def EjercicioCicloWhile(self):
        i = 1
        while i <= 10:
            print("Numero: ", i)
            i += 1

    def HolaMundo(self):
        print("Hola Mundo")

    def OperacionesAritmeticas(self):
        a = 10
        b = 5

        # Suma
        Suma = a + b
        print(f"{a} + {b} = {Suma}")

        # Resta
        Resta = a - b
        print(f"{a} - {b} = {Resta}")

        # Multiplicacion
        Multi = a * b
        print(f"{a} * {b} = {Multi}")

        # División
        Div = a / b
        print(f"{a} / {b} = {Div}")

        # valores a variables
        x = int(input("x: "))
        y = int(input("y: "))

        # Potencia
        Potencia = x ** y
        print(f"{x} ^ {y} = {Potencia}")

        # residuo
        Residuo = x % y
        print(f"{x} % {y} = {Residuo}")

        # Raiz cuadrada
        Raiz = x ** (1/2)
        print(f"Raiz cuadrada de {x} = {Raiz}")

# --- FUNCIONES GLOBALES FUERA DE LA CLASE ---

def saludo(nombre):
    print(f"Hola {nombre}")

def _Pi():
    return 3.1416

def suma(a, b):
    return a + b

def Suma(a, b):
    return a + b

def Resta(a, b):
    return a - b

def Multiplicacion(a, b):
    return a * b

def Division(a, b):
    return a / b

def Potencia(a, b):
    return a ** b

def Raiz(a):
    return a ** (1/2)



# --- FUNCIONES GLOBALES ---
if __name__ == "__main__":
    saludo("Carlitos Chávez")

    # diametro de un circulo
    R = 10
    Diametro = 2 * _Pi() * R
    print(f"El diametro del circulo es: {Diametro}")

    # suma
    print(f"La suma es igual a: {suma(1, 1)}")

    # funciones aritmeticas
    print(f"La suma es igual a: {Suma(1, 1)}")
    print(f"La resta es igual a: {Resta(1, 1)}")
    print(f"La multiplicacion es igual a: {Multiplicacion(2, 2)}")
    print(f"La division es igual a: {Division(25, 5)}")
    print(f"La potencia es igual a: {Potencia(2, 2)}")
    print(f"La raiz cuadrada es igual a: {Raiz(36)}")



# Clase animal 

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def correr(self):
        print(f"{self.nombre} esta corriendo")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} gua gua gua")



# Definir objetos para usar las clases
if __name__ == "__main__":
    perro = Perro("Rufus")
    perro.correr()
    perro.ladrar()
    perro.comer()

    gato = Animal("Misio")
    gato.correr()
    gato.comer()


    