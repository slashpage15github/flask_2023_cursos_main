from flask import Flask, render_template, request, url_for, flash, redirect
import model.package_model.aspirantes as aspirantes
import model.package_model.Empresa as Empresa
import model.package_model.Curso as Curso
import model.package_model.AspirantesCursos as AspirantesCursos
from datetime import datetime
#import metodos static
from model.package_model.aspirantes import Aspirantes
from model.package_model.AspirantesCursos import AspirantesCursos
import jsonpickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'j\x86\x14\xcc:\x99\xb3\x91\xf8/Bv\r\xaa"\xf1\x8a\xfa(A\xa1\xe2\x85\xd6'


@app.route("/valida_existe", methods=['GET','POST'])
def valida_aspirante():
    rfc=request.form['f_rfc'].upper()
    cuantos_aspiran=Aspirantes.existe_aspirante(rfc)
    return jsonpickle.encode(cuantos_aspiran)

@app.route("/valida_existe_rfc_curso", methods=['GET','POST'])
def valida_aspirante_rfc_curso():
    rfc=request.form['f_rfc'].upper()
    curso=request.form['f_id_curso']
    cuantos_aspirancursos=AspirantesCursos.existe_aspirantecursos(curso,rfc)
    return jsonpickle.encode(cuantos_aspirancursos)

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
    _cur=request.form['f_id_curso']
    _fec=datetime.now()
    
    cuantos_aspiran=Aspirantes.existe_aspirante(_rfc)
    cuantos_aspirancursos=AspirantesCursos.existe_aspirantecursos(_cur,_rfc)
    if cuantos_aspiran==1:
        if cuantos_aspirancursos==1:
            flash(f"Aspirante y curso ya registrado","Error")
            return redirect(url_for('add_aspirante'))
        else:
            obj_aspcur=AspirantesCursos(_cur,_rfc,_fec)
            res_aspcur=obj_aspcur.insertar_aspirantecursos(obj_aspcur)
            flash(f"Curso agregado correctamente","success")
            return redirect(url_for('add_aspirante'))
    else:
        _nom=request.form['f_nombre'].upper()    
        _pat=request.form['f_paterno'].upper()    
        _mat=request.form['f_materno'].upper()    
        _emp=request.form['f_id_empresa']    
        _tel=request.form['f_telefono']    
        _ema=request.form['f_email']    
        _cur=request.form['f_id_curso']
        _fec=datetime.now()
        obj_asp= aspirantes.Aspirantes(_rfc,_nom,_pat,_mat,_emp,_tel,_ema,_fec)
        res=obj_asp.insertar_aspirante(obj_asp)
        
        obj_aspcur=AspirantesCursos(_cur,_rfc,_fec)
        res_aspcur=obj_aspcur.insertar_aspirantecursos(obj_aspcur)

        #return _rfc+'-'+_nom+'-'+_pat+'-'+_mat+'-'+_emp+'-'+_tel+'-'+_ema+'-'+_cur
        flash(f"Aspirante y curso registrado correctamente","success")
        return redirect(url_for('add_aspirante'))  
        #return render_template('aspirante.html')
        #return res

@app.route("/lista_cursos",methods=["POST","GET"])
def lista_cursos():
    obj_cur= Curso.Curso()
    lista_cursos = obj_cur.obtener_cursos()
    return render_template('lista_cursos.html',lista_cursos=lista_cursos)

if __name__ == "__main__":
    app.run(debug=True)