#Ejercicio 8: Escribir un programa que imprima la tabla de multiplicar de un numero ingresado por el usuario
import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Ingresa un numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
