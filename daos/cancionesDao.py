import database.db as db
from models.Canciones import Canciones
from models.TipoMusica import TipoMusica
from models.ListaCanciones import ListaCanciones
from datetime import datetime
from sqlalchemy import extract

######################Agregar Canción###################################
def register_cancion(nombreCancion, duracionCancion, id_usuario,tipoMusica_id):
    listaCanciones= db.session.query(ListaCanciones).get('1')
    db.session.commit()
    if listaCanciones == None:
        listaCanciones = ListaCanciones('1', 'Mi lista preferida')
        db.session.add(listaCanciones)
        db.session.commit()

    canciones = Canciones(nombreCancion, duracionCancion,id_usuario,tipoMusica_id, listaCanciones.id)
    db.session.add(canciones)
    db.session.commit()
    return True
######################Listar Canción###################################
def get_canciones():
    canciones= db.session.query(Canciones).all()
    db.session.commit()
    return canciones
######################Buscar Canción###################################
def find_canciones(nombreCancion):
    canciones= db.session.query(Canciones).filter(
            Canciones.nombreCancion == nombreCancion
        ).first()
    db.session.commit()
    return canciones
######################Lista  Canción por tipo música###################################
def lista_canciones(idtipoMusica):
    canciones= db.session.query(Canciones).filter(
            Canciones.tipoMusica_id == idtipoMusica
        ).all()
    db.session.commit()
    return canciones
