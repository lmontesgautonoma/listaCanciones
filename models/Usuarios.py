import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class Usuarios(db.Base):
    __tablename__ = 'usuarios'
    id = Column('idUsuario', Integer, primary_key=True, autoincrement=True)
    nombreUsuario = Column('nombreUsuario', String(35), nullable=False)
    idTipoUsuario = relationship("TipoUsuarios", back_populates="usuarios")
    def __init__(self, nombreUsuario):
        self.nombreUsuario = nombreUsuario
        
    def __repr__(self):
        return f"<Usuarios {self.id}>"