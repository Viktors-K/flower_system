from flask import Flask, request, render_template

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
        print(f"Username: {username}, Password: {password}")
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)