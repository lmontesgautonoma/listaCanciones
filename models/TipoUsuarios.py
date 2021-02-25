import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class TipoUsuarios(db.Base):
     __tablename__ = 'tipoUsuarios'

     id = Column('idTipoUsuario', String(15), primary_key=True, nullable=False, autoincrement=True)
     nombreTipoUsuario = Column('nombreTipoUsuario', String(20), nullable=False)

     def __init__(self, nombreTipoUsuario):
         self.nombreTipoUsuario = nombreTipoUsuario
     def __repr__(self):
         return f"<TipoUsuarios {self.id}>"