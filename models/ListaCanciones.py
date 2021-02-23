import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class ListaCanciones(db.Base):
    __tablename__ = 'listaCanciones'
    id = Column('id', String(15), primary_key=True, nullable=False)
    nombreListaCancion = Column('nombreListaCancion', String(20), nullable=False)
    canciones = relationship('Canciones', back_populates='listaCanciones')

    def __init__(self, idlistacanciones, nombreListaCancion):
         self.id = idlistacanciones
         self.nombreListaCancion = nombreListaCancion

    def __repr__(self):
        return f"<ListaCanciones {self.id}>"