# Client Management Software App.

---

This is a app built for the BBGrand Studio business to handle client managment. The intent of the application is for the clients of the BBGrand Piano Studio to be able to create a User profile with critical information needed by the Owner for business functions.

The User then can add there students taking lessons under their profile for the owner. This allows parent, who has User profile to manage their information without the business ower having to keep paper records of their clients.

The owner who is a Admin user can see all Users and Students upon their log in as well as email each User or all Users from the website to save time if needed.

The owner can also update, delete, edit or upgrade users to Admin privilgaes if the business expands to more than one owner.

The owner can also update, or delete individual students if needed.

## User-Flow

1. User registers their information using the register link and inputing all required fields into the form.
2. They are then redirected to a page showing their name and options to use below their name.
3. They can then start to add students.
4. After entering each student they are redirectred back to the user page showing their name and the newly added student.
5. They can add as many students as they want to, their is no limit.

## Admin-Flow

_The software is pre-loaded with a Admin user._

### Admin Login

**Do not delete this user, or you will not be able to see Admin functions.**

- Username: Sam **(case sensitive)**
- Password: mydemoapp **(case sensitive)**

1. The admin logs in with their username and password.
2. They will see list of all students registered by the parent user.
3. They see all users listed below as a second list.
4. The admin is also given an option next to each user to email them directly, or given an option to email all users in a bulk email.
5. The admin can edit, or delete a user which in turn deletes all associated students to that user.
6. The admin can delete individual students, but this does not affect any other students tied to the parent user.

## Tech-stack used

- Python

  - Used for the logic and handeling routes for the view to the user

- Jinja2
  -Jinja used to dynamically render template views for users.

- SQL Database
  - SQLDatabase for storing all data with a many-to-one relationship for the students to their respective user.
  - SQLAlchemy used for CRUD operations to the database

## Fameworks used

- https://pythonhosted.org/Flask-Mail/

  - Used by client to send emails from the app to owner.

- WTForms

  - Used for creating all forms for registering of new users, loging in of users, editing database information, and adding database information.

- Flask-Debugger

  - Used during development for debugging issues.

- SQLAlchemy
  - Used for interfacing new and current database object instances being sent to and from the application for database management.
