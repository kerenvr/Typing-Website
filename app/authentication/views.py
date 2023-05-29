from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
        #return redirect(url_for('views.home'))

    return render_template("login.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        data = request.form
        print(data)

    return render_template("sign-up.html")


