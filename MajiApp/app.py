from flask import Flask, request, render_template, session, redirect
# from majiapp_main import Storage
# from flask_mysqlbd import MySQLdb
import MySQLdb.cursors
from MySQLdb.cursors import DictCursor
from flask_mysqldb import MySQL
import json
from flask import jsonify

app = Flask(__name__, template_folder='templates', static_folder='../MajiApp/static')
app.secret_key = "MajiApp_secret_key"

app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'MajiApp'
app.config['MYSQL_PASSWORD'] = 'B@Unix'
app.config['MYSQL_DB'] = 'MajiApp_db'

mysql = MySQL(app)
# @app.route('/')
# def index():
#     return "hello"
# @app.route('/login',methods=['GET','POST'])
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin', methods=['GET','POST'])
def adminlogin():
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password'] 

        # Fetch admin credentials from admin.js file
        with open('admin.js') as f:
            admin_credentials = json.load(f)

        if username == admin_credentials['username'] and password == admin_credentials['password']:
            session['loggedin'] = True
            session['username'] = username
            session['password'] = password
            return redirect('/admin_dashboard')
        else:
            return render_template('admin.html')
    return render_template('admin.html')

@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM User_maji WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            session['loggedin'] = True
            session['username'] = ['username']
            session['password'] = ['password']
            return redirect('/dashboard')
        else:
            return render_template('login.html')
        
    
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    if session['username']:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM User_maji WHERE username = %s", (session['username'], ))
        user = cursor.fetchone()
        return render_template('dashboard.html', user=user)
    return redirect('/login.html')

# @app.route('/logout')
# def logout():
    
#     session.pop('loggedin', None)
#     session.pop('username', None)
#     session.pop('id', None)
#     return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)