import os
from dotenv import load_dotenv

load_dotenv()
db_user = os.getenv("DB_USER")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")