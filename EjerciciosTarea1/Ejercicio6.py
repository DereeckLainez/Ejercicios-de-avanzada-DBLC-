#Ejercicio 6: Escribir un programa que pida al usuario tres números y determine cuál es el mayor
import os
os.system('cls' if os.name == 'nt' else 'clear')

a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))
mayor = max(a, b, c)
print("El numero mayor es:", mayor)
