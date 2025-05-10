from flask import Flask, render_template, request, redirect, url_for, session, flash
from extensions import db
from flask_migrate import Migrate
import os
from models import Product, User
from forms import AdminLoginForm, ProductForm

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_delivery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Главная страница с меню продуктов
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Админ панель (вход)
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        # Простая проверка логина и пароля
        if form.username.data == 'admin' and form.password.data == 'admin123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Неверные имя пользователя или пароль', 'error')
    return render_template('admin_login.html', form=form)

# Админ панель (главная страница)
@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    products = Product.query.all()
    return render_template('admin_dashboard.html', products=products)

# Добавление продукта
@app.route('/admin/add_product', methods=['GET', 'POST'])
def add_product():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Продукт добавлен успешно', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('add_product.html', form=form)

# Выход из админки
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

if __name__ == "__main__":
    app.run(debug=True)
