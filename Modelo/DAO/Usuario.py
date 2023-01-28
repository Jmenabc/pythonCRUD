"""
Clase que contiene la entidad de la base de datos Usuarios
@author Jmenabc
"""

class Usuario:
    usuario_id = 0
    usuario_nombre = ""
    usuario_apellidos = ""
    usuario_email = ""

    def __init__(self,Usuario_id,Usuario_nombre,Usuario_apellidos,Usuario_email):
        self.usuario_id = Usuario_id
        self.usuario_nombre = Usuario_nombre
        self.usuario_apellidos = Usuario_apellidos
        self.usuario_email = Usuario_email
