#UVG
#Bases de Datos
#Laboratorio 10
#
#Davis Alvarez - 15842

from Conexion import *
from decimal import Decimal

def menuPrincipal():
    fin = True
    print("__________________________")
    print("Bienvenido a IntelHalf")
    print("__________________________")
    while(fin):
        print("")
        print("(a). Buscar por Velocidad y RAM ")
        print("(b). Eliminar por Modelo")
        print("(c). Decrecer el precio por Modelo")
        print("(e). Salir")
        print("")

        acction = input("Ingrese la letra de la opcion que desea ejecutar: ")

        if (acction=='a'):
            print("(a). Buscar por Velocidad y RAM ")
            opcionA()
        elif (acction=='b'):
            print("(b). Eliminar por Modelo")
            opcionB()
        elif (acction == 'c'):
            print("(c). Decrecer el precio por Modelo")
            opcionC()
        elif (acction == 'd'):
            print("(d). Agregar un nuevo Modelo")
            opcionD()
        elif (acction == 'e'):
            fin=False
        else:
            print("'"+acction+"' no es una opcion! Intente de nuevo")

def opcionA():
    print("")
    print("__________________________")
    ram = input("Ingrese la RAM: ")
    vel =input("Ingrese la Velocidad: ")

    cnn = BeginTransaction()
    cur=cnn.cursor()
    consulta = "SELECT modelo, precio FROM PC WHERE ram="+ram+" and velocidad="+vel+""
    cur.execute(consulta)

    lista = cur.fetchall()
    print("")
    if(len(lista)>0):
        for i in lista:
            print("Modelo: " + i[0])
            print("Precio: "+ str(i[1]))
        print("")
        print("__________________________")
    else:
        print("Adam Kovic no encontro una PC con RAM "+ram+" y Velocidad "+vel+".")

    EndTransaction(cnn)

def opcionB():
    cnn = BeginTransaction()
    print("")
    mol = input("Ingrese Modelo: ")

    cur = cnn.cursor()
    consultaPC = "DELETE FROM PC WHERE modelo='"+mol+"'"
    consultaPro = "DELETE FROM Producto WHERE modelo='"+mol+"'"

    cur.execute(consultaPC)
    cur.execute(consultaPro)

    print("")
    res = input("Desea eliminar la PC modelos "+mol+" ? (y/n)")
    if(res=='y'):
        CommitTransaction(cnn)
    else:
        print("")
        print("Adam Kovic NO guardara los cambios realizados!")
        print("__________________________")
        EndTransaction(cnn)

def opcionC():
    cnn = BeginTransaction()
    print("")
    mol = input("Ingrese Modelo: ")

    cur = cnn.cursor()
    consulta = "select * from pc where modelo='" + mol + "'"

    cur.execute(consulta)

    lista = cur.fetchall()
    print("")
    if (len(lista) > 0):
        precio=lista[0][4]
        nPrecio=precio - Decimal(100.0)
        res = input("Desea disminuir este $"+ str(precio) +"precio a $"+str(nPrecio)+" ? (y/n)" )
        print("")
        print("__________________________")
        if (res == 'y'):
            actualizar = "UPDATE PC SET precio="+str(nPrecio)+" WHERE modelo='"+mol+"'"
            cur.execute(actualizar)
            CommitTransaction(cnn)
        else:
            print("")
            print("Adam Kovic NO guardara los cambios realizados!")
            print("__________________________")
            EndTransaction(cnn)
    else:
        print("Adam Kovic no encontro una PC con Modelo " + mol +".")


def opcionD():
    cnn = BeginTransaction()

    print("")
    fab = input("Ingrese Fabricante: ")
    mol = input("Ingrese Modelo: ")
    vel = input("Ingrese Velocidad: ")
    ram = input("Ingrese RAM: ")
    dis = input("Ingrese Disco Duro: ")
    pre = input("Ingrese Precio: ")

    cur = cnn.cursor()
    consulta = "select * from producto where modelo='" + mol + "'"

    cur.execute(consulta)

    lista = cur.fetchall()
    print("")
    if (len(lista) > 0):
        print("Alanah Pearce ha encontrado un modelo "+mol+" existente ")
        print("")
        EndTransaction(cnn)
    else:
        res = input("Desea ingresar el Modelo " + mol + "precio a $" + pre + " ? (y/n)")
        if (res == 'y'):
            insertarPC = "INSERT INTO Producto VALUES('"+fab+"','"+mol+"','PC');"
            insertarPro = "INSERT INTO PC VALUES('"+mol+"', "+vel+", "+ram+", "+dis+", "+pre+");"
            cur.execute(insertarPC)
            cur.execute(insertarPro)
            CommitTransaction(cnn)
        else:
            print("")
            print("Adam Kovic NO guardara los cambios realizados!")
            print("__________________________")
            EndTransaction(cnn)