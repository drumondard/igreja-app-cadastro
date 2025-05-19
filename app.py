from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista simples para armazenar membros (exemplo em memória)
membros = []

@app.route('/')
def index():
    return render_template('index.html', membros=membros)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        if nome and email:
            membros.append({'nome': nome, 'email': email})
            return redirect(url_for('index'))
        else:
            return "Por favor, preencha todos os campos", 400

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
