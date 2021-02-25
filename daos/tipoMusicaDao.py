######################Listar Tipo de Música###################################
def get_tipoMusica():
    tipoMusica= db.session.query(TipoMusica).all()
    db.session.commit()
    return tipoMusica