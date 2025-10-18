suma = 0
num = int(input("Ingresa un número positivo (negativo para salir): "))
while num >= 0:
    suma += num
    num = int(input("Ingresa otro número positivo (negativo para salir): "))
print("La suma total es:", suma)
