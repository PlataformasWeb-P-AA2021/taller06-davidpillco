from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Pais
engine = create_engine('sqlite:///basespaises.db')


Session = sessionmaker(bind=engine)
session = Session()

p_americanos = session.query(Pais).filter(Pais.continente == "NA").all()
print(p_americanos)