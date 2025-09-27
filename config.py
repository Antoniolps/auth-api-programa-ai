import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config: 
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'dev-secret')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    API_KEYS = os.environ.get('API_KEYS', 'dev-key')
    API_KEY_HEADER = os.environ.get('API_KEY_HEADER', 'X-API-Key')