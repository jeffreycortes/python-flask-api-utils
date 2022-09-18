from enum import Enum, unique

@unique
class TipoRol(Enum):
    Administrador = 1
    Asistente = 2
    Conductor = 3
    Donante = 4
    EnfermeraJefe = 5
    Enfermera = 6
    Medico = 7
    Directivo = 8
