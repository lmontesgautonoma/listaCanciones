import database.db as db
from models.TipoMusica import TipoMusica
from sqlalchemy import extract

######################Agregar Tipo Música###################################
def register_tipoMusica(nombreTipoMusica):
    tipoMusica = TipoMusica(nombreTipoMusica)
    db.session.add(tipoMusica)
    db.session.commit()
    return True
######################Listar Tipo de Música###################################
def get_tipoMusica():
    tipoMusica= db.session.query(TipoMusica).all()
    db.session.commit()
    return tipoMusica