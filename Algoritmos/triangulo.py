print("\nEste algoritmo calcula el área de un triángulo")

try: 
    b = float(input("\nDame la base del triángulo: "))
    h = float(input("Dame la altura del triángulo: "))

    area = (b*h)/2

    print(f'\nEl área del triágulo es: {area}\n')

except:
    print("\nOcurrió un error, favor de verificar que estás ingresando números válidos.\n") 