import sqlite3


sql_tabla_usuario = '''
CREATE TABLE usuario(
idUsuario integer PRIMARY KEY AUTOINCREMENT,
nombreUsuario text not null unique,
correo text not null unique,
passwd text not null
)
'''

sql_tabla_precio ='''
CREATE TABLE precio(
idPrecio integer PRIMARY KEY AUTOINCREMENT,
precio real,
fechaRegistro text,
idUsuario integer,
FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario)
)
'''

sql_tabla_producto = '''
CREATE TABLE producto(
idProducto integer PRIMARY KEY AUTOINCREMENT,
nombreProducto text not null,
idPrecio integer,
FOREIGN KEY(idPrecio) REFERENCES precio(idPrecio)
)
'''

sql_tabla_lista ='''
CREATE TABLE lista(
idLista integer PRIMARY KEY AUTOINCREMENT,
nombreLista text not null default "Nueva Lista",
fechaCreada text not null, color integer,
favorito_lista boolean default false,
confirmacion boolean default false,
idProducto integer,
FOREIGN KEY(idProducto) REFERENCES producto(idProducto)
)
'''

sql_tabla_receta = '''
CREATE TABLE receta(
idReceta integer PRIMARY KEY AUTOINCREMENT,
nombreReceta text not null default "Nueva Receta",
fechaCreada text not null,
favorito_receta boolean default false,
procedimiento text,
idProducto integer,
FOREIGN KEY(idProducto) REFERENCES producto(idProducto))'''


if __name__ == '__main__':
    try:
        print('Creando Base de datos')
        conexion = sqlite3.connect('ListasInteligentes.db')

        print('Creando tablas')
        conexion.execute(sql_tabla_usuario)
        conexion.execute(sql_tabla_precio)
        conexion.execute(sql_tabla_producto)
        conexion.execute(sql_tabla_lista)
        conexion.execute(sql_tabla_receta)

        conexion.close()

        print('Base de datos lista!')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)
