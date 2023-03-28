from flask_wtf import FlaskForm
from sqlalchemy import column
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, TelField
from wtforms.validators import InputRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    """Form for registering a new user."""

    username = StringField("Username", validators=[InputRequired(),Length(min=3, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    first_name = StringField("First Name", validators=[InputRequired(), Length(min=3, max=30)])
    last_name = StringField("Last Name", validators=[InputRequired(), Length(min=3, max=30)])
    phone = StringField("Phone", validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    is_admin = BooleanField("Admin", default=True)
class LoginForm(FlaskForm):
    """Form for logging in."""

    username = StringField("Username", validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
class StudentForm(FlaskForm):
    """Form for adding a new student."""

    first_name = StringField("First Name", validators=[InputRequired(), Length(min=3, max=30)])
    last_name = StringField("Last Name", validators=[InputRequired(), Length(min=3, max=30)])


class EditForm(FlaskForm):
    """Form for editing a user."""

    username = StringField("Username", validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    first_name = StringField("First Name", validators=[InputRequired(), Length(min=3, max=30)])
    last_name = StringField("Last Name", validators=[InputRequired(), Length(min=3, max=30)])
    phone = StringField("Phone", validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[InputRequired(), Email()])


class AdminEditForm(FlaskForm):
    """Form for editing a user."""

    username = StringField("Username", validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    first_name = StringField("First Name", validators=[InputRequired(), Length(min=3, max=30)])
    last_name = StringField("Last Name", validators=[InputRequired(), Length(min=3, max=30)])
    phone = TelField("Phone", validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    is_admin = BooleanField("Admin", default=False)

class MailForm(FlaskForm):
    """Form for sending a mail."""

    subject = StringField("Subject", validators=[InputRequired(), Length(min=3, max=30)])
    body = TextAreaField("Body", validators=[InputRequired()])
