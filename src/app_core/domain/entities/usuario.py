from .estado_usuario import EstadoUsuario
from .tipo_identidad import TipoIdentidad
from .tipo_rh import TipoRol
from .tipo_rol import TipoRol

class Usuario:
    def __init__(self, *initial_data):
        self.tipoIdentidad = None
        self.identidad = None
        self.fechaNacimiento = None
        self.primerNombre = None
        self.segundoNombre = None
        self.primerApellido = None
        self.segundoApellido = None
        self.rh = None
        self.estatura = None
        self.peso = None
        self.email = None
        self.direccionResidencia = None
        self.direccionTrabajo = None
        self.tipoRol = None
        self.fechaRegistro = None
        self.identidadUsuarioRegistro = None
        self.clave = None
        self.estado = None

        self.inicializarData(initial_data)

    def inicializarData(self, initial_data):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])

    def actualizarUsuario(usuario):
        return "actualizarUsuario"

    def obtenerPerfilUsuario(identidadUsuario):
        return "obtenerPerfilUsuario"
