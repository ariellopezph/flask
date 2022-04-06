from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)
mysql = MySQL()

@app.route("/")
def home():
    return "no se que paso pero anda"

@app.route('/add_contact')
def add_contact():
    return 'add contact'

@app.route('/edit_contact')
def edit_contact():
    return 'edit contact'

@app.route('/del_contact')
def del_contact():
    return 'del contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)