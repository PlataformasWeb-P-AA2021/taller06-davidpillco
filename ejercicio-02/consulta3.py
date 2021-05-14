from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Pais
engine = create_engine('sqlite:///basespaises.db')


Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

for pais in paises:
    print("Pais: %s -> Lenguajes: %s" % (pais.pais_nombre, pais.lenguajes))

