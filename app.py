# app.py (ou seu arquivo principal)
from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Suponha que você tenha um modelo User que implemente os métodos do Flask-Login
# Exemplo simplificado:
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def is_active(self):
        return True
    
    def get_id(self):
        return self.id
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False

# Usuários exemplo
users = {'usuario1': User(1, 'usuario1', 'senha123')}

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if str(user.get_id()) == user_id:
            return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = users.get(form.username.data)
        if user and user.password == form.password.data:
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha incorretos.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sessão.', 'info')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return f'Olá, {current_user.username}! Bem-vindo(a).'

if __name__ == '__main__':
    app.run(debug=True)
