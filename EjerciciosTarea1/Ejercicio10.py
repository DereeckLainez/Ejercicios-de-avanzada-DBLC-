#Ejercicio 10: Escribir un programa que imprima una linea de asteriscos de longitud N
import os
os.system('cls' if os.name == 'nt' else 'clear')

N = int(input("Ingresa un numero N: "))
print("*" * N)
