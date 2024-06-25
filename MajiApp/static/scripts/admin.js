function adminlogin(event) {
    event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        if (username === 'admin' && password === 'adminlogin') {
            alert('Login successful!');
        } else {
            alert('Login failed!');
        }
}
// @app.route('/admin', methods=['GET','POST'])
// def adminlogin():
//     if request.method == "POST" and 'username' in request.form and 'password' in request.form:
//         username = request.form['username']
//         password = request.form['password'] 
//         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
//         cursor.execute("SELECT * FROM User_maji WHERE username = %s AND password = %s", (username, password))
//         user = cursor.fetchone()

//         if user and user['role'] == 'admin':  # Check if the user is an admin
//             session['loggedin'] = True
//             session['username'] = ['username']
//             session['password'] = ['password']
//             return redirect('/admin_dashboard')
//         else:
//             return render_template('admin_login.html')  # Render a different template for admin login
    
//     return render_template('admin_login.html')  # Render a different template for admin login

// @app.route('/admin_dashboard')
// def admin_dashboard():
//     if session['username']:
//         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
//         cursor.execute("SELECT * FROM User_maji WHERE username = %s", (session['username'], ))
//         user = cursor.fetchone()
//         return render_template('admin_dashboard.html', user=user)  # Render a different template for admin dashboard
//     return redirect('/admin_login.html')  # Redirect to admin login page if not logged in

