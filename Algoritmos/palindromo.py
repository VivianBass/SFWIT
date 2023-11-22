import re
from unidecode import unidecode

print("\nEste algoritmo revisa si una cadena dada es palíndromo")

cadena=input("\nIngresa la cadena que quieres verificar si es palíndromo: ")

cadena2=unidecode(cadena)
exp=re.compile(r'[^a-zA-Z0-9]')

cadena_aux=exp.sub('',cadena2)
cadena_aux=cadena_aux.lower()
cadena_reversa = cadena_aux[::-1]

if cadena_aux == cadena_reversa:
    print(f'\nLa frase {cadena} SÍ es palíndromo!\n')
else:
    print(f'\nLa frase {cadena} NO es palíndromo!\n')
