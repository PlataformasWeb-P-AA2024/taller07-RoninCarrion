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


file = open('ejemplo02/data/datos_clubs.txt', 'r', encoding='utf-8')

clubs = [line.split(';') for line in file.readlines()]
# clubs = [line.split(';') for line in clubs]
print(clubs)
for nombre, deporte, fundacion in clubs:
    fundacion = int(fundacion)
    club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
    print(club)
    session.add(club)

session.commit()
