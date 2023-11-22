import re


print("\nEste algoritmo pide el nombre de la persona y lo muestra en pantalla")

nombre = input("\n¿Cómo te llamas?: ")


if all(x.isalpha() or x.isspace() for x in nombre):
    print(f'\nHola {nombre}!\n')
else:
    print("\nOcurrió un error, favor de verificar que estás ingresando un nombre válido.\n") 


