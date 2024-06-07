import pytest
from flask import Flask
from flask_mysqldb import MySQL
from index import app as flask_app

@pytest.fixture(scope='module')
def app():
    flask_app.config['TESTING'] = True
    flask_app.config["MYSQL_HOST"] = 'localhost'
    flask_app.config["MYSQL_USER"] = 'josty'
    flask_app.config["MYSQL_PASSWORD"] = '2511'
    flask_app.config["MYSQL_DB"] = 'Deli'
    return flask_app

@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def mysql(app):
    mysql = MySQL(app)
    with app.app_context():
        yield mysql

def test_agregar_usuario_exitoso(client, mysql):
    # Datos de prueba
    cedula = '1234567890'
    nombre = 'Alexander'
    apellido = 'López'

    cur = mysql.connection.cursor()    
    # Enviar solicitud POST al formulario
    response = client.post('/agregarUser', data={
        'cedula': cedula,
        'nombre': nombre,
        'apellido': apellido
    }, follow_redirects=True)
    
   # Verificar que no se agregó un segundo usuario con la misma cédula
    cur.execute('SELECT COUNT(*) FROM Deli.Login WHERE cedula_User = %s', (cedula,))
    count = cur.fetchone()[0]
    assert count == 1
    cur.close()

def test_agregar_usuario_cedula_duplicada(client, mysql):
    # Datos de prueba
    cedula = '1234567890'
    nombre = 'Jostyn'
    apellido = 'Alcivar'

    cur = mysql.connection.cursor()    
    # Enviar solicitud POST al formulario
    response = client.post('/agregarUser', data={
        'cedula': cedula,
        'nombre': nombre,
        'apellido': apellido
    }, follow_redirects=True)
    
    # Verificar que no se agregó un segundo usuario con la misma cédula
    cur.execute('SELECT COUNT(*) FROM Deli.Login WHERE cedula_User = %s', (cedula,))
    count = cur.fetchone()[0]
    assert count == 1
    cur.close()
