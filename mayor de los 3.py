a=0
b=0
c=0

print("Ingrese 3 numeros")
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))

if a>b and a>c:
    print("El numero mayor es: ",a)
elif b>a and b>c:
    print("El numero mayor es: ",b)
else:
    print("El numero mayor es: ",c)
    