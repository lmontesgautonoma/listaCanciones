import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class TipoMusica(db.Base):
     tablename = 'tipoMusica'
     id = Column('id', Integer, primary_key=True, autoincrement=True)
     nombreTipoMusica = Column('nombreTipoMusica', String(20), nullable=False)
     canciones = relationship('Canciones', back_populates='tipoMusica')

     def init(self, nombreTipoMusica):
        #  self.id = idtipomusica
         self.nombreTipoMusica = nombreTipoMusica
     def repr(self):
         return f"<TipoMusica {self.id}>"