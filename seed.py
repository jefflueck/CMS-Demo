from models import User, db
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


db.drop_all()
db.create_all()

heidi = User.register(first_name='Heidi', last_name='Lueck', phone='920-562-0555', email='heidi.lueck@gmail.com', username='Heidi', password='Ironman3731!', is_admin=True)

db.session.add(heidi)
db.session.commit()
