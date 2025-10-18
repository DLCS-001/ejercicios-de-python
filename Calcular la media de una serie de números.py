suma = 0
contador = 0
while True:
    n = int(input("Ingresa un número (0 para terminar): "))
    if n == 0:
        break
    suma += n
    contador += 1
if contador > 0:
    print("La media es:", suma / contador)
else:
    print("No se ingresaron números.")
