a , b =0, 1
try:
    opc=int(input("Ingresa Un numero entre 10 y 15 para Generar los Números de la Serie Fibonacci: "))
    if opc<=15 and opc>=10:
        while b <=opc:
            print(b)
            a,b=b,a+b
    else:
        print("Ingresa un dato valido.")

except ValueError:
    print("Ingresa un numero valido.")
except NameError:
    print("Ingresa un dato valido.")