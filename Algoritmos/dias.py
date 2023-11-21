# Este algoritmo calcula cuántos días tienes en el periodo de los años 1582 al 2023. 
# Se calcula desde 1582 porque es el año que empezaron a usarse los años bisiestos

from datetime import datetime


try:
    fecha = input("\nIngresa tu fecha de nacimiento en el formato YYYY-MM-DD: ")
    fecha = datetime.strptime(fecha, '%Y-%m-%d')
    hoy = datetime.now()

    if 1582 < fecha.year < hoy.year:
        dias = (hoy - fecha).days
        print(f'\nTienes {dias} días de edad.\n')
    else:
        print("\nFavor de revisar los años introducidos. Este algoritmo calcula cuántos días tienes en el periodo de los años 1582 al 2023. \n")

except ValueError:
    print("\nFecha inválida, favor de revisar la fecha introducida.\n")