from enum import Enum, unique

@unique
class EstadoUsuario(Enum):
  Activo = 1
  Bloqueado = 2
  Inactivo = 3
  Cancelado = 4
