from flask import Flask,url_for,render_template,request,flash,redirect
# import sqlite3

app = Flask(__name__)

# app.config['SECRET_KEY']='clés_flash'

# def connexion():
#     return sqlite3.connect('base.db')


@app.route("/")
def Connect():
    return render_template("Connexion.html")


@app.route("/accueil/")
def accueil():
    return render_template("accueil.html")


if __name__ == "__main__":
    app.run(debug=True)