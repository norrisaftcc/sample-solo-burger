from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'change-this-in-production'  # Required for session support

@app.route('/')
def index():
    return "Hello, World! Your Flask app is running."

VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"


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


if __name__ == '__main__':
    app.run(debug=True)
