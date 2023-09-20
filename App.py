from flask import Flask, render_template, request, url_for, flash, redirect
import model.package_model.aspirantes as aspirantes
import model.package_model.Empresa as Empresa
import model.package_model.Curso as Curso
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/aspirante")
def add_aspirante():
    obj_emp= Empresa.Empresa()
    obj_cur= Curso.Curso()
    lista_empresas = obj_emp.obtener_empresas()
    lista_cursos = obj_cur.obtener_cursos()
    return render_template('aspirante.html',lista_empresas=lista_empresas,lista_cursos=lista_cursos)

@app.route("/registra",methods=['POST'])
def registra_aspirante():
    _rfc=request.form['f_rfc'].upper()
    _nom=request.form['f_nombre'].upper()    
    _pat=request.form['f_paterno'].upper()    
    _mat=request.form['f_materno'].upper()    
    _emp=request.form['f_id_empresa']    
    _tel=request.form['f_telefono']    
    _ema=request.form['f_email']    
    _cur=request.form['f_id_curso']
    _fec=datetime.now()
    obj_asp= aspirantes.Aspirantes(_rfc,_nom,_pat,_mat,_emp,_tel,_ema,_fec)
    res=obj_asp.insertar_student(obj_asp)
    #return _rfc+'-'+_nom+'-'+_pat+'-'+_mat+'-'+_emp+'-'+_tel+'-'+_ema+'-'+_cur
    return res

if __name__ == "__main__":
    app.run(debug=True)