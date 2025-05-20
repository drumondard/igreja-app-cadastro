# criar_admin.py
from app import app, db
from models import User

with app.app_context():
    # Verifica se já existe um admin
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin')
        admin.set_password('senha_segura123')
        db.session.add(admin)
        db.session.commit()
        print("Usuário admin criado com sucesso.")
    else:
        print("Usuário admin já existe.")
