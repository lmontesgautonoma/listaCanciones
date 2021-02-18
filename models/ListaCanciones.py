import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class ListaCanciones(db.Base):
    __tablename__ = 'listaCanciones'
   
    idTipoMusica = relationship("Lista", back_populates="listaCanciones")
    idUsuario = relationship("Cancion", back_populates="listaCanciones")
       
    def __repr__(self):
        return f"<ListaCanciones {self.id}>"