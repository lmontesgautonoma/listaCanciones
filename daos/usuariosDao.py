import database.db as db
from models.Usuarios import Usuarios
from models.TipoUsuarios import TipoUsuarios
from sqlalchemy import extract

######################Agregar Usuarios###################################
def register_usuario(user_id, first_name):
    usuarios= db.session.query(Usuarios).get(user_id)
    db.session.commit()
    if usuarios == None:
        tipousuarios= db.session.query(TipoUsuarios).get(1)
        db.session.commit()
        if tipousuarios == None:
            tipousuarios = TipoUsuarios(1, 'premiun')
            db.session.add(tipousuarios)
            db.session.commit()

        usuarios = Usuarios(user_id, first_name, tipousuarios.id)
        db.session.add(usuarios)
        db.session.commit()
        return True
    return False