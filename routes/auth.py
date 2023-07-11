import logging
from flask import Flask, render_template, request, url_for, flash, get_flashed_messages, jsonify, make_response, redirect, session
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user 
from config import app, db
from models.user import User
from flask_bcrypt import Bcrypt
from datetime import datetime
from models.user import User

bcrypt = Bcrypt()
logging.basicConfig(level=logging.DEBUG)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/user/dashboard', methods=['GET', 'POST'], endpoint='dashboard')
@login_required
def user_dashboard():
    #user = User.query.filter(User.user_id).first()
    # user = User.query.all()
    user = current_user
    flash('Logged in successfully!')
    return render_template('dashboard.html', user=user)






@app.route('/hiring', methods=['GET'])
def hiring():
    return render_template('/hiring.html')


'''the user sign up route'''
@app.route('/auth/signup', methods=["POST","GET"])
def userSignup():
    if request.method == "POST":
        '''collect the information from the html form'''
        userform = request.form
        username = userform["Username"]
        email = userform["Email"]
        country = userform["Country"]
        address = userform["Address"]
        password = userform["Password"]

        if not username or not email or not password or not country or not address:
            flash("All fields should be filled")
            return render_template('/signup.html')
        
        pwd_hash = bcrypt.generate_password_hash(password, 8).decode('utf8')

        newUser = User(username=username, email=email, password=pwd_hash, country=country, address=address)
        try:
            db.session.add(newUser)
            db.session.commit()
            flash("User created successfully")
            return render_template('/login.html')
        except Exception as e:
            db.session.rollback()
            logging.error(e)
            existingUser = db.session.query(User).filter(User.email == email).first()
            if existingUser is not None:
                flash(f"user with the email: {email} already exists")
            else:
                flash("An error occurred while creating the user")
            return render_template('/signup.html')
            
    return render_template('/signup.html')



'''Login Route'''
@app.route('/auth/login', methods=["GET", "POST"], endpoint="user_login_view")
def user_login():
    if request.method == 'POST':
        # collect login email and password
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('All fields are required')
            return render_template('login.html')

        # Check if user with given email exists in database
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Invalid email or password')
            return render_template('login.html')

        # Check if given password matches the hashed password in database
        if bcrypt.check_password_hash(user.password, password):
            user.last_login = datetime.utcnow()
            db.session.commit()
            # login user
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Wrong Password - Try Again!')
    # GET request
    return render_template('login.html')

            

'''Logout Route'''
@app.route('/auth/logout', methods=["GET","POST"])
@login_required
def user_logout():
    logout_user()
    session.pop('message', None)
    flash('logged out successfully')
    return redirect(url_for('user_login_view'))