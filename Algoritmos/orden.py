print("\nEste algoritmo ordena una lista de 5 números de menor a mayor")

try:
    entrada = input("\nIngresa una lista de 5 números separados por espacios: ")
    lista = list(map(float, entrada.split()))

    if len(lista) == 5:
        print(f'\nLa lista que ingresaste es: {lista}')
        lista.sort()
        print(f'\nLa lista ordenada es: {lista}\n')
    else:
        print("\nIngresa 5 números exactamente.\n")

except:
    print("\nOcurrió un error, favor de verificar que estás ingresando una lista de números separada por espacios.\n") 