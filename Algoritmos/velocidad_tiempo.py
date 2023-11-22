print("\nEste algoritmo calcula el tiempo que tardas en recorrer una distancia a una velocidad dada.")

try:
    v = float(input("\nDame la velocidad en km/h: "))
    d = float(input("Dame la distancia en km: "))

    t=d/v
        
    if t==1:
        h="hora"
    else:
        h="horas"


    print(f'\nEl tiempo que tardas en recorrer {d} km a una velocidad de {v} km/h, es de:{t: .2f} {h}.\n') 

except:
    print("\nOcurrió un error, favor de verificar que estás ingresando velocidad y distancia válidas.\n") 