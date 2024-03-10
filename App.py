
from flask import Flask, jsonify, redirect,render_template,request, abort, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import psycopg2
import psycopg2.extras; psycopg2.extensions.set_wait_callback(psycopg2.extras.wait_select)





app = Flask(__name__, template_folder="template")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/Registration', methods = ['GET', 'POST'])
def Registration():
    return render_template("Registration.html")

@app.route('/home', methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

# Add your database URL to create a database object.
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://paragratnaparkhi01:9Z8fQORcyvNk@ep-fragrant-dawn-a5k2hvf1.us-east-2.aws.neon.tech/neondb?sslmode=require"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    with app.app_context():
        db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if username or email already exists
        existing_user = user.query.filter((user.username == username) | (user.email == email)).first()
        if existing_user:
            return "Username or email already exists!"

        # Create a new user
        new_user = user(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))  # Redirect to login page after successful registration

    return render_template('register.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

# @app.route('/registration', methods=['POST'])
# def registration():
#     username = request.form['UserName']
#     company_name = request.form['CompanyName']
#     email = request.form['Email']
#     password = request.form['password']
#     confirm_password = request.form['confirm_password']
#     flash(username,company_name,email,password,confirm_password)  # for debugging purposes only!

#     if not username or not company_name or not email or not password or not confirm_password:
#         flash('All fields are required', 'error')
#         return redirect(url_for('index'))

#     if password != confirm_password:
#         flash('Password and Confirm Password do not match', 'error')
#         return redirect(url_for('index'))

#     new_user = User(username=username, company_name=company_name, email=email, password=password)

#     try:
#         db.session.add(new_user)
#         db.session.commit()
#         flash('Registration successful', 'success')
#         return redirect(url_for('index'))
#     except IntegrityError:
#         db.session.rollback()
#         flash('Username or email already exists', 'error')
#         return redirect(url_for('index'))
#     finally:
#         db.session.close()


#     with app.app_context():
#         db.create_all()  



# if __name__ == '__main__':
#     app.run(debug=True)







# This is my code for Flask application which I am trying to run on Heroku but it's not working and giving me an Application  
#     This is my code for login and registration page. I have created two classes: User and Login. The User class represents data about individual users who can 
# This is my code for login and registration page.
# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()

#     username = data.get('username')
#     company_name = data.get('companyName')
#     email = data.get('email')
#     password = data.get('password')
#     confirm_password = data.get('confirmPassword')

#     if not username or not company_name or not email or not password or not confirm_password:
#         return jsonify({'error': 'All fields are required'}), 400

#     if password != confirm_password:
#         return jsonify({'error': 'Password and Confirm Password do not match'}), 400

#     new_user = User(username=username, company_name=company_name, email=email, password=password)

#     try:
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify({'message': 'Registration successful'}), 201
#     except IntegrityError:
#         db.session.rollback()
#         return jsonify({'error': 'Username or email already exists'}), 400
#     finally:
#         db.session.close()


        

# Create a simple model
# class Book(db.Model):
#     book_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)

# # Commit your model (table) to the database
# with app.app_context():
#     db.create_all()

# @app.route('/add_book', methods=['POST'])
# def add_book():
#     if request.method == 'POST':
#         data = request.get_json()

#         # Validate if the required fields are present in the request
#         if 'title' not in data:
#             return jsonify({'error': 'Missing title'}), 400

#         title = data['title']

#         # Create a new Book instance and add it to the database
#         new_book = Book(title=title)
#         db.session.add(new_book)
#         db.session.commit()
#         return jsonify({'message': 'Book added successfully'}), 201+