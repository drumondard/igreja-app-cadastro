from models import db, User
from werkzeug.security import generate_password_hash
from app import app

with app.app_context():
    db.create_all()

    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', password=generate_password_hash('admin123'))
        db.session.add(admin)
        db.session.commit()
        print("Usuário admin criado.")
    else:
        print("Usuário admin já existe.")
