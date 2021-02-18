import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class Canciones(db.Base):
    __tablename__ = 'canciones'
    id = Column('id', String(15), primary_key=True, nullable=False)
    nombreCancion = Column('nombreCancion', String(35), nullable=False)
    duracionCancion = Column('nombreCancion', String(5), nullable=False)
    idTipoMusica = relationship("TipoMusica", back_populates="canciones")
    idUsuario = relationship("Usuarios", back_populates="canciones")
    def __init__(self,id,nombreCancion, duracionCancion):
        self.id = id
        self.nombreCancion = nombreCancion
        self.duracionCancion = duracionCancion
        
    def __repr__(self):
        return f"<Canciones {self.id}>"