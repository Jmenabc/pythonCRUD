from Modelo.Consultas.ConsultasPostgreSQL import ConsultasPostgreSQL

#Creamos una instancia de la clase consultas para poder ejecutarlas

consultas = ConsultasPostgreSQL()

#Metemos en una lista los resultados de la lista

#listaUsuarios = consultas.listarUsuarios()

print('añadiendo usuario')
print('Nombre')
nombre = input()
print('apellidos')
apellidos = input()
print('email')
email = input()

consultas.añadirUsuarios(nombre=nombre,apellidos=apellidos,email=email)

