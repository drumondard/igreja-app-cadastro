from werkzeug.security import generate_password_hash
from app import app, db
from models import User, Membro

def criar_admin():
    with app.app_context():
        # Cria as tabelas se não existirem
        db.create_all()

        # Verifica se já existe o admin
        if User.query.filter_by(username='admin').first():
            print("Usuário admin já existe.")
        else:
            senha_hash = generate_password_hash('admin123')
            admin = User(username='admin', password=senha_hash)
            db.session.add(admin)
            db.session.commit()
            print("Usuário admin criado com sucesso.")

if __name__ == '__main__':
    criar_admin()
