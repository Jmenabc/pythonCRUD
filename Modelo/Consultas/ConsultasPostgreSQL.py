import Modelo.Utils
import psycopg2

"""
Clase que contiene todas las consultas SQL
@author Jmenabc
"""
class ConsultasPostgreSQL:


    def listarUsuarios(self):
        try:
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Haciendo conexion a base de datos")

            con = psycopg2.connect(
                host="localhost",
                database="python",
                user="postgres",
                password="root",
                port=5432
            )
            consulta = 'SELECT * FROM holamundo.Usuario'
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Abriendo conexion")
            cur = con.cursor()
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Ejecutamos la consulta")
            cur.execute(consulta)
            consultaEjecutada = cur.fetchall()
            for row in consultaEjecutada:
                print(row[0], row[1])
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Cerrando conexion a la base de datos")
            con.close()

        except Exception as error:
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]:", error)
