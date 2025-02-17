from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.blueprints.auth import auth_bp
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.users import User


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
   
    if current_user.is_authenticated: # se já estiver logado vai ser redirecionado
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        informe_preferences = False if request.form.get('informe_preferences') else True
        if informe_preferences:
            preferences = {
                'skill_level':          request.form.get('skill_level'),
                'dietary_restrictions': request.form.get('dietary_restrictions'),
                'favorite_cuisines':    request.form.get('favorite_cuisines')
            }
        remember = True if request.form.get('remember') else False
        
        user = User.objects(email=email).first()
        
        if not user or not user.check_password(password):
            flash('Por favor, verifique seus dados e tente novamente.', 'error')
            return redirect(url_for('auth.login'))
            
        login_user(user, remember=remember)

        return redirect(url_for('main.index'))
        
    return render_template('auth/login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        
        if User.objects(email=email).first(): # verifica se já existe no banco
            flash('Email já registrado.', 'error')
            return redirect(url_for('auth.signup'))
            
        if User.objects(username=username).first():
            flash('Nome de usuário já existe.', 'error')
            return redirect(url_for('auth.signup'))
        
        new_user = User(
            email=email,
            username=username,
            name=name
        )
        new_user.set_password(password)
        new_user.save()
        
        flash('Registro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/signup.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth_bp.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')