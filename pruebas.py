import pytest
from flask import Flask
from flask_mysqldb import MySQL

def datosTestN_correcto(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre_User FROM Login where cedula_User="1206678623";')
    nombre = cur.fetchone()  
    return nombre[0]

def datosTestA_correcto(mysql): 
    cur = mysql.connection.cursor()  
    cur.execute('SELECT apellido_User FROM Login WHERE cedula_User="1206678623";')
    apellido = cur.fetchone()  
    return apellido[0]

def datosTestN_incorrecto(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre_User FROM Login where cedula_User="1250532478";')
    nombre = cur.fetchone()  
    return nombre[0]

def datosTestA_incorrecto(mysql): 
    cur = mysql.connection.cursor()  
    cur.execute('SELECT apellido_User FROM Login WHERE cedula_User="1250532478";')
    apellido = cur.fetchone()  
    return apellido[0]

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    app.config["MYSQL_HOST"] = 'localhost'
    app.config["MYSQL_USER"] = 'josty'
    app.config["MYSQL_PASSWORD"] = '2511'
    app.config["MYSQL_DB"] = 'Deli'
    app.config["MYSQL_PORT"] = 3306
    return app

@pytest.fixture(scope='module')
def mysql(app):
    mysql = MySQL(app)
    with app.app_context():
        yield mysql

def test_datos_correctos(mysql):
    assert datosTestN_correcto(mysql) == "Arianna Misaely"
    assert datosTestA_correcto(mysql) == "Aspiazu Sánchez"


def test_datos_incorrecto(mysql):
    assert datosTestN_incorrecto(mysql) == "Jostyn"
    assert datosTestA_incorrecto(mysql) == "Alcivar Montesdeoca"