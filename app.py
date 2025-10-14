from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/configuracoes')
def configuracoes():
    return render_template('configuracoes.html')

if __name__ == '__main__':
    app.run(debug=True)