import model.package_model.Curso as Curso
obj_curso = Curso.Curso()
lista_cursos = obj_curso.obtener_cursos()
if lista_cursos!=None:
    for x in lista_cursos:
        print(x)
else:
    print("No se encontraron datos de estudiantes")