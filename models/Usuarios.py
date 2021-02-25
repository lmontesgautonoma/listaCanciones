import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class Usuarios(db.Base):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nombreUsuario = Column('nombreUsuario', String(35), nullable=False)
    idTipoUsuario =  Column('tipousuario_id', String(15), ForeignKey('tipoUsuarios.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    canciones = relationship("Canciones", back_populates="usuarios")

    def __init__(self, idUsuario, nombreUsuario, tipousuario):
        self.id = idUsuario
        self.nombreUsuario = nombreUsuario
        self.idTipoUsuario = tipousuario

    def __repr__(self):
        return f"<Usuarios {self.id}>"