import database.db as db
from models.Canciones import Canciones
from datetime import datetime
from sqlalchemy import extract

######################Agregar Canción###################################
def register_cancion(id,nombreCancion, duracionCancion):
    canciones = db.session.query(Canciones).get(id)
    db.session.commit()
    if canciones == None:
        canciones = Canciones(id,nombreCancion, duracionCancion)
        db.session.add(canciones)
        db.session.commit()
        return True
    return False