from tokenize import Name
from urllib import request
from flask import Blueprint , render_template ,request ,flash

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
            flash('Account created !',category='success')
    
    
    return render_template('signup.html')