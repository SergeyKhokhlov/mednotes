from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class addNote(FlaskForm):
    title = StringField('Название:', validators=[DataRequired()])
    text = TextAreaField('Текст:', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')
