import database.db as db
from models.Canciones import Canciones
from models.TipoMusica import TipoMusica
from datetime import datetime
from sqlalchemy import extract

######################Agregar Canción###################################
def register_cancion(nombreCancion, duracionCancion, id_usuario):
    tipoMusica= db.session.query(TipoMusica).get('1')
    db.session.commit()
    if tipoMusica == None:
        tipoMusica = TipoMusica('1', 'rock')
        db.session.add(tipoMusica)
        db.session.commit()

    canciones = Canciones(nombreCancion, duracionCancion,id_usuario,tipoMusica.id)
    db.session.add(canciones)
    db.session.commit()
    return True