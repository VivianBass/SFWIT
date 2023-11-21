# Este algoritmo calcula si un número es par o impar

try:
    numero=float(input("\nDigita el número del que quieres saber si es par o impar: "))

    if numero%2==0:
        print(f'\n{numero} es un número par.\n')
    else:
        print(f'\n{numero} es un número impar.\n')
   
        
except:
    print("\nOcurrió un error, favor de verificar que estás ingresando un número válido.\n") 