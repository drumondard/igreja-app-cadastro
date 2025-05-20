from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
import os
from models import db, User, Membro

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user'] = user.username
            return redirect(url_for('admin_dashboard'))
        else:
            error = 'Credenciais inválidas.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/admin')
def admin_dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html', username=session['user'])

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        membro = Membro(nome=nome, email=email, telefone=telefone)
        db.session.add(membro)
        db.session.commit()
        return redirect(url_for('listar'))

    return render_template('cadastro.html')

@app.route('/lista')
def listar():
    if 'user' not in session:
        return redirect(url_for('login'))

    membros = Membro.query.all()
    return render_template('lista.html', membros=membros)

if __name__ == '__main__':
    app.run(debug=True)
