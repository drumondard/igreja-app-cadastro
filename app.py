from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

# Inicialização do app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))  # Melhor usar uma variável de ambiente para produção
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa as extensões
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Modelo do usuário administrador
class AdminUser(db.Model):
    __tablename__ = 'admin_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

# Rota principal
@app.route('/')
def index():
    return "Hello, Church Members!"

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = AdminUser.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            session['user_id'] = user.id
            return redirect(url_for('admin_dashboard'))
        flash('Credenciais inválidas.', 'danger')
    return render_template('login.html')

# Dashboard
@app.route('/admin')
def admin_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Você saiu da sessão.', 'info')
    return redirect(url_for('login'))

# Execução local
if __name__ == '__main__':
    app.run(debug=True)
