#UVG
#Bases de Datos
#Laboratorio 10
#
#Davis Alvarez - 15842


import psycopg2



print ("Opened database successfully")

#Funcion que inicia una Transaccion
def BeginTransaction():
    try:
        conn = psycopg2.connect(database="lab10-15842", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
        print("")
        print("James Willems esta listo para realizar la Transaccion!")
        print("__________________________")
        return conn
    except:
        print("Ocurrio un error al iniciar la Transaccion, Contacte a Bruce Green para resolver el problema")

#Funcion que finaliza una Transaccion
def EndTransaction(conexion):
    try:
        conexion.close()
        print("Elyse Willems cerro la Transaccion!")
        print("__________________________")
        print("")
    except:
        print("Ocurrio un error al cerrar la Transaccion, Contacte a Bruce Green para resolver el problema")

#Funcion que realiza un commit a la DB
def CommitTransaction(conexion):
    try:
        conexion.commit()
        print("")
        print("Adam Kovic guardo los cambios realizados!")
        print("__________________________")
        EndTransaction(conexion)
    except:
        print("Ocurrio un error al guardar la Transaccion, Contacte a Bruce Green para resolver el problema")
        print("Se realilzara un Rollback automatico...")

        rollbackTransaction(conexion)

#Funcion que realiza un Rollback a la DB
def rollbackTransaction(conexion):
    try:
        conexion.rollback()
        print("")
        print("Lawrence Sonntag ha realizado el RollBack correctamente!")
        print("__________________________")
        EndTransaction(conexion)
    except:
        print("Ocurrio un error al hacer Rollback, Contacte a Bruce Green para resolver el problema")
