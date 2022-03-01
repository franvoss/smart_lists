from base_de_datos import BaseDeDatos

bd = BaseDeDatos()

def crear_usuario(nombreUsuario,correo,passwd):
    #print('llego a crear usuario')
    crear_usuario_sql = f"""
        INSERT INTO usuario (nombreUsuario,correo,passwd)
        VALUES ('{nombreUsuario}','{correo}','{passwd}')
"""
    bd.ejecutar_sql(crear_usuario_sql)
    var = 1
    #print(var, 'us1')
    #print('finalizo crear_usuario')
    return 1

def validar_usuario_registro(nombreUsuario, correo, passwd):
    #print('llego a validar')
    validar_usuario_registro_sql= f"""
        SELECT * FROM usuario WHERE nombreUsuario = '{nombreUsuario}' OR correo = '{correo}'
"""
    #print('llego antes validar')
    fila=bd.ejecutar_sql(validar_usuario_registro_sql)
    #print('llego a else servidor')
    #print(fila)
    if not fila:
        print('antes crear usuario')
        crear_usuario(nombreUsuario, correo, passwd)
        var = 2
        print(var, 'us2')
        print('finalizo creacion')
        return 2
    else:
        var = 0
        print(var, 'us0')
        return 0






def validar_usuario_login(nombreUsuario):
    validar_usuario_login_sql = f"""
        SELECT passwd FROM usuario WHERE nombreUsuario = {nombreUsuario}
"""
    bd = BaseDeDatos()
    bd.ejecutar_sql(validar_usuario_login_sql)




