import json
from .usuario import Usuario
from ..data.persistencia import Persistencia

class Cuenta:
    def __init__(self):
        primerNombre:str = None
        segundoNombre:str = None
        primerApellido:str = None
        email:str = None
        persistencia:Persistencia = None
        self._perfilUsuario = Usuario()
        self.persistencia = Persistencia()

    def iniciarSesion(self):
        return "iniciando sesión"

    def cerrarSesion(self):
        return "cerrando sesión"

    def registarUsuario(self, usuario:Usuario):
        filasAffectadas = self.persistencia.registarUsuario(usuario) or 0
        return "Usuario crado correctamente" if (filasAffectadas > 0) else "Error: La transacción no pudo ser procesada. Por favor intente de nuevo."

    def auteticarUsuario(self, token):
        #self.persistencia = Persistencia()
        #self.persistencia.EjecutarTransaccion(comando)
        return "auteticarUsuario"
