# Programa para saber si una letra es vocal o consonante

letra = input("Ingresa una letra: ")

if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("La letra", letra, "es una vocal.")
else:
    print("La letra", letra, "es una consonante.")
