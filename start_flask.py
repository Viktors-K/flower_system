from flask import Flask, request, render_template, redirect, url_for
import csv

csv_name = "C:\\Users\\vvkocetoks\\OneDrive - Rīgas domes izglītības iestādes\\Desktop\\flower_system\\login.csv"
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
        data = read_lines_from_csv(csv_name)
        print(data)
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