from ast import main
from urllib import request
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password'
app.config['MYSQL_DB'] = 'dataformulario'
mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM datos')
    data = cur.fetchall()
    return render_template('index.html', datos = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        city = request.form['city']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO datos (fullname, email, city) VALUES (%s, %s, %s)',
        (fullname, email, city))
        mysql.connection.commit()
#        flash ('Datos Almacenados con Éxito')
        return redirect(url_for('Index'))
    return 'add_contact'

if __name__ == '__main__':
    app.run (port=3000, debug=True)