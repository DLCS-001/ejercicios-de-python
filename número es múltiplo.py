# Programa para saber si un número es múltiplo de 5 y de 7

numero = int(input("Ingresa un número: "))

if numero % 5 == 0 and numero % 7 == 0:
    print("El número", numero, "es múltiplo de 5 y de 7.")
else:
    print("El número", numero, "no es múltiplo de 5 y de 7.")
