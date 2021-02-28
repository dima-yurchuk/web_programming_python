from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask import session

class ContactForm(FlaskForm):
    # cookie_name = session.get("name")
    # cookie_email = session.get("email")
    name = StringField(
            'Name',
            validators=[DataRequired(message="Поле не можу бути пустим!")]
        )
    email = StringField(
            'Email',
            validators=[
                DataRequired(),
                Email(message='Incorrect email address!')
            ]
        )
    body = TextField(
            'Body',
            validators=[
                DataRequired(),
                Length(min=1, max=150, message="Field must be between 1 and 150 characters long!")
            ]
        )
    submit = SubmitField('Submit')
    # cookie_name = session.get("name")
    # cookie_email = session.get("email")
    # if cookie_name is None and cookie_email is None:
    #     name = StringField(
    #         'Name',
    #         validators=[DataRequired(message="Поле не можу бути пустим!")]
    #     )
    #     email = StringField(
    #         'Email',
    #         validators=[
    #             DataRequired(),
    #             Email(message='Incorrect email address!')
    #         ]
    #     )
    #     body = TextField(
    #         'Body',
    #         validators=[
    #             DataRequired(),
    #             Length(min=1, max=150, message="Field must be between 1 and 150 characters long!")
    #         ]
    #     )
    #     submit = SubmitField('Submit')
    # else:
    #     body = TextField(
    #         'Body',
    #         validators=[
    #             DataRequired(),
    #             Length(min=1, max=150, message="Field must be between 1 and 150 characters long!")
    #         ]
    #     )
    #     submit = SubmitField('Submit')
