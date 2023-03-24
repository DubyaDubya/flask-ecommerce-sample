from settings import db_user, db_name
from api import create_app

app = create_app(db_name=db_name, db_user=db_user)
app.run(debug = True)