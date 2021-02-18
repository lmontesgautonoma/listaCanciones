import database.db as db
from models.TipoMusica import TipoMusica
from sqlalchemy import extract

######################Agregar Canción###################################
def register_tipoMusica():
    tipoMusica = db.session.query(TipoMusica)
    db.session.commit()
    if tipoMusica == None:
        tipoMusica = TipoMusica("Vallenato")
        db.session.add(tipoMusica)
        db.session.commit()
        return True
    return False