import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class Canciones(db.Base):
    __tablename__ = 'canciones'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nombreCancion = Column('nombreCancion', String(35), nullable=False)
    duracionCancion = Column('duracionCancion', String(5), nullable=False)

    tipoMusica_id = Column('tipoMusica_id', String(15), ForeignKey('tipoMusica.id',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    tipoMusica = relationship("TipoMusica", back_populates="canciones")

    usuarios_id = Column('usuarios_id', Integer, ForeignKey('usuarios.id',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    usuarios = relationship("Usuarios", back_populates="canciones")

    listaCanciones_id = Column('listaCanciones_id', String(15), ForeignKey('listaCanciones.id',onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    listaCanciones = relationship("ListaCanciones", back_populates="canciones")

    def __init__(self,nombreCancion, duracionCancion, usuarioid, tipoMusicaid, listaCancionesid):
        self.nombreCancion = nombreCancion
        self.duracionCancion = duracionCancion
        self.usuarios_id= usuarioid
        self.tipoMusica_id = tipoMusicaid
        self.listaCanciones_id = listaCancionesid
    def __repr__(self):
        return f"<Canciones {self.id}>"