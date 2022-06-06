from models import User, db
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy



sam = User.register(first_name='Sam', last_name='Smith', phone='111-111-1111', email='samiam@gmail.com', username='Sam', password='mydemoapp', is_admin=True)
frank = User.register(first_name="Frank", last_name="Tank", phone="222-222-2222", email="fankthetank@yahoo.com", username="Frank", password="mydemoapp", is_admin=False)

db.session.add_all([sam, frank])
db.session.commit()
