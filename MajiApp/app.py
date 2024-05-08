import flask
from flask import Flask, request, render_template, session, redirect, url_for
import MySQLdb


# user = "bunix"
# password = "B@Unix"
# host = "localhost"
# dbname = "MajiApp_db"


app = Flask(__name__)
app.secret_key = "MajiApp_secret_key"
app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'bunix'
app.config['MYSQL_PASSWORD'] = 'B@Unix'
app.config['MYSQL_DB'] = 'MajiApp_db'


#login manager configuration
# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
    # return (int(user_id))

# @app.route('/')
# def hello():
#     return render_template("login.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = MySQLdb.connection.cursor()
        cursor.execute("SELECT * FROM User_main WHERE username = %s AND password = %s", (username, password))
        account = cursor.fetchone()
        if account:
            session['logged_in'] = True
            session['username'] = username
            return render_template('index.html')
        else:
            return render_template('login.html', info="invalid password!")
    #     if username in db and db[username] == password:
    #         session['logged_in'] = True
    #         session['username'] = username
    #         return render_template('index.html')
    #     else:
    #         return render_template('login.html', info="invalid password!")

        #     if database[username] == password:
        #         return render_template('index.html',info='login successful')
        #     else:
        #         return render_template('login.html',info='invalid password')

    # return render_template('login.html')

@app.route('/logout')
def logout():
    
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('id', None)
    return redirect(url_for('login'))
#     logout_user()
#     return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)