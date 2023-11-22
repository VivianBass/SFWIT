print("\nEste algoritmo calcula si un año es bisiesto o no.")

try:

    anio = int(input("\nEscribe el año que quieres saber si es bisiesto: ")) 

    if anio%400==0:
        print(f'\nEl año {anio} es bisiesto.\n') 
    else:
        if anio%4==0 and anio%100!=0:
            print(f'\nEl año {anio} es bisiesto.\n') 
        else:
            print(f'\nEl año {anio} NO es bisiesto.\n') 

except:
    print("\nOcurrió un error, favor de verificar que estás ingresando un año válido.\n") 