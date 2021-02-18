import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Lista(db.Base):
     __tablename__ = 'lista'

     id = Column('idLista', String(15), primary_key=True, nullable=False, autoincrement=True)
     nombreLista = Column('nombreLista', String(20), nullable=False)

     def __init__(self, nombreLista):         
         self.nombreLista = nombreLista
     def __repr__(self):
         return f"<Lista {self.id}>"