# Programa para saber si un número es primo o no

numero = int(input("Ingresa un número: "))

if numero <= 1:
    print("El número no es primo.")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("El número", numero, "es primo.")
    else:
        print("El número", numero, "no es primo.")
