from flask import render_template, redirect, url_for, request, flash, jsonify
from app.blueprints.auth import auth_bp
from flask_login import login_user, logout_user, login_required, current_user
from app.models.users import User
from werkzeug.security import generate_password_hash


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('menu.menu'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        
        user_data = User.find_by_email(email)
        
        if not User.check_password(user_data, password):
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'error': 'Por favor, verifique seus dados e tente novamente.'})
            flash('Por favor, verifique seus dados e tente novamente.', 'error')
            return redirect(url_for('auth.login'))
        
        user = User(user_data)
        login_user(user, remember=remember)
        
        return redirect(url_for('menu.menu'))
        
    return render_template('login/login.html')


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('menu.menu'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        
        if not email or not password or not name:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'error': 'Todos os campos são obrigatórios.'})
            flash('Todos os campos são obrigatórios.', 'error')
            return redirect(url_for('auth.signup'))
            
        if User.find_by_email(email):
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'error': 'Email já registrado.'})
            flash('Email já registrado.', 'error')
            return redirect(url_for('auth.signup'))

        informe_preferences = not request.form.get('informe_preferences')
        skill_level = 'iniciante'
        dietary_restrictions = []
        
        if informe_preferences:
            skill_level = request.form.get('skill_level', 'iniciante')
            dietary_restrictions = request.form.get('dietary_restrictions', '').split(',')
            dietary_restrictions = [r.strip() for r in dietary_restrictions if r.strip()]

        user_data = User.create_user(
            email=email,
            password=password,
            name=name,
            skill_level=skill_level,
            dietary_restrictions=dietary_restrictions
        )
        
        user = User(user_data)
        login_user(user)
        
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('menu.menu'))  # Redireciona para o menu ao invés do login
        
    return render_template('signup/signup.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('menu.menu'))


@auth_bp.route('/perfil')
@login_required
def profile():
    return render_template('profile/profile.html')


@auth_bp.route('/perfil/mudar-senha', methods=['POST'])
@login_required
def change_password():
    data = request.get_json()
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')

    if new_password != confirm_password:
        return jsonify({'error': 'As novas senhas não coincidem.'}), 400

    data_user = User.find_by_email(current_user.email)
    if not User.check_password(data_user, current_password):
        return jsonify({'error': 'Senha atual incorreta.'}), 400

    new_password_hash = generate_password_hash(new_password)
    User.collection.update_one(
        {'user_id': current_user.id},
        {'$set': {'password_hash': new_password_hash}}
    )

    return jsonify({'message': 'Senha alterada com sucesso!'}), 200