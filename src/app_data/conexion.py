import sys
import mysql.connector
from .constantes import *

class Conexion:
    numRows:int = 0
    def __init__(self
                ,tipoConexion:TipoConexion = TipoConexion.MySql
                ,nombreServidor:str = SERVIDOR
                ,nombreBaseDatos:str = BASE_DE_DATOS
                ,usuario:str = USUARIO
                ,clave:str = CLAVE
        ):
        self._tipo = tipoConexion
        self._baseDatos = nombreBaseDatos
        self._servidor = nombreServidor
        self._usuario = usuario
        self._clave = clave
        self._cursor = None
        self.inicializarConexion()

    def inicializarConexion(self):
        if self._tipo == TipoConexion.MySql:
            print("Conexion inicializada!!!!!")
            self._mysql = mysql.connector.connect( host = self._servidor
                                                    ,database = self._baseDatos
                                                    ,user = self._usuario
                                                    ,passwd = self._clave
            )


    def inicializarCursor(self):
        if self._tipo == TipoConexion.MySql:
            self._cursor = self._mysql.cursor()

    def ejecutarConsulta(self, consulta):
        data = []
        if self._tipo == TipoConexion.MySql:
            self.inicializarCursor()
            self._cursor.execute(consulta)
            columns = [i[0] for i in self._cursor.description]
            for row in self._cursor:
                data.append(dict(zip(columns, row)))
            data = data
            self.numRows = len(data)
        return data

    def ejecutarTransaccion(self, comando, valores = ()):
        try:
            if self._tipo == TipoConexion.MySql:
                self.inicializarCursor()
                if len(valores) > 0:
                    self._cursor.execute(comando, valores)
                else:
                    self._cursor.execute(comando)

                self.numRows = self._cursor.rowcount
        except:
            print('Error::::::', sys.exc_info()[0])
            return 0
        finally:
            self._cursor.close()
            self._mysql.commit()
            self._mysql.close()
