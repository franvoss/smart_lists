'''def funcion(parametro,parametro2):
    print(parametro)
    print(parametro2)
one = "asd"
two = "abc"
funcion(one,two)'''

import sqlite3
'''def consulta2():
    conexion = sqlite3.connect('ListasInteligentes.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuario(nombreUsuario, correo, passwd) VALUES ('prueba','prueba','prueba')")
    conexion.commit()
consulta2()'''



def consulta():
    conexion = sqlite3.connect('ListasInteligentes.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)


print (consulta())


