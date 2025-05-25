#Ejercicio 4: Escribir un programa que pida al usuario un número y determine si es positivo, negativo o cero.
import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = float(input("Ingresa un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")
