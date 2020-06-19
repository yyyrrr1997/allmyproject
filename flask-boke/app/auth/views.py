#app/auth/views.py
from flask import render_template,url_for,request,flash,redirect,url_for
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,login_required,logout_user
from . import auth

from ..models import User
from ..import db


@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    #flash('登录成功')
    if form.validate_on_submit():
        user =User.query.filter_by(name=form.username.data,
                password =form.password.data).first()
        if user:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html',title='登录',form=form)

@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register',methods=['GET','POST'])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                name=form.username.data,
                password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('auth.login'))
    return render_template('register.html',
            title='注册',
            form=form)
