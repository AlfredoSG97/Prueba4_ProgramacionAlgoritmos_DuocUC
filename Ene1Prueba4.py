import Funciones_Pasajes as Func
fila1=["Fila 1: Ventana ",1,2,3,4,5,6,"    Ventana"]
fila2=["Fila 2: Ventana ",7,8,9,10,11,12," Ventana"]
fila3=["Fila 3: Ventana ",13,14,15,16,17,18," Ventana "]
fila4=["Fila 4: Ventana ",19,20,21,22,23,24," Ventana "]
fila5=["Fila 5: Ventana ",25,26,27,28,29,30," Ventana "]
Division=["<<<<Salida Emergencias   , Salida Emergencias>>>> "]
fila6=["Fila 6 (Vip) Ventana ",31,32,33,34,35,36," Ventana "]
fila7=["Fila 7 (Vip) Ventana ",37,38,39,40,41,42," Ventana "]
opc=0
validarut=0
DatosCliente=[[],[],[]]
Nombre=""
telefono=0
contador=0
contadorVip=0
tarifanormal=78900
tarifavip=240000
rut=0
validanombre=0
asiento=0
validatelefono=0
ocupados=[]
validar_nombre=""
validar_telefono=0
totalpago9=0
totalFinal=0
try:
    while opc !=6:
        Func.menu_asientos()
        opc=int(input("Ingresa Una opcion: "))

        #Ver Asientos disponibles
        if opc==1:
            Func.mostrar_disponibles(fila1,fila2,fila3,fila4,fila5,fila6,fila7,Division)
        #Comprar asientos
        if opc==2:
            cantidad=int(input("Ingresa la cantidad de asientos que deseas comprar: "))
            Func.validar_rut(validarut)
            Func.validar_nombre(validanombre)
            Func.validar_telefono(validatelefono)
            print("=========================================================================")
            for c in range (cantidad):
                Func.mostrar_disponibles(fila1,fila2,fila3,fila4,fila5,fila6,fila7,Division)
                print("Valores asientos fila 1 a 5: $78.900 y filas Vip 6 y 7 :$240.000")
                fila=int(input("Ingresa el numero de la fila en la que te quieres sentar:  "))
                if fila==1:
                    contador=contador+1
                if fila==2:
                    contador=contador+1
                if fila==3:
                    contador=contador+1
                if fila==4:
                    contador=contador+1
                if fila==5:
                    contador=contador+1
                if fila==6:
                    contadorVip=contadorVip+1
                if fila==7:
                    contadorVip=contadorVip+1


                asiento=int(input("Ingresa el asiento en el que te quieres sentar:"))
                Func.remplazar_asientos(asiento,fila1,fila2,fila3,fila4,fila5,fila6,fila7,fila,contador,contadorVip)
            banco=int(input("Usted pertenece a BancoDuoc 1.- Si, 2.- No : "))
            pago = contador * tarifanormal
            pago2= contadorVip*tarifavip
            total=pago+pago2
            if banco==1:
                print("Tienes un descuento del 15% ")
                total=pago+pago2
                totalf=total*0.15
                print("Su nuevo total es: ",round(total-totalf))
                contador=0
                contadorVip=0
            if banco==2:
                print("Su total es: ",total)
                contador=0
                contadorVip=0
        if opc==3:
            fila=int(input("Ingresa el numero de la fila del asiento que quieres anular:  "))
            asiento=int(input("Ingresa el asiento que quieres anular:"))
            Func.liberar_asientos(asiento,fila1,fila2,fila3,fila4,fila5,fila6,fila7,fila,Nombre,telefono,rut)
            Func.mostrar_disponibles(fila1,fila2,fila3,fila4,fila5,fila6,fila7,Division)
        if opc==4:
            Func.modificar_datos(rut,validatelefono,validanombre)
        if opc==5:
            Func.salir()
            break
except ValueError:
    print("Ingresa datos validos.")