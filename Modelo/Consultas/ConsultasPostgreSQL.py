import Modelo.Utils
import psycopg2
from Modelo.DAO.Usuario import Usuario
"""
Clase que contiene todas las consultas SQL
@author Jmenabc
"""
class ConsultasPostgreSQL:


    def listarUsuarios(self):
        try:
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Haciendo conexion a base de datos")

            con = psycopg2.connect(
                Modelo.Utils.ConexionPostgreSQL.HOST,
                Modelo.Utils.ConexionPostgreSQL.DATABASE,
                Modelo.Utils.ConexionPostgreSQL.USER,
                Modelo.Utils.ConexionPostgreSQL.PASSWORD,
                Modelo.Utils.ConexionPostgreSQL.PORT
            )
            consulta = 'SELECT * FROM holamundo.Usuario'
            cur = con.cursor()
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Ejecutamos la consulta")
            consultaEjecutada = cur.execute(consulta)
            for row in consultaEjecutada.fetchall():
                print(row[0], row[1])
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Cerrando conexion a la base de datos")
            con.close()

        except Exception as error:
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]:" + error)
