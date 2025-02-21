from src.configs import DB
from enum import Enum

class Unidades(Enum):
    Unidade = 'Unidade'
    Par = 'Par'
    Pacote = 'Pacote'
    Caixa = 'Caixa'
    Fardo = 'Fardo'
    Pallet = 'Pallet'

class Medidas(Enum):
    Mililitro = 'Mililitro'
    Litro = 'Litro'
    Grama = 'Grama'
    Quilograma = 'Quilograma'
    Unidade = 'Unidade'

class Produtos(DB.Model):
    __tablename__ = 'produtos'

    id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
    nome = DB.Column(DB.String(100), nullable=False)
    quantidade = DB.Column(DB.Numeric(6, 1), nullable=False)
    medida = DB.Column(DB.Enum(Medidas), nullable=False)
    estocado = DB.Column(DB.Integer, nullable=False)
    unidade = DB.Column(DB.Enum(Unidades), nullable=False)
    valor_unitario = DB.Column(DB.Numeric(6, 2), nullable=False)

    def __repr__(self):
        return f'ID: {self.id} Nome: {self.nome}'
