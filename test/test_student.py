import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import model.package_model.student as Student
obj_student = Student.Student()

#insert
# result=obj_student.insertar_student("DAVID", "HOLA", 100,"A",49)
# if result==1:
#     print("El estudiante fue registrado con éxito")
# else:
#     print("No se pudo registrar el estudiante")
    
    
#delete
# result_del=obj_student.eliminar_student("sita")
# if result_del>=1:
#     print("El estudiante fue borrado con éxito")
# else:
#     print("No se pudo eliminar el estudiante")

#update
# result_upd=obj_student.actualizar_student("ISC",100,"X",5,"Anil")
# if result_upd>=1:
#     print("El estudiante fue actualizado con éxito")
# else:
#     print("No se pudo actualizado el estudiante")

#trae todos
# result_all=obj_student.obtener_students()
# if result_all!=None:
#     for x in result_all:
#         print(x)
# else:
#     print("No se encontraron datos de estudiantes")
    
#trae POR id
result_one=obj_student.obtener_student_por_id("Anil")
if result_one!=None:
    for x in result_one:
        print(x)
else:
    print("No se encontraron al estudiante")    