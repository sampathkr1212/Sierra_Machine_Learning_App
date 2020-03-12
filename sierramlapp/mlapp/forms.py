from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class PricePrediction(FlaskForm):
    excel = FileField('Upload an excel file', validators=[FileAllowed(['csv','xlsx'])])
    submit = SubmitField('Upload')
