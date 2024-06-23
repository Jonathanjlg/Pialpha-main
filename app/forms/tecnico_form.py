from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired, Email

class TecnicoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = StringField('Senha', validators=[DataRequired()])
    confirmar_senha = StringField('Confirma senha', validators=[DataRequired()])
    tecnico_id = SelectField('Tecnico', coerce=int, validators=[DataRequired()])