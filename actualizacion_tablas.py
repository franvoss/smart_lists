import update as update

from base_de_datos import BaseDeDatos
from datetime import datetime

bd = BaseDeDatos()

def agregar_lista(nombre_Lista, favorito_lista, confirmacion, id_producto):
    sql_agregar_Lista = f'''
    INSERT INTO lista (nombre_lista, fechaCreada, favorito_lista, confirmacion, idProducto)
    VALUES ({nombre_lista}, {datetime.now().strftime("%Y-%m-%d %H:%M%S")}, {favorito_lista}, {confirmacion}, {id_producto})
    '''
    bd.ejecutar_sql(sql_agregar_lista)

def update_lista(nombre):
    sql = "update form lista where nombre_Lista = nombre_Lista"
    SET lista = nombre_Lista
    WHERE nombrelista = "hoy domingo lasagna"

def Delete from table_lista
    sql = "delete form lista where nombre_lista = hoy domingo lasagna"




def agregar_precio(idPrecio, precioreal, fechaRegistro, idUsuario):
    sql_agregar_precio = f'''
    INSERT INTO precio (idPrecio, precioreal, fechaRegistro, idUsuario)
    VALUES ({idPrecio}, {precioreal}, {datetime.now().strftime("%Y-%m-%d %H:%M%S")}, {idUsuario})
    '''
    bd.ejecutar_sql(sql_agregar_precio)

def update_precio(precioreal):
    sql_agregar_precio = f'''
    sql = "update form precio where precioreal = 10"
    SET precioreal = 10
    WHERE idPrecio = 001
    """
    bd.ejecutar_sql(sql_update_precio)

def Delete from table_precio
    sql = "delete form precio where precioreal = 10"




def agregar_producto(idProducto, nombreproducto, idPrecio):
    sql_agregar_producto = f'''
    INSERT INTO producto (idProducto, nombreproducto, idPrecio)
    VALUES ({idProducto}, {nombreproducto}, {idPrecio})
    '''
    bd.ejecutar_sql(sql_agregar_precio)

def update_table_producto():
    sql = "update form producto where nombreproducto = tomate"
    SET nombreproducto = tomate
    WHERE condition;

def delete from table_producto
    sql = "delete form precio where precioreal = 10"



def agregar_receta (idRecetea, nombreReceta, fechaCreada, favorito_receta, procedimiento, idproducto):
    sql_agregar_producto = f'''
    INSERT INTO producto (idReceta, nombreReceta, fechaCreada, favorito_receta, procedimiento, idproducto)
    VALUES ({idReceta}, {nombreproducto}, {idPrecio})
    '''
    bd.ejecutar_sql(sql_agregar_precio)

def update_table_receta():
        SET nombrereceta = tomate
        WHERE condition;

def Delete from table_lista
    sql = "delete form lista where nombre_lista = hoy domingo lasagna"








