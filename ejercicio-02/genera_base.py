from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basespaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    pais_nombre = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    dependencia = Column(String)
    def __repr__(self):
        return "Pais:%s" % (
                          self.pais_nombre)
   

Base.metadata.create_all(engine)

