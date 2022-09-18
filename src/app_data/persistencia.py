import sys
import json
from collections import namedtuple
from .conexion import Conexion
from ..entities.usuario import Usuario
from ..entities.estado_donacion import EstadoDonacion

class Persistencia:
    transaccion = None
    def __init__(self):
        self._conexion = Conexion()

    def formatDate(self, date):
        date = date.replace("T", " ").replace("Z", "")
        return date

    def registarUsuario(self, usuario:Usuario):
        try:
            comando = """INSERT INTO USUARIOS
                        (IdTipoidentidad, Identidad, FechaNacimiento, PrimerNombre, SegundoNombre, PrimerApellido, SegundoApellido, IdTipoRh, Estatura, Peso, Email, DireccionResidencia, DireccionTrabajo, IdRol, FechaRegistro, IdentidadUsuarioRegistro, Clave, IdEstado)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            valores = (usuario.tipoIdentidad
                        ,usuario.identidad
                        ,usuario.fechaNacimiento
                        ,usuario.primerNombre
                        ,usuario.segundoNombre
                        ,usuario.primerApellido
                        ,usuario.segundoApellido
                        ,usuario.rh
                        ,usuario.estatura
                        ,usuario.peso
                        ,usuario.email
                        ,usuario.direccionResidencia
                        ,usuario.direccionTrabajo
                        ,usuario.tipoRol
                        ,usuario.fechaRegistro
                        ,usuario.identidadUsuarioRegistro
                        ,usuario.clave
                        ,usuario.estado
            )
            return self.EjecutarTransaccion(comando, valores)
        except:
            print('Error___:', sys.exc_info()[0])
            return 0

    def registrarDonacion(self, donacion):
        try:
            comando = """INSERT INTO DONACIONES
                        (FechaRegistro, IdentidadUsuarioRegistro, FechaTomaMuestra, IdentidadUsuarioDonante, IdLugarDestino, FechaModificacion, IdentidadUsuarioModificacion, IdEstado)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            valores = (self.formatDate(donacion.fechaRegistro)
                        ,donacion.identidadUsuarioRegistro
                        ,donacion.fechaTomaMuestra
                        ,donacion.identidadUsuarioDonante
                        ,int(donacion.lugarDestino or 1)
                        ,self.formatDate(donacion.fechaModificacion)
                        ,donacion.identidadUsuarioModificacion
                        ,EstadoDonacion.Nueva.value
            )
            return self.EjecutarTransaccion(comando, valores)
        except:
            print('Error___:', sys.exc_info()[0])
            return 0

    def obtenerDonaciones(self, estado, fechaInicio, fechaFin):
        try:
            comando = """SELECT D.FechaRegistro
                            	,D.IdentidadUsuarioRegistro
                            	,D.FechaTomaMuestra
                            	,D.IdentidadUsuarioDonante
                                ,US.PrimerNombre
                                ,US.PrimerApellido
                            	,LD.LugarDestino
                            	,D.FechaModificacion
                            	,D.IdentidadUsuarioModificacion
                            	,ET.Estado
                            FROM DONACIONES D
                            	INNER JOIN USUARIOS US ON US.IDENTIDAD = D.IDENTIDADUSUARIODONANTE
                            	INNER JOIN DONACIONES_P_LUGARES_DESTINO LD ON LD.IDLUGARDESTINO = D.IDLUGARDESTINO
                                INNER JOIN GLOBAL_P_ESTADOS ET ON ET.IDESTADO = D.IDESTADO"""
            return self.EjecutarConsulta(comando)
        except:
            print('Error___:', sys.exc_info()[0])
            return []

    def EjecutarTransaccion(self, comando, valores = ()):
        self._conexion.ejecutarTransaccion(comando, valores)
        return self._conexion.numRows

    def EjecutarConsulta(self,consulta):
        return self._conexion.ejecutarConsulta(consulta)
