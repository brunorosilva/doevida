from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('main.html')

@app.route('/about')

def about():

    return render_template('about.html')
    
@app.route('/teste_usuario')

def teste():

    return render_template('teste_usuario.html')

@app.route('/cadastro')

def cadastro():

    return render_template('cadastro.html')

if __name__ == '__main__':

    app.run(debug=True)