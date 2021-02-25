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