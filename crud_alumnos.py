import crud_academica
db = crud_academica.crud()

class crud_alumnos:
    def consultar_alumnos(self, buscar):
        return db.consultar("select * from clientes where nombre like'%"+ buscar["buscar"] 
            +"%' or apellido like'%"+ buscar["buscar"] +"%'")
    
    def administrar(self, alumnos):
        if alumnos["accion"] == "nuevo":
            sql = """
                INSERT INTO clientes (nombre, apellido, dui, telefono)
                VALUES (%s, %s, %s, %s)
            """
            val = (alumnos["nombre"], alumnos["apellido"], alumnos["dui"], alumnos["telefono"])
        elif alumnos["accion"] == "modificar":
            sql = """
                UPDATE clientes
                    SET nombre=%s, apellido=%s, dui=%s, telefono=%s
                WHERE idCliente=%s
            """
            val = (alumnos["nombre"], alumnos["apellido"], alumnos["dui"], alumnos["telefono"], alumnos["idCliente"])
        elif alumnos["accion"] == "eliminar":
                sql = """
            DELETE FROM clientes
            WHERE idCliente=%s
        """
        val = (alumnos["idCliente"],)
        return db.ejecutar_consultas(sql, val)






