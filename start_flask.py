from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission
        username = request.form['username']
        password = request.form['password']
        # Here you can add your logic to authenticate the user
        if username in users and users[username] == password:
            # Authentication successful, redirect to dashboard
            return redirect(url_for('dashboard'))
        else:
            # Authentication failed, display error message
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)