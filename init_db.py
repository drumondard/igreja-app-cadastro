from app import db, User

# Cria as tabelas no banco (se não existirem)
db.create_all()

# Cria um usuário inicial
user = User(username='admin', email='admin@exemplo.com')
user.set_password('123456')  # senha segura no hash

# Adiciona e salva no banco
db.session.add(user)
db.session.commit()

print("Tabela criada e usuário admin inserido com sucesso!")
