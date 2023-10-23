import model.package_model.Database as Database
from flask import jsonify
class AspirantesCursos:
    def __init__(self, id_curso, rfc, fecha_registro):
        self.__id_curso=id_curso
        self.__rfc=rfc
        self.__fecha_registro=fecha_registro
    
    @staticmethod    
    def existe_aspirantecursos(id_curso,rfc):
        conexion = conexion = Database.Database()
        aspirantecurso = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT count(*) as ex FROM aspirantes_cursos WHERE ID_CURSO = %s and RFC= %s",(id_curso , rfc))
            aspirantecurso = cursor.fetchone()
        conexion.conn.close()
        #return jsonify(aspirante[0])    
        return aspirantecurso[0]    
    
    def insertar_aspirantecursos(self, obj_asp):
        #return obj_asp.__rfc
        #return obj_asp
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO aspirantes_cursos(ID_CURSO,RFC,FECHA_REGISTRO) VALUES (%s, %s, %s)"
                vals=(obj_asp.__id_curso,obj_asp.__rfc,obj_asp.__fecha_registro)
                #return (query % vals) ver sentencia
                affected=cursor.execute(query,vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: «{}»".format(except_detail))
            finally:
                conexion.conn.close() 
    
    def eliminar_aspirantecursos(self,id_curso,rfc):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM aspirantes_cursos WHERE ID_CURSO = %s and RFC=%s", id_curso,rfc)
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_aspirantecursos(self,id_curso,rfc):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("UPDATE aspirantes_cursos SET ID_CURSO = %s, WHERE ID_CURSO = %s and RFC=%s",id_curso, rfc)
        conexion.conn.commit()
        conexion.conn.close()
        return affected

    def obtener_aspirantescursos(self):
        conexion = Database.Database()
        students = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM aspirantes_cursos")
            students = cursor.fetchall()
        conexion.conn.close()
        return students
    
    def obtener_aspirantescursos_rfc(self,rfc):
        conexion = conexion = Database.Database()
        student = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT * FROM aspirantes_cursos WHERE RFC = %s",rfc)
            student = cursor.fetchone()
        conexion.conn.close()
        return student                