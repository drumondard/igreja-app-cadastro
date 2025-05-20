from werkzeug.security import generate_password_hash
from models import db, User
from app import app  # importa seu app Flask

def criar_admin():
    with app.app_context():
        username = input("Digite o username do admin: ")
        senha = input("Digite a senha do admin: ")

        # Verifica se já existe o usuário
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print("Usuário já existe!")
            return

        senha_hash = generate_password_hash(senha)
        admin = User(username=username, password=senha_hash)

        db.session.add(admin)
        db.session.commit()
        print("Usuário admin criado com sucesso!")

if __name__ == "__main__":
    criar_admin()
