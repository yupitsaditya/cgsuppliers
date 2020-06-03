from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField,RadioField,FileField
from wtforms.validators import DataRequired, Email, ValidationError, URL

from wtforms.fields.html5 import DateField
import re

# (value, string shown in the dropdown)
choices = {
    "productTypes" : [
        ('Award','Award'),
        ('Lapel Pin','Lapel Pin'),
        ('Personalized Gifts','Personalized Gifts'),
        ('Printing','Printing')
    ]

}

class insertProdcutForm(FlaskForm):
    productName         =   StringField("Product Name",validators=[DataRequired()])
    category            =   SelectField("Selecte Product Category", choices=choices["productTypes"],validators=[DataRequired()])
    price               =   IntegerField("Price",validators=[DataRequired()])
    imageFile           =   FileField("Image",validators=[DataRequired()])
    submit              =   SubmitField("Add to Database",validators=[DataRequired()])


class adminLoginForm(FlaskForm):
    email               =   StringField("Email",validators=[DataRequired(),Email()])
    password            =   PasswordField("Password",validators=[DataRequired()])
    submit              =   SubmitField("Login",validators=[DataRequired()])

class contactUsQueryForm(FlaskForm):
    email               =   StringField("Email",validators=[DataRequired(),Email()])
    name                =   StringField("Name",validators=[DataRequired()])
    queryDescription    =   StringField("Query Description",validators=[DataRequired()])
    submit              =   SubmitField("Submit",validators=[DataRequired()])

