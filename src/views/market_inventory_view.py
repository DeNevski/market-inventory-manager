from flask import render_template
from src.configs import APP
from src.controllers.market_inventory_controller import produtos_list
from src.controllers.market_inventory_form import MarketStockForm

@APP.route('/')
def index():
    return render_template('index.html', titulo_pagina='Estoque De Comércio')

@APP.route('/visualizar-estoque')
def visualizar_estoque():
    return render_template('visualizar_estoque.html', produtos=produtos_list(), titulo_pagina='Visualizando Estoque')

@APP.route('/adicionar-estoque')
def adicionar_estoque():
    form = MarketStockForm()
    return render_template('adicionar_produto.html', titulo='Adicionar Produto', titulo_pagina='Adicionando Estoque', form=form)
