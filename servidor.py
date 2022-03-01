from flask import Flask, request, render_template,redirect
import autenticacion
#from usuario import var

app= Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login_page():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup_page():
    return render_template('signup.html')

@app.route('/crearUsuario', methods=['GET','POST'])
def crear_usuario():
    if request.form['passwd'] != request.form['confirm']:
        return 'Las contraseñas no coinciden', 412
    else:
        #print('llego a else servidor') -
        aux=autenticacion.validar_usuario_registro(request.form['nombreUsuario'], request.form['correo'],request.form['passwd'])
        #print('llego a antes del if return')
        if aux == 2:  #registro correcto
            #print(aux,'aux2')
            return redirect('/')
        elif aux == 0:
            #print(aux,'aux0')
            return 'El usuario ya existe o el correo ya se encuentra registrado',412
        else:
            #print(aux,'auxrand')
            return 'Error inesperado',412


if __name__ == '__main__':
    app.debug = True
    app.run()