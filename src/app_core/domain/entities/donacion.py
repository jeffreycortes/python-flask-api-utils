import json
from .estado_donacion import EstadoDonacion
from ..data.persistencia import Persistencia

class Donacion:
    def __init__(self, *initial_data):
        self.id = None
        self.fechaRegistro = None
        self.fechaTomaMuestra = None
        self.identidadUsuario = None
        self.lugarDestino = None
        self.fechaCierre = None
        self.fechaModificacion   = None
        self.identidadUsuarioModificacion = None
        self.estado = None
        self.persistencia = Persistencia()

        self.inicializarData(initial_data)

    def inicializarData(self, initial_data):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])

    def registrarDonacion(self, donacion:any):
        filasAffectadas = self.persistencia.registrarDonacion(donacion) or 0
        return "Donacion creado correctamente" if (filasAffectadas > 0) else "Error: La donación no pudo ser procesada. Por favor intente de nuevo."

    def actualizarDonacion(self, estado):
        return "actualizarDonacion"

    def cancelarDonacion(self, donacionId):
        return "cancelarDonacion"

    def obtenerDonaciones(self, filtros):
        estado = EstadoDonacion.Nueva.value;
        fechaInicio = filtros["fechaInicio"]
        fechaFin = filtros["fechaFin"]
        return self.persistencia.obtenerDonaciones(estado, fechaInicio, fechaFin)
