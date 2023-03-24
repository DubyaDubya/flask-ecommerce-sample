from flask import Flask
import psycopg2
from api.models import Transaction
from settings import db_name, db_user

def create_app(db_name, db_user):
    app = Flask(__name__)

    app.config.from_mapping(
        DB_NAME=db_name,
        DB_USER=db_user
    )

    @app.route('/')
    def root():
        return "The key functionality is on /transactions and /transactions/<id>"
    @app.route('/transactions')
    def transactions():
        conn = psycopg2.connect(database = app.config['DB_NAME'], user = app.config['DB_USER'])
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM raw_transactions ORDER BY index LIMIT 50")

        txns = [Transaction(row).__dict__ for row in cursor.fetchall()]
        return txns

    @app.route('/transaction/<id>')
    def transaction(id):
        conn = psycopg2.connect(database = app.config['DB_NAME'], user = app.config['DB_USER'])
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM raw_transactions WHERE index =  %s", (id,))
        txn = Transaction(cursor.fetchone())
        return txn.__dict__

    return app

        