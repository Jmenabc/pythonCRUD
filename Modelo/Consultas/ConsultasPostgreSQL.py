import Modelo.Utils
import psycopg2
from Modelo.Utils.ConexionPostgreSQL import *
"""
Clase que contiene todas las consultas SQL
@author Jmenabc
"""
class ConsultasPostgreSQL:


    def listarUsuarios(self):
        try:
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Haciendo conexion a base de datos")
            con = psycopg2.connect(
                host=HOST,
                database=DATABASE,
                user=USER,
                password=PASSWORD,
                port=PORT
            )
            consulta = 'SELECT * FROM holamundo.Usuario'
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Abriendo conexion")
            cur = con.cursor()
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Ejecutamos la consulta")
            cur.execute(consulta)
            consultaEjecutada = cur.fetchall()
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]: Cerrando conexion a la base de datos")
            con.close()
            return consultaEjecutada

        except Exception as error:
            print("[Modelo-Consultas-ConsultasPostgreSQL-listarUsuario]:", error)


    def añadirUsuarios(self,nombre,apellidos,email):
        print("[Modelo-Consultas-ConsultasPostgreSQL-añadirUsuarios]: Haciendo conexion a base de datos")
        con = psycopg2.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            port=PORT
        )

        consulta = f'INSERT INTO holamundo.usuario (usuario_nombre, usuario_apellidos, usuario_email) VALUES ({nombre},{apellidos}, {email});'
        print("[Modelo-Consultas-ConsultasPostgreSQL-añadirUsuarios]: Abriendo conexion")
        cur = con.cursor()
        print("[Modelo-Consultas-ConsultasPostgreSQL-añadirUsuarios]: Ejecutamos la consulta")
        cur.execute(consulta)
        print("[Modelo-Consultas-ConsultasPostgreSQL-añadirUsuarios]: Cerrando conexion a la base de datos")
        con.close()

