from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class Index1Form(FlaskForm):
    field1 = StringField("Поле 1:", validators=[DataRequired('Поле не заполнено')])
    field2 = StringField("Поле 2:", validators=[DataRequired('Поле не заполнено')])
    submit = SubmitField("Отправить (Метод POST)")


class Index3Form(FlaskForm):
    field1 = StringField()
    field2 = TextAreaField()
