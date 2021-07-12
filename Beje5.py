import func5 as ef
numero1 = 0
numero2 = 0
numeros = 0
op = 0
try:
    while op >= 1 or op <=4:
        ef.menu()
        op = int(input("ingresa una opcion: "))
        if op == 1:
            numero1 = int(input("ingrese el primer numero: "))
            numero2 = int(input("ingrese el segundo numero: "))
            if numero1>numero2:
                total = ef.mayor(numero1, numero2)
                print("el primer numero es mayor por la tanto su total es de: ", str(total))
            else:
                print("El segundo numero es mayor que el primero. ")
        if op == 2:
            numero1 = int(input("ingrese el primer numero: "))
            numero2 = int(input("ingrese el segundo numero: "))
            total = ef.menor(numero1, numero2)
            print("el primer numero es menor por lo tanto su resultado es: ", str(total))
        if op == 3:
            numero1 = int(input("ingrese el primer numero: "))
            numero2 = int(input("ingrese el segundo numero: "))
            total = ef.igual(numero1, numero2)
            print("ambos numeros iguales por lo tanto su resultado es : ", str(total))
        if op == 4:
            ef.salir()
            break
except ValueError:
    print("recurde que solo debe ingresar numeros")
    