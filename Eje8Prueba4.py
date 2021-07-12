conta=0
opc=0
while opc!=2:
    opc=int(input("Ingresa 1 para verificar palindromos o 2 para salir. "))
    if opc==1:
        palabra=str(input("Ingresa la palabra, recuerda que deben ser solo frases: ")).strip().upper()
        palabras=palabra.split()
        eliminaespacios="".join(palabras)
        invertir=""
        for l in range(len(eliminaespacios)-1,-1,-1):
            invertir+=eliminaespacios[l]
        for l in palabra:
            if (l.isalpha()):
                conta+=1
        if invertir==eliminaespacios:
            print("Es un palindromo")
            print("La cantidad de letras es: ",conta)
        else:
            print("No es un palindromo")
            print("La cantidad de letras es: ",conta)
    if opc==2:
        print("Seleccionaste Salir")
        break