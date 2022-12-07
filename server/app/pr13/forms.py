from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField
from wtforms.validators import EqualTo, Email, DataRequired, ValidationError

from server.app.pr13.models import get_user_by_name


class RegistrationForm(FlaskForm):
    """
    Registration form

    :cvar username: username
    :type username: StringField
    :cvar pwd: user password
    :type pwd: PasswordField
    :cvar pwd2: user password repeat
    :type pwd2: PasswordField
    :cvar submit: submit field
    :type submit: SubmitField
    """
    username = StringField('Имя пользователя:')
    user_email = EmailField('Почта:', validators=[DataRequired(),
                                                  Email(message='Введен некорректный email адрес')])
    pwd = PasswordField('Пароль:', validators=[DataRequired()])
    pwd2 = PasswordField('Повторите пароль:', validators=[DataRequired(),
                                                          EqualTo('pwd', message='Пароли не совпадают')])
    submit = SubmitField("Регистрация")

    def validate_username(self, username: StringField):
        """
        username validator

        :param username: username
        :type username: StringField
        :raises ValidationError: if username is already taken
        """
        user_obj = get_user_by_name(username.data)
        if user_obj:
            raise ValidationError('Пользователь с таким именем уже существует')


class LoginForm(FlaskForm):
    """
    Login form

    :cvar name: username
    :type name: StringField
    :cvar pwd: user password
    :type pwd: PasswordField
    :cvar remember: remembers users for the duration of the session
    :type remember: BooleanField
    :cvar submit: submit field
    :type submit: SubmitField
    """
    name = StringField("Имя пользователя:", validators=[DataRequired('Поле не заполнено')])
    pwd = PasswordField("Пароль:", validators=[DataRequired('Поле не заполнено')])
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")
