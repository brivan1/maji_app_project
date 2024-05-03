from flask import Flask, request, render_template, session, login_required, logout_user

app = Flask(__name__)
app.secret_key = "majiapp"


# @app.route('/')
# def hello():
#     return render_template("login.html")

database = {'brivan': '123', 'karani': '321', 'rio': 'bra3il'}

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        if username in database and database[username] == password:
            session['logged_in'] = True
            session['username'] = username
            return render_template('index.html')
        else:
            return render_template('login.html', info="invalid password!")

        #     if database[username] == password:
        #         return render_template('index.html',info='login successful')
        #     else:
        #         return render_template('login.html',info='invalid password')

    return render_template('login.html')

@app.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)