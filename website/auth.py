from flask import Blueprint , render_template ,request ,flash , redirect, url_for
from website.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        password = request.form.get('password')
        
        if len(email) < 4 :
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
            return redirect(url_for('views.home'))
    
    
    return render_template('signup.html')