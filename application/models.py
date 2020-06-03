import flask
from application import db
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class insertProduct(db.Document):
    productName            =   db.StringField(max_length=50,validators=[DataRequired()])
    category            =   db.StringField(max_length=50,validators=[DataRequired()])
    price               =   db.IntField(validators=[DataRequired()])
    imageFile           =   db.ImageField(thumbnail_size=(150,150, False))


class adminLogin(db.Document):
    email               =   db.StringField(max_length=50,validators=[DataRequired(),Email()])
    password            =   db.StringField(max_length=50,validators=[DataRequired()])

class contactUsQuery(db.Document):
    email               =   db.StringField(max_length=50,validators=[DataRequired(),Email()])
    name                =   db.StringField(max_length=50,validators=[DataRequired()])
    queryDescription    =   db.StringField(max_length=50,validators=[DataRequired()])
