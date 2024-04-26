import os
import urllib.parse

from dotenv import load_dotenv

load_dotenv()

GRPC_HOST = 'localhost'
# GRPC_HOST = '192.168.69.5'
GRPC_PORT = 50051


POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = int(os.getenv('POSTGRES_PORT'))

password_escaped = urllib.parse.quote_plus(POSTGRES_PASSWORD)  # для экранирования пароля со спец. символами


DATABASE_CONFIG = {
    'connections': {
        'default': f'postgres://{POSTGRES_USER}:{password_escaped}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    },
    'apps': {
        'models': {
            'models': ['src.models', 'aerich.models'],  # чтобы находились все файлы с моделями надо из определить в
            #   __init__.py в папке models
            'default_connection': 'default',
        },
    },
}
