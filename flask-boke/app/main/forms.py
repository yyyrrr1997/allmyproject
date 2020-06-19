#app/main/forms.py
from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField

class PostForm(FlaskForm):
    title =StringField(label='标题',validators=[DataRequired()])
    body=PageDownField(label='正文',validators=[DataRequired()])
    submit =SubmitField(label='发表')

class CommentForm(FlaskForm):
    body=PageDownField(label='评论',validators=[DataRequired()])
    submit =SubmitField(label='发表')

