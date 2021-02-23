import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Lista(db.Base):
     __tablename__ = 'lista'

     id = Column('id', Integer, primary_key=True, autoincrement=True)
     nombreLista = Column('nombreLista', String(20), nullable=False)
     listaCanciones = relationship('ListaCanciones', back_populates='lista')

     def __init__(self, nombreLista):
         self.nombreLista = nombreLista
     def __repr__(self):
         return f"<Lista {self.id}>"