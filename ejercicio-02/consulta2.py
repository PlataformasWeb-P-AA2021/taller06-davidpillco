from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Pais
engine = create_engine('sqlite:///basespaises.db')


Session = sessionmaker(bind=engine)
session = Session()

p_asia = session.query(Pais).filter(Pais.continente == "AS").order_by(Pais.dial).all()
print(p_asia)