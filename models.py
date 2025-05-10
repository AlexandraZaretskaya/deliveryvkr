from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<Product {self.name}>"

class Pizza(Product):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    toppings = db.Column(db.String(255), nullable=True)  # Дополнительные поля для пиццы

    def __repr__(self):
        return f"<Pizza {self.name}>"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='orders')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    order = db.relationship('Order', backref='order_items')
    product = db.relationship('Product', backref='order_items')

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product = db.relationship('Product', backref='cart', lazy=True)
    quantity = db.Column(db.Integer, default=1)
    user_session = db.Column(db.String(100), nullable=False)
