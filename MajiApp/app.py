from flask import Flask, request, render_template, session, redirect, url_for
from flask import MySQLdb, MySQL


app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "MajiApp_secret_key"
app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'MajiApp'
app.config['MYSQL_PASSWORD'] = 'B@Unix'
app.config['MYSQL_DB'] = 'MajiApp_db'
mysql = MySQL(app)
    
@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login(username, password):
    
    
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = MySQLdb.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'], password=app.config['MYSQL_PASSWORD'], db=app.config['MYSQL_DB']).cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM User_maji WHERE username = %s AND password = %s", (username, password))
        account = cursor.fetchone()
        if account:
            session['logged_in'] = True
            session['id'] = account['id']
            session['username'] = username
            return render_template('index.html')
        else:
            return render_template('login.html', info="invalid password!")
    

    return render_template('login.html')

@app.route('/logout')
def logout():
    
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('id', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)