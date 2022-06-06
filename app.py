from flask import Flask, request, render_template, redirect, flash, session, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import null
from models import db, connect_db, User, Student
from forms import EditForm, RegisterForm, LoginForm, StudentForm, AdminEditForm, MailForm
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)



bcrypt = Bcrypt()
app.config.from_object(__name__)
uri = os.environ.get('DATABASE_URL', 'postgresql:///cms-demo')# or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

# the toolbar is only enabled in debug mode:
app.debug = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','asecretkey31903748')


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = None # your email address would go here in real application
app.config['MAIL_PASSWORD'] = None# your app generated password would go here in real application
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_MAX_EMAILS'] = None
mail = Mail(app)




toolbar = DebugToolbarExtension(app)


connect_db(app)
db.create_all()


@app.route('/')
def show_homepage():
  return render_template('landing_page.html')

@app.route('/register', methods=['GET','POST'])
def show_register_form():
  form = RegisterForm()
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    first_name = form.first_name.data
    last_name = form.last_name.data
    phone = form.phone.data
    email = form.email.data
    user = User.register(username=username, password=password, first_name=first_name, last_name=last_name, phone=phone, email=email, is_admin=False)
    db.session.add(user)
    db.session.commit()
    session['user_id'] = user.id
    return redirect(f'/user/{user.id}/view')

  return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def show_login_form():
  form = LoginForm()
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    user = User.authenticate(username, password)
    session['user_id'] = user.id
    return redirect(f'/user/{user.id}/view')

  return render_template('login.html', form=form)

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')


@app.route('/user/<int:user_id>/view')
def show_user(user_id):
  user = User.query.get_or_404(session['user_id'])
  if user.is_admin:
    students = Student.query.all()
    users = User.query.all()
    return render_template('admin.html', students=students, users=users,user=user)
  else:
    students = Student.query.filter_by(guardian=user_id).all()
  return render_template('user.html', user=user, students=students,)

@app.route ('/user/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
  user = User.query.get_or_404(session['user_id'])
  if user.is_admin:
    form = AdminEditForm()
  else:
    form = EditForm()
  if form.validate_on_submit():
    user.username = form.username.data
    user.password = form.password.data
    hashed_password = bcrypt.generate_password_hash(form.password.data)
    hashed_utf8 = hashed_password.decode("utf8")
    user.password = hashed_utf8
    user.first_name = form.first_name.data
    user.last_name = form.last_name.data
    user.phone = form.phone.data
    user.email = form.email.data
    db.session.commit()
    return redirect(f'/user/{user.id}/view')

  return render_template('edit_user.html', form=form, user=user)


@app.route('/user/<int:user_id>/delete', methods=['GET', 'POST'])
def delete_user(user_id):
  user = User.query.get_or_404(session['user_id'])
  Student.query.filter_by(guardian=user_id).delete()
  db.session.delete(user)
  db.session.commit()
  return redirect('/')



@app.route('/add/student', methods=['GET', 'POST'])
def add_student():
  user = User.query.get_or_404(session['user_id'])
  form = StudentForm()
  if form.validate_on_submit():
    first_name = form.first_name.data
    last_name = form.last_name.data

    student = Student(first_name=first_name, last_name=last_name, guardian=session['user_id'])
    db.session.add(student)
    db.session.commit()
    return redirect(f'/user/{user.id}/view')

  return render_template('add_student.html', form=form)

@app.route('/student/<int:student_id>/edit', methods=['GET', 'POST'])
def edit_student(student_id):
  user = User.query.get_or_404(session['user_id'])
  student = Student.query.get_or_404(student_id)
  form = StudentForm()
  if form.validate_on_submit():
    student.first_name = form.first_name.data
    student.last_name = form.last_name.data
    db.session.add(student)
    db.session.commit()
    return redirect(f'/user/{user.id}/view')

  return render_template('edit_student.html', form=form, student=student)

@app.route('/student/<int:student_id>/delete', methods=['GET', 'POST'])
def delete_student(student_id):
  user = User.query.get_or_404(session['user_id'])
  student = Student.query.get_or_404(student_id)
  db.session().delete(student)
  db.session.commit()
  return redirect(f'/user/{user.id}/view')

@app.route('/mail/<int:user_id>/outgoing', methods=['GET','POST'])
def mail_outgoing(user_id):
  user = User.query.get_or_404(session['user_id'])
  form = MailForm()
  if form.validate_on_submit():
    subject = form.subject.data
    body = form.body.data
    email = User.query.get_or_404(user_id)
    msg = Message(subject=subject, body=body, sender=f'{user.first_name} {user.last_name}', recipients=[email.email])
    mail.send(msg)
    return redirect(f'/user/{user.id}/view')

  return render_template('mail_outgoing.html', form=form, user=user)

@app.route('/mail/outgoing/all', methods=['GET','POST'])
def mail_outgoing_all_users():
  user = User.query.get_or_404(session['user_id'])
  users = User.query.all()
  form = MailForm()
  if form.validate_on_submit():
    with mail.connect() as conn:
      for user in users:
        subject = form.subject.data
        body = form.body.data
        email = User.query.get_or_404(user.id)
        msg = Message(subject=subject, body=body, sender=f'{user.first_name} {user.last_name}', recipients=[email.email])
        conn.send(msg)
    return redirect(f'/user/{user.id}/view')

  return render_template('mail_outgoing.html', form=form, users=users,user=user)



