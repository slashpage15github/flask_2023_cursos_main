import model.package_model.Databasex as Databasex
class Student :
    def insertar_student(self, nom, bra, rol,sec,age):
        conexion = Databasex.Databasex()
        with conexion.cursor as cursor:
            affected=cursor.execute("INSERT INTO student(name, branch, roll, section, age) VALUES (%s, %s, %s, %s, %s)",
                        (nom, bra, rol,sec,age))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def eliminar_student(self,id):
        conexion = Databasex.Databasex()
        with conexion.cursor as cursor:
            affected=cursor.execute("DELETE FROM student WHERE NAME = %s", (id))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_student(self, bra, rol,sec,age,nom ):
        conexion = Databasex.Databasex()
        with conexion.cursor as cursor:
            affected=cursor.execute("UPDATE student SET BRANCH = %s, ROLL = %s, SECTION = %s, AGE = %s WHERE NAME = %s",
                       (bra, rol, sec, age, nom))
        conexion.conn.commit()
        conexion.conn.close()
        return affected

    def obtener_students(self):
        conexion = Databasex.Databasex()
        students = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT name, branch, roll, section, age FROM student")
            students = cursor.fetchall()
        conexion.conn.close()
        return students
    
    def obtener_student_por_id(self,id):
        conexion = conexion = Databasex.Databasex()
        student = None
        with conexion.cursor as cursor:
            cursor.execute(
                "SELECT NAME, BRANCH, ROLL, SECTION, AGE FROM student WHERE NAME = %s", (id))
            student = cursor.fetchone()
        conexion.conn.close()
        return student                