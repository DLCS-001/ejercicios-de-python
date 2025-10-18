n = int(input("Ingresa un número n: "))
suma = 0
for i in range(1, n+1):
    suma += i
    print(suma, end=", " if i < n else "\n")
