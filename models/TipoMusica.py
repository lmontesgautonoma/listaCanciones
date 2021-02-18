import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class TipoMusica(db.Base):
     __tablename__ = 'tipoMusica'

     id = Column('idTipoMusica', String(15), primary_key=True, nullable=False, autoincrement=True)
     nombreTipoMusica = Column('nombreTipoMusica', String(20), nullable=False)

     def __init__(self, nombreTipoMusica):         
         self.nombreTipoMusica = nombreTipoMusica
     def __repr__(self):
         return f"<TipoMusica {self.id}>"