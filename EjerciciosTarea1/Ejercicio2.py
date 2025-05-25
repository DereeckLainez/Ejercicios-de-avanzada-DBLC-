# Ejercicio 2: Sumar dos números y mostrar el resultado
import os
os.system('cls' if os.name == 'nt' else 'clear')

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
suma = a + b
print("La suma es:", suma)
