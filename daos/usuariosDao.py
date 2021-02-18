import database.db as db
from models.Usuarios import Usuarios
from sqlalchemy import extract

######################Agregar Usuarios###################################
def register_usuario(nombreUsuario):
    usuarios= db.session.query(Usuarios)
    db.session.commit()
    if usuarios == None:
        usuarios = Usuarios(nombreUsuario)
        db.session.add(usuarios)
        db.session.commit()
        return True
    return False