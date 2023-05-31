from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
        #return redirect(url_for('views.home'))

    return render_template("login.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        flash('Hi')
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be longer than 8 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be at least 2 characters', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        elif password1 != password2: 
            flash('Passwords do not match', category='error')
        else:
            flash('Login successful', category='success')
            return redirect(url_for('views.home'))
        
            
        data = request.form
        print(data)
    return render_template("sign-up.html")


