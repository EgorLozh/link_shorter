import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_HOST = 'postgres'

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(DB_URL)

