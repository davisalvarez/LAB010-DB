#UVG
#Bases de Datos
#Laboratorio 10
#
#Davis Alvarez - 15842


import psycopg2

conn = psycopg2.connect(database="lab10-15842", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")
