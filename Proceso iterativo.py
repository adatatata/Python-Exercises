n = int(input("Seleccione un numero positivo : "))
token = 0
if n == 1:
    print(n)
    print(token)
while int(n) > 1:
    if n % 2 != 0:
        n = n*3+1
        token = token+1
        print("cantidad de valores generados", token)
        print(n)
    if n % 2 == 0:
        n = n/2
        token = token+1
        print("cantidad de valores generados", token)
        print(n)
print(n)
print("Cantidad de valores generados", token)
