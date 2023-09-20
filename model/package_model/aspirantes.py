import model.package_model.Database as Database
class Aspirantes:
    def __init__(self, rfc, nombre, paterno, materno,id_empresa, telefono, email, fecha_registro):
        self.__rfc=rfc
        self.__nombre=nombre
        self.__paterno=paterno
        self.__materno=materno
        self.__id_empresa=id_empresa
        self.__telefono=telefono
        self.__email=email
        self.__fecha_registro=fecha_registro
    
    def insertar_student(self, obj_asp):
        #return obj_asp.__rfc
        #return obj_asp
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query="INSERT INTO aspirantes(RFC,ID_EMPRESA,NOMBRE,PATERNO,MATERNO,TELEFONO,EMAIL,FECHA_REGISTRO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                vals=(obj_asp.__rfc,obj_asp.__id_empresa, obj_asp.__nombre, obj_asp.__paterno,obj_asp.__materno,obj_asp.__telefono,obj_asp.__email,obj_asp.__fecha_registro)
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
    
    def eliminar_student(self,id):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM student WHERE NAME = %s", (id))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_student(self, bra, rol,sec,age,nom ):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected=cursor.execute("UPDATE student SET BRANCH = %s, ROLL = %s, SECTION = %s, AGE = %s WHERE NAME = %s",
                       (bra, rol, sec, age, nom))
        conexion.conn.commit()
        conexion.conn.close()
        return affected

    def obtener_students(self):
        conexion = Database.Database()
        students = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT name, branch, roll, section, age FROM student")
            students = cursor.fetchall()
        conexion.conn.close()
        return students
    
    def obtener_student_por_id(self,id):
        conexion = conexion = Database.Database()
        student = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT NAME, BRANCH, ROLL, SECTION, AGE FROM student WHERE NAME = %s", (id))
            student = cursor.fetchone()
        conexion.conn.close()
        return student                