import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class TipoUsuario(db.Base):
     __tablename__ = 'tipoUsuario'
     
     id = Column('idTipoUsuario', String(15), primary_key=True, nullable=False)
     nombreTipoUsuario = Column('nombreTipoUsuario', String(20), nullable=False)
     
     def __init__(self, id, nombreTipoUsuario):
         self.id = id
         self.nombreTipoUsuario = nombreTipoUsuario
     def __repr__(self):
         return f"<TipoUsuario {self.id}>"