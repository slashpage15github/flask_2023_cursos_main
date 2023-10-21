from flask import Flask, render_template, request, url_for, flash, redirect
from model.package_model.aspirantes import Aspirantes
from  . import public

#app = Flask(__name__)

@public.route("/valida_existe", methods=['GET','POST'])
def valida_aspirante():
    rfc=request.form['x_rfc'].upper()
    cuantos_aspiran=Aspirantes.existe_aspirante(rfc)
    print(cuantos_aspiran)