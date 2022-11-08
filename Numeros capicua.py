listanum = []


def main():

    num = int(input("Elija un numero : "))
    token = num
    if int(num) < 0:
        print("numero incorrecto")
        main()
    for i in range(len(str(num))):
        a = num % 10
        listanum.insert(0, int(a))
        num = num/10
    for j in range(len(str(token))):
        b = listanum[0]
        c = listanum[-1]
        token = token/100
        if b != c:
            print("El numero no es capicua")
            break
        if b == c:
            if token >= 10:
                listanum.pop(0)
                listanum.pop(-1)
            if token < 10:
                print("El numero es capicua")
                print(listanum)
                break


main()
