from enum import Enum, unique, auto

#constantes
SERVIDOR = "localhost"
BASE_DE_DATOS = "fundacion"
USUARIO = "root"
CLAVE = "$Ping·0n"
PATH_ROOT = 'src/'
PATH_DATA = PATH_ROOT + 'data/'

@unique
class TipoConexion(Enum):
    MsSql = 1
    MySql = 2
    Orcle = 3
    Mongo = 4
    JsonLocal = 5
