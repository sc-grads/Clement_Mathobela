from flask import Blueprint, render_template, request

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')
    
    
@auth.route('/logout')
def logout():
    return "<p>Logged Out!!</p>"
    

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')
        
       
        
    
    return render_template('sign_up.html')