# Programa para determinar la calificación en letras según la nota numérica

calificacion = int(input("Ingresa la calificación (0-100): "))

if calificacion >= 90 and calificacion <= 100:
    print("La calificación es: A")
elif calificacion >= 80 and calificacion <= 89:
    print("La calificación es: B")
elif calificacion >= 70 and calificacion <= 79:
    print("La calificación es: C")
elif calificacion >= 60 and calificacion <= 69:
    print("La calificación es: D")
elif calificacion >= 0 and calificacion <= 59:
    print("La calificación es: F")
else:
    print("Calificación fuera de rango.")
