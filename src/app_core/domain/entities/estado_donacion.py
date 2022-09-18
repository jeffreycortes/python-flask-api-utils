from enum import Enum, unique

@unique
class EstadoDonacion(Enum):
  Nueva = 1
  Agendada = 2
  Finalizada = 3
  Incumplida = 4
  Cancelada = 5
