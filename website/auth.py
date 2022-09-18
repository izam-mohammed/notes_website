
from flask import Blueprint , render_template ,request ,flash , redirect, url_for
from website.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required , logout_user , current_user

auth = Blueprint('auth',__name__)

#login
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST' :
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user :
            if check_password_hash(user.password, password) :
                flash('Logged in successfully !', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incurrect password', category='error')
        else:
            flash('email does not exist ', category='error')
        
    return render_template('login.html', user=current_user)

#logout
@auth.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return render_template('logout.html',user=current_user)

#signup
@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user :
            flash('email already exist',category='error')
        elif len(email) < 4 :
            flash('Email must be atlest 5 characters', category='error')
        elif len(name) < 2 :
            flash('Name must be atleast 3 characters', category='error')
        elif len(password) < 7 :
            flash('Password must be atleast 7 characters', category='error')
        else :
            new_user = User(email=email,name=name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created !',category='success')
            return redirect(url_for('auth.login'))
    
    
    return render_template('signup.html',user=current_user)