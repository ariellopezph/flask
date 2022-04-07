
from flask_mysqldb import MySQL
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'BqCMHW1-'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        direction = request.form['direction']
        cur = mysql.connection.cursor()
        print(cur)
        print(name)
        cur.execute('INSERT INTO clientes (name, lastname, age, direction) VALUES (%s, %s, %s, %s)', (name,lastname,age,direction))
        mysql.connection.commit()
        return 'ok'

@app.route('/edit_contact')
def edit_contact():
    return 'edit contact'

@app.route('/del_contact')
def del_contact():
    return 'del contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)