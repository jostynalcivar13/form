from flask import render_template, Flask, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app= Flask (__name__)

app.config["MYSQL_HOST"]='localhost'
app.config["MYSQL_USER"]='josty'
app.config["MYSQL_PASSWORD"]='2511'
app.config["MYSQL_BD"]='Deli'
mysql= MySQL(app)

app.secret_key='clavesecreta'

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/agregarUser', methods=['POST'])
def agregarUser():
    if request.method=='POST':
        cedula=request.form['cedula']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        cur=mysql.connection.cursor()
        cur.execute('CREATE DATABASE IF NOT EXISTS Deli')
        cur.execute('CREATE TABLE IF NOT EXISTS Deli.Login (id_User INT AUTO_INCREMENT PRIMARY KEY,  cedula_User char(10) unique,   nombre_User VARCHAR(50),     apellido_User VARCHAR(25))')
        cur.execute('INSERT INTO Deli.Login (cedula_User,nombre_User,apellido_User) VALUES (%s,%s,%s)', (cedula,nombre,apellido))
        mysql.connection.commit()
        cur.close()
        flash("¡Contacto guardado!")
        return redirect(url_for('index'))
         
