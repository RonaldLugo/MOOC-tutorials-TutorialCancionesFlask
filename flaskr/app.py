from flaskr import create_app
from .modelos import db, Medio, Cancion, Album, Usuario 

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#Prueba 1
""" with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete='Cantante')
    c2 = Cancion(titulo='Prueba2', minutos=2, segundos=25, interprete='Cantante')
    db.session.add(c)
    db.session.add(c2)
    db.session.commit()
    print(Cancion.query.all()) """

#Prueba 2
with app.app_context():
    u = Usuario(nombre_usuario='Juan', contrasena='12345')
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    #c = Cancion(titulo='mi cancion', minutos=1, segundos=15, interprete='Cantante')
    u.albumes.append(a)
    #a.canciones.append(c)
    db.session.add(u)
    #db.session.add(c)
    db.session.commit()
    # validar albumes vs usuarios
    # ver usuarios y los albumes del primer usuario
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    # al borrar el usuario debe borrar sus albumes tambien en cascada
    db.session.delete(u)
    # ya no hay usuarios ni albumes (notar que se consulta la clase Album y no la lista de albumes de usuario)
    print(Usuario.query.all())
    print(Album.query.all())
    db.session.commit()
