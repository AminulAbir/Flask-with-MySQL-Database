from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class User(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    year = IntegerField('Birth Year', validators=[DataRequired()])
    submit = SubmitField('Add')
