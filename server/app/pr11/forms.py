from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, RadioField
from wtforms.validators import DataRequired


class DataRangeFormatForm(FlaskForm):
    start_date = DateField('Начало диапазона')
    end_date = DateField('Конец диапазона')
    file_format = RadioField(u'Programming Language', choices=['csv', 'json', 'yaml'], validators=[DataRequired(), ])
    submit = SubmitField("Скачать")
