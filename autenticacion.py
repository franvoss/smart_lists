import usuario as plantilla_usuario

def validar_usuario_registro(nombreUsuario,correo,passwd):
    #print('llego a autenticacion')
    var = plantilla_usuario.validar_usuario_registro(nombreUsuario,correo,passwd)
    #print('volvio a autenticacion')
    if var == 0:  #Si el return que le llega es 0, el usuario o correo ya existen
        return 0
    elif var == 1:  #Si el return que le llega es 1, se creó el usuario validación no finalizó
        return 1
    elif var == 2: #'''Todo finalizó de forma correcta'''
        return 2
    else:  #
        return "error"


