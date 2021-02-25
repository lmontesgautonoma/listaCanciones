import database.db as db
from models.Lista import Lista
from models.Canciones import Canciones
from sqlalchemy import extract

######################Agregar Lista###################################

def register_lista(user_id, first_name):
    usuarios = Usuarios(user_id, first_name, tipousuarios.id)
    db.session.add(usuarios)
    db.session.commit()
    return False

