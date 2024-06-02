from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad Club
clubs = session.query(Club).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Clubs")
for s in clubs:
    print("%s" % (s))
    print("---------")

# Obtener todos los registros de 
# la entidad Jugador
jugadores = session.query(Jugador).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python

print("Jugadores")
for s in jugadores:
    print("%s" % (s))
    print("---------")



