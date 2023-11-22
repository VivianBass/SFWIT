from datetime import datetime

print("\nEste algoritmo calcula cuántos días faltan de la fecha actual a día de muertos y navidad.")

hoy = datetime.now()
muertos = datetime.strptime("2024-11-01", '%Y-%m-%d')
navidad= datetime.strptime("2023-12-25", '%Y-%m-%d')

dias_muertos = (muertos - hoy).days +1
dias_navidad = (navidad - hoy).days +1

print(f'\nFaltan {dias_muertos} días para día de muertos y {dias_navidad} días para navidad.\n')
    
