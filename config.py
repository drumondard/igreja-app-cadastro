import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-segura'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://usuario:senha@host:porta/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
