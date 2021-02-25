import database.db as db
from models.Canciones import Canciones
from models.TipoMusica import TipoMusica
from models.ListaCanciones import ListaCanciones
from datetime import datetime
from sqlalchemy import extract

######################Listar Canción###################################
def get_canciones():
    canciones= db.session.query(Canciones).all()
    db.session.commit()
    return canciones

######################Remover Canción por tipo de musica###################################
def remover_cancion(nombreCancion, id_usuario,tipoMusica_id):

    rowdelete = db.session.query(Canciones).filter(
        Canciones.nombreCancion==nombreCancion,
        Canciones.usuarios_id == id_usuario,
        Canciones.tipoMusica_id == tipoMusica_id).delete()
    db.session.commit()
    return rowdelete

######################Lista  Canción por tipo música###################################
def lista_canciones(idtipoMusica):
    canciones= db.session.query(Canciones).filter(
            Canciones.tipoMusica_id == idtipoMusica
        ).all()
    db.session.commit()
    return canciones