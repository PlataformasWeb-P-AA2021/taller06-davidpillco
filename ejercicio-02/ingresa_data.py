from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Pais

import json
import requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basespaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
datos_json = (archivo.json())
# print(datos_json)

for d in datos_json:
    p = Pais(pais_nombre=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geoname=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], dependencia=d['is_independent'])
    session.add(p)

# confirmar transacciones
session.commit()
