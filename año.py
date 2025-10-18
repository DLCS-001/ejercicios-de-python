# Programa para saber si un año de nacimiento es válido

año = int(input("Ingresa tu año de nacimiento: "))

if año > 1900 and año < 2025:
    print("El año de nacimiento es válido.")
else:
    print("El año de nacimiento no es válido.")
