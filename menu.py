def menu():
    print("0)Salir\n1)10 primeros numeros impares")
    print("2)impares divisibles entre 3 y 7 menores de 300")
    n = int(input("Selecciona la opción : "))
    if n == 1:
        lista = []
        token = 0
        while len(lista) != 10:
            token = token + 1
            par = token % 2
            if par != 0:
                lista.append(token)
                print(lista)
        menu()    
    if n == 2:
        lista = []
        token = 0
        while len(lista) != 10:
            token = token + 1
            par = token % 2
            div3 = token % 3
            div7 = token % 7
            if token > 300:
                menu()
                break
            if par != 0 and div3 == 0 and div7 == 0:
                lista.append(token)
                print(lista)
    if n == 0:
        SystemExit()
    if n > 2:
        print("numero incorrecto")
        menu()


menu()

