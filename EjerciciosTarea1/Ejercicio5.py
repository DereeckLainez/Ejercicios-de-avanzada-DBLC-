#Ejercicio 5: Escribir un programa que pida al usuario un numero entero y determine si es par o impar
import os 
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Ingresa un numero entero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
