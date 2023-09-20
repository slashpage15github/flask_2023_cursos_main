import model.package_model.Database as Database
class Curso:
    def __init__(self, id_curso='', nombre_curso=''):
        self.__id_curso=id_curso
        self.__nombre_curso=nombre_curso
    
    def obtener_cursos(self):
        conexion = Database.Database()
        cursos = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT ID_CURSO,NOMBRE_CURSO FROM catalogo_curso")
            cursos = cursor.fetchall()
        conexion.conn.close()
        return cursos
    
    def obtener_curso_por_id(self,id):
        conexion = conexion = Database.Database()
        curso = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT ID_CURSO,NOMBRE_CURSO FROM catalogo_curso WHERE ID_CURSO = %s", (id))
            curso = cursor.fetchone()
        conexion.conn.close()
        return curso                