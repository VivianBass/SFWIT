# Este algoritmo calcula el volumen de una esfera

import math

try:
    radio = float(input("\nIngresa el radio de la esfera: "))

    vol = (4/3) * math.pi * (radio ** 3)

    print(f'\nEl volumen de la esfera es: {vol} unidades cúbicas\n')

except:
    print("\nOcurrió un error, favor de verificar que estás ingresando número válido.\n") 