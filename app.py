
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Coneccion MyAQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'BqCMHW1-'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

#  Configuraciones

app.secret_key = 'mysecretkey'

# Funciones

@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clientes')
    data = cur.fetchall()
    return render_template('index.html', clientes = data)


# Agregar contacto

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        direction = request.form['direction']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO clientes (name, lastname, age, direction) VALUES (%s, %s, %s, %s)', (name,lastname,age,direction))
        mysql.connection.commit()
        flash('Contacto agregado correctamente')
        return redirect(url_for('home'))

# Editar contacto

@app.route('/edit_contact/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clientes WHERE id = {0}'.format(id))
    data = cur.fetchall()
    print(data)
    return render_template('edit_contact.html', contact = data[0])

# Respuesta editar contacto

@app.route('/update/<string:id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        direction = request.form['direction']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE clientes 
        SET name = %s,
            lastname = %s,
            age = %s,
            direction = %s
        WHERE id = %s
        
        """, (name, lastname, age, direction, id))
        mysql.connection.commit()
        flash("Contacto editado")
        return redirect(url_for('home'))


# Eliminar contacto

@app.route('/del_contact/<string:id>')
def del_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM clientes WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado')
    return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run(port = 3000, debug = True)