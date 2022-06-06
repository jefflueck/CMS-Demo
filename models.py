import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    user = db.relationship('Student', backref='user', cascade='all, delete-orphan', single_parent=True)



    @classmethod
    def register(cls, username, password, first_name, last_name, phone, email, is_admin):

        hashed_password = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed_password.decode("utf8")

        return cls(username=username, password=hashed_utf8, first_name=first_name, last_name=last_name, phone=phone, email=email, is_admin=is_admin)

    @classmethod
    def authenticate(cls, username, password):
        """Authenticate user."""
        user = cls.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False



class Student(db.Model):
    """Student."""
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    guardian = db.Column(db.Integer, db.
    ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)




