from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'change-this-in-production'  # Required for session support

@app.route('/')
def index():
    return "Hello, World! Your Flask app is running."

@app.route('/login' , methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Here you would typically validate the credentials
        # For now, we'll just check if they are not empty
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome to your dashboard, {session['username']}!  <a href='/logout'>Logout</a>"
    else:
        return redirect('/login')  
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
if __name__ == '__main__':
    app.run(debug=True)
