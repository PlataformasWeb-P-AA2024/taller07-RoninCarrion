from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


file = open('ejemplo02/data/datos_jugadores.txt', 'r', encoding='utf-8')

jugadores = [line.split(';') for line in file.readlines()]
# clubs = [line.split(';') for line in clubs]

for club, posicion, dorsal, nombre in jugadores:
    clubJugador = session.query(Club).filter(Club.nombre == club).one()
    dorsal = int(dorsal)
    jugador = Jugador(nombre=nombre, dorsal=dorsal, posicion=posicion, club=clubJugador)
    print(jugador)
    session.add(jugador)

session.commit()
