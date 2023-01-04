import mysql.connector

#crear una clase para la conexion
class db:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = "localhost",
            type = "mysql",
            user = "root",
            passwd = "",
            database = "mandados"
        )
        self.cursor = self.conexion.cursor()