from flask import Flask, request, render_template, redirect, url_for, session
import csv
import os
import binascii

dirname = os.path.dirname(__file__)
csv_name = os.path.join(dirname, 'login.csv')

def add_line_to_csv(file_path, data):
    with open(file_path, 'a',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
  
def read_lines_from_csv(file_path):
    lines = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(row)
    return lines

def read_users(file_name):
    data = read_lines_from_csv(file_name)
    users = []
    for i in range(0, len(data)):
        temp = data[i]
        user = {}
        user.update({'name': temp[0], 'password': temp[1], 'admin': temp[2]})
        users.append(user)
    return users

def login_required(func):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

app = Flask(__name__)

app.secret_key = binascii.hexlify(os.urandom(24)).decode()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if 'username' not in session:
        if request.method == 'POST':
            # Handle form submission
            username = request.form['username']
            password = request.form['password']
            users = read_users(csv_name)
            is_same = any(user['name'] == username and user['password'] == password for user in users)
            # Here you can add your logic to authenticate the user
            if is_same:
                # Authentication successful, redirect to dashboard
                session['username'] = username
                for user in users:
                    if user['name'] == username:
                        session['admin'] = user.get('admin', False)
                return redirect(url_for('dashboard'))
            else:
                # Authentication failed, display error message
                return render_template('login.html', error='Nepareizs lietotājvārds vai parole')
        else:
            return render_template('login.html')
    else:
        return redirect(url_for('dashboard'))

@login_required
@app.route('/dashboard/')

def dashboard():
    admin = session.get('admin')
    if admin == 'True':
        return render_template('admin_dashboard.html')
    else:
        return render_template('dashman3.html')

if __name__ == '__main__':
    app.run(debug=True)