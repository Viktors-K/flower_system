from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/registret', methods=['GET'])
#def registret():
 #   username = request.args.get('username')
 #   password = request.args.get('password')
#
    # Saglabā lietotāja datus teksta failā
 #   with open('lietotaji.txt', 'a') as file:
 #       file.write(f'Lietotājvārds: {username}, Parole: {password}\n')
#
 #   return 'Reģistrācija veiksmīga!'

if __name__ == '__main__':
    app.run(debug=True)