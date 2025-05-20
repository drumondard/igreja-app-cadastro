from app import db, User

def init_db():
    # Cria as tabelas no banco de dados (se não existirem)
    db.create_all()

    # Verifica se já existe usuário admin para não duplicar
    if User.query.filter_by(username='admin').first() is None:
        # Cria um usuário inicial
        user = User(username='admin', email='admin@exemplo.com')
        user.set_password('123456')  # Defina a senha que desejar

        # Adiciona e salva no banco
        db.session.add(user)
        db.session.commit()
        print("Usuário admin criado com sucesso.")
    else:
        print("Usuário admin já existe.")

if __name__ == '__main__':
    init_db()
