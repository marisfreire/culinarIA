from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from app.blueprints.auth import auth_bp
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from app.models.users import User


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
   
    if current_user.is_authenticated:
        return redirect(url_for('menu.menu'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        remember = True if request.form.get('remember') else False
        
        user = User.objects(email=email).first()
        
        if not user or not user.check_password(password):
            flash('Por favor, verifique seus dados e tente novamente.', 'error')
            return redirect(url_for('auth.login'))
            
        login_user(user, remember=remember)

        return redirect(url_for('menu.menu'))
        
    return render_template('login/login.html')


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        email =    request.form.get('email')
        password = request.form.get('password')
        name =     request.form.get('name')
        
        if User.collection.find_one({"email": email}):
            flash('Email já registrado.', 'error')
            return redirect(url_for('auth.signup'))

        informe_preferences = False if request.form.get('informe_preferences') else True
        if informe_preferences:
            skill_level =          request.form.get('skill_level'),
            dietary_restrictions = request.form.get('dietary_restrictions'),
            
        new_user = User.create_user(
            email = email,
            name = name,
            password_hash = password,
            skill_level = skill_level,
            dietary_restrictions = dietary_restrictions 
        )
        flash('Registro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('signup/signup.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('menu.menu'))


@auth_bp.route('/profile')
@login_required
def profile():
    return render_template('profile/profile.html')