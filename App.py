from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/aspirante")
def add_aspirante():
    return render_template('aspirante.html')

@app.route("/registra",methods=['POST'])
def registra_aspirante():
    _rfc=request.form['f_rfc']
    return _rfc

if __name__ == "__main__":
    app.run(debug=True)