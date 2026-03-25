from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'change-this-in-production'  # Required for session support

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password123'

@app.route('/')
def index():
    return 'Hello, World! Your Flask app is running. <a href="/login">Go to Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
