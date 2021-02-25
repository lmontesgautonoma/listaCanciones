import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class TipoMusica(db.Base):
     __tablename__ = 'tipoMusica'
     id = Column('id', Integer, primary_key=True, autoincrement=True)
     nombreTipoMusica = Column('nombreTipoMusica', String(20), nullable=False)
     canciones = relationship('Canciones', back_populates='tipoMusica')

     def __init__(self, nombreTipoMusica):
        #  self.id = idtipomusica
         self.nombreTipoMusica = nombreTipoMusica
     def __repr__(self):
         return f"<TipoMusica {self.id}>"