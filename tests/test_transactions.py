from api.models.transactions import Transaction
from settings import db_name, db_user
import psycopg2

#creating a sample row
conn = psycopg2.connect(database= db_name, user = db_user)
cursor = conn.cursor()
cursor.execute("SELECT * FROM raw_transactions WHERE index=2")
record = cursor.fetchone()

def test_transaction():
    txn = Transaction(record)
    assert txn.index == 2
    assert txn.Transaction_id == 14407
    assert txn.Gender == "Female"
    assert txn.City == "Seattle"