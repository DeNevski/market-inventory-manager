from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, SubmitField, validators
from src.models.entities.produtos_table import Unidades, Medidas

class MarketStockForm(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=100)])
    quantidade = DecimalField('Quantidade', places=1, validators=[validators.DataRequired(), validators.NumberRange(min=0)])
    medida = SelectField('Medida', choices=[(medida.value) for medida in Medidas], validators=[validators.DataRequired()])
    estocado = IntegerField('Estocado', [validators.DataRequired()])
    unidade = SelectField('Unidade', choices=[(unidade.value) for unidade in Unidades], validators=[validators.DataRequired()])
    valor_unitario = DecimalField('Valor Unitário', places=2, validators=[validators.DataRequired(), validators.NumberRange(min=0)])
    salvar = SubmitField('Salvar')
