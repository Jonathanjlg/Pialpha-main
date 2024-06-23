from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Enviar')