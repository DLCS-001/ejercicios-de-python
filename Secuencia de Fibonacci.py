limite = int(input("Ingresa un número límite para Fibonacci: "))
a, b = 0, 1
while a <= limite:
    print(a)
    a, b = b, a + b
