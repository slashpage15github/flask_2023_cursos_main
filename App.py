from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/aspirante")
def add_aspirante():
    return render_template('aspirante.html')

if __name__ == "__main__":
    app.run(debug=True)