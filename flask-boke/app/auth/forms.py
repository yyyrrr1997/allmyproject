#app/auth/forms.py
from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
from wtforms.fields.simple import PasswordField,SubmitField
class RegistrationForm(FlaskForm):
    email =StringField(label='邮箱地址',validators=[DataRequired(),
                                                    Length(4,32),
                                                    Email()])
    username =StringField(label='用户名',validators=[DataRequired(),
                                                    Length(4,32),
                                                    Regexp('^[A-Za-z_][A-Za-z0-9_]*$',0)])
    password=PasswordField(label='密码',validators=[DataRequired(),
                                                    EqualTo('password2',message='两次密码输入必须一致')])
    password2=PasswordField(label='确认密码',validators=[DataRequired()])
    submit =SubmitField()
class LoginForm(FlaskForm):
    username=StringField(label='用户名',validators=[DataRequired()])
    password=PasswordField(label='密码',validators=[DataRequired()])
    submit=SubmitField()

