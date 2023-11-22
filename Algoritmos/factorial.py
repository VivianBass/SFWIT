import math

print("\nEste programa calcula el factorial de un número dado.")

try:
    numero = int(input("\n¿De cuál número quieres calcular el factorial?: "))

    factorial = math.factorial(numero)

    print(f'\nEl factorial de {numero} es: {factorial}\n') 

except:
    print("\nOcurrió un error, favor de verificar que estás ingresando un número entero.\n") 