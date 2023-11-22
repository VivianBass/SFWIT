print("\nEste algoritmo calcula el incremento salarial de una persona.")

try: 
    salario=input("\n¿Cuál es el salario en pesos?: ")

    salario=salario.replace(",","")
    salario=float(salario)
    
    if salario < 15000:
        incremento=salario*.2
    else:
        incremento=salario*.15

    print(f'\nEl incremento salarial es de: {incremento} pesos, para recibir en total: {salario+incremento} pesos.\n') 
	
except:
    print("\nOcurrió un error, favor de verificar que estás ingresando un salario válido.\n") 