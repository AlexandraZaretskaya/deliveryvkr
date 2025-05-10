from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, NumberRange

class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Login')

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(min=1, max=100)])
    description = StringField('Description', validators=[Length(max=255)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Save Product')
