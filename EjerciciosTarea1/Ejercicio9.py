#Ejercicio 9: Escribir un programa que calcule la suma de los primeros N numeros enteros
import os
os.system('cls' if os.name == 'nt' else 'clear')

N = int(input("Ingresa un numero N: "))
suma = 0
for i in range(1, N + 1):
    suma += i
print("La suma de los primeros", N, "numeros es:", suma)
