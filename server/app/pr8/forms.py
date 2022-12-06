from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField


class Index1Form(FlaskForm):
    field1 = StringField()
    field2 = TextAreaField()