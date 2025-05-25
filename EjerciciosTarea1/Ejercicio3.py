# Ejercicio 3: Calcular el area de un rectangulo
import os
os.system('cls' if os.name == 'nt' else 'clear')

base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))
area = base * altura
print("El area del rectangulo es:", area)
