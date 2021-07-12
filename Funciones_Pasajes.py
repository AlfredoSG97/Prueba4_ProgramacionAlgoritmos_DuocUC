import sys
from itertools import cycle
DatosCliente=[[],[],[]]
rutClientes=[]
validarut=0
validanombre=0
#Tarifas
tarifanormal=78900
validatelefono=0
tarifavip=240000
contadorN=0
contadorV=0
pagonormal=0
pagovip=0
totales=[]
#Pagos

descuento=0
def menu_asientos ():
    print ("------MENU------")
    print ("1.- ver asientos disponibles ")
    print ("2.- comprar asientos")
    print ("3.- anular vuelo  ")
    print ("4.- modificar datos del pasajero ")
    print ("5.- salir")

def salir():
    print("Gracias por comprar con nosotros.")




def validar_rut(validarut):
    while validarut<=0:
        rut=int(input("Ingresa tu rut para el registro. : "))
        if rut==():
            print("debes  ingresar los datos solicitados.")
        if rut <=999999999 and rut >=1000000:
            registra_rut(rut)
            validarut=validarut+1
        else:
            print("Rut incorrecto, verifica los datos ingresados.")


def modificar_datos(rut,validatelefono,validanombre):

    try:
        rut=int(input("Ingresa tu rut para buscar en el registro. : "))
        rutClientes.index(rut)
        print("Rut Encontrado")
        modificar=int(input("1.- Modificar telefono , 2.- Modificar Nombre: "))
        if modificar==1:
            DatosCliente[2].pop()
            print("Telefono eliminado con exito. ")
            while validatelefono<=0:
                telefono=int(input("Ingresa tu nuevo telefono para el registro :+569 "))
                if telefono==():
                    print("Ingresa un telefono valido")
                if telefono <=99999999 and telefono >=11111111:
                    registra_telefono(telefono)
                    validatelefono=validatelefono+1
                    input("Ingresa enter para continuar")
                else:
                    print("Ingresa un numero valido")
        if modificar==2:
            DatosCliente[1].pop()
            print("Nombre eliminado de la lista")
            while validanombre<=0:
                Nombre=input("Ingresa el nuevo nombre: ")
                if Nombre==():
                    print("Ingresa un nombre valido.")
                else:
                    registra_Nombre(Nombre)
                    validanombre=validanombre+1
        print(DatosCliente)
    except ValueError:
        print("Rut no registrado")

def validar_nombre(validanombre):
    while validanombre<=0:
        Nombre=input("Ingresa tu nombre: ")
        if Nombre==():
            print("Ingresa un nombre valido.")
        else:
            registra_Nombre(Nombre)
            validanombre=validanombre+1

def validar_telefono(validatelefono):
    while validatelefono<=0:
        telefono=int(input("Ingresa tu telefono para el registro :+569 "))
        if telefono==():
            print("Ingresa un telefono valido")
        if telefono <=99999999 and telefono >=11111111:
            registra_telefono(telefono)
            validatelefono=validatelefono+1
            input("Ingresa enter para continuar")
        else:
            print("Ingresa un numero valido")



def liberar_asientos(asiento,fila1,fila2,fila3,fila4,fila5,fila6,fila7,fila,Nombre,telefono,rut):
    if fila == 1:
        if asiento <1 or asiento >6:
            print("usted a ingresado un numero de asiento que no corresponde a la fila ")
        else:
            fila1[asiento] = asiento
            DatosCliente[0].pop()
            DatosCliente[1].pop()
            DatosCliente[2].pop()

    if fila ==2:
        if asiento <7 or asiento >12:
            print("usted a ingresado un numero de asiento que no corresponde a la fila ")
        else:
            fila2[asiento-6] = asiento
            DatosCliente[0].pop()
            DatosCliente[1].pop()
            DatosCliente[2].pop()
    if fila == 3:
        if asiento <13 or asiento > 18:
            print("usted a ingresado un numero de asiento que no corresponde a la fila ")
        else:
            fila3[asiento-12] = asiento
            DatosCliente[0].pop()
            DatosCliente[1].pop()
            DatosCliente[2].pop()
    if fila == 4:
        if asiento <19 or asiento > 24:
            print("usted a ingresado un numero de asiento que no corresponde a la fila ")
        else:
            fila4[asiento-18] = asiento
            DatosCliente[0].pop()
            DatosCliente[1].pop()
            DatosCliente[2].pop()
    if fila ==5:
        if asiento <25 or asiento >30:
            print("usted a ingresado un numero de asiento que no corresponde a la fila ")
        else:
            fila5[asiento-24] = asiento
            DatosCliente[0].pop()
            DatosCliente[1].pop()
            DatosCliente[2].pop()
    if fila ==6:
        if asiento <31 or asiento >36:
            print("usted a ingresado un numero de asiento que no corresponde a la fila ")
        else:
            fila6[asiento-30] = asiento
            DatosCliente[0].pop()
            DatosCliente[1].pop()
            DatosCliente[2].pop()
    if fila == 7:
        if asiento <37 or asiento >42:
            print("usted a ingresado un numero de asiento que no corresponde a la fila ")
        else:
            fila7[asiento-36] = asiento
            DatosCliente[0].pop()
            DatosCliente[1].pop()
            DatosCliente[2].pop()


def remplazar_asientos (asiento,fila1,fila2,fila3,fila4,fila5,fila6,fila7,fila,contador,contadorVip):
    if fila==1:
        fila1[asiento] = "X"
        contador=contador+1
    if fila==2:
        fila2[asiento-6] = "X"
        contador=contador+1
    if fila==3:
        fila3[asiento-12] = "X"
        contador=contador+1
    if fila==4:
        fila4[asiento-18] = "X"
        contador=contador+1
    if fila==5:
        fila5[asiento-24] = "X"
        contador=contador+1
    if fila==6:
        fila6[asiento-30] = "X"
        contadorVip=contadorVip+1
    if fila==7:
        fila7[asiento-36] = "X"
        contadorVip=contadorVip+1



def mostrar_disponibles(fila1,fila2,fila3,fila4,fila5,fila6,fila7,Division):
    print("Los Asientos disponibles son: ")
    print(fila1)
    print(fila2)
    print(fila3)
    print(fila4)
    print(fila5)
    print(Division)
    print(fila6)
    print(fila7)
    return mostrar_disponibles


def registra_rut(rut):
    DatosCliente[0].append(rut)
    rutClientes.append(rut)
    print("Rut Ingresado Correctamente. ")
    return registra_rut

def registra_Nombre(Nombre):
    DatosCliente[1].append(Nombre)
    print("Nombre Ingresado Correctamente. ")
    return registra_Nombre

def registra_telefono(telefono):
    DatosCliente[2].append(telefono)
    print("Telefono Ingresado Correctamente. ")
    return registra_telefono

