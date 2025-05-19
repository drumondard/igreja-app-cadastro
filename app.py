from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuração do banco SQLite (arquivo local)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo do Membro
class Membro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Membro {self.nome}>'

@app.before_first_request
def cria_banco():
    db.create_all()  # Cria as tabelas no banco

@app.route('/')
def index():
    membros = Membro.query.all()
    return render_template('index.html', membros=membros)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        if nome and email:
            # Verifica se email já existe
            if Membro.query.filter_by(email=email).first():
                return "Email já cadastrado.", 400

            novo_membro = Membro(nome=nome, email=email)
            db.session.add(novo_membro)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return "Por favor, preencha todos os campos", 400

    return render_template('cadastro.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
