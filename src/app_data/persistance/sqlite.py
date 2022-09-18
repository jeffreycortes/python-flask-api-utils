import sqlite3

class Sqlite:
    def __init__(self, databaseName = 'local.db'):
        self._databaseName = databaseName
        self._connection = sqlite3.connect(self._databaseName)
        self._connection.row_factory = sqlite3.Row
        self.__cursor = None

    def getCursor(self):
        self.__cursor = self._connection.cursor()
        return self.__cursor

    def commit(self):
        self.connection.commit()

    def createTable(self):
        cursor = self.getCursor()
        cursor.execute('CREATE TABLE TEST (ID TEXT, NAME TEXT)')
        cursor.close()
        return 'create'

    def insertTest(sel):
        cursor.execute("INSERT INTO TEST VALUES (1,'TEST')")

    def read(self):
        cursor = self.getCursor()
        cursor.execute("SELECT * FROM TEST")
        rows = cursor.fetchall()
        for row in rows:
            r = dict(row)
            print(r)
        return 'read'

    def update(self):
        return 'update'

    def delete(self):
        return 'delete'
