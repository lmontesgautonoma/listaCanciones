import database.db as db
from models.Canciones import Canciones
from models.TipoMusica import TipoMusica
from models.ListaCanciones import ListaCanciones
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

    listaCanciones= db.session.query(ListaCanciones).get('1')
    db.session.commit()
    if listaCanciones == None:
        listaCanciones = ListaCanciones('1', 'Mi lista preferida')
        db.session.add(listaCanciones)
        db.session.commit()

    canciones = Canciones(nombreCancion, duracionCancion,id_usuario,tipoMusica.id, listaCanciones.id)
    db.session.add(canciones)
    db.session.commit()
    return True
######################Listar Canción###################################
def get_canciones():
    canciones= db.session.query(Canciones).all()
    db.session.commit()
    return canciones