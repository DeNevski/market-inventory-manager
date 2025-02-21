from src.models.entities.produtos_table import Produtos
from src.configs import APP, DB
from src.controllers.market_inventory_form import MarketStockForm
from flask import request, redirect, url_for, render_template

def produtos_list():
    with APP.app_context():
        produtos = Produtos.query.order_by(Produtos.id).all()
        return produtos
    
@APP.route('/adicionar', methods=['POST',])
def adicionar():
    form = MarketStockForm(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('adicionar_produto.html'))
    
    nome = form.nome.data
    quantidade = form.quantidade.data
    medida = form.medida.data
    estocado = form.estocado.data
    unidade = form.unidade.data
    valor_unitario = form.valor_unitario.data

    if Produtos.query.filter_by(nome=nome, quantidade=quantidade, medida=medida).first():
        return redirect(url_for('index'))
    else:
        novo_produto = Produtos(nome=nome.title(), quantidade=quantidade, medida=medida, estocado=estocado, unidade=unidade, valor_unitario=valor_unitario)

        DB.session.add(novo_produto)
        DB.session.commit()

        return redirect(url_for('index'))

@APP.route('/editar/<int:id>')
def editar(id):
    produto = Produtos.query.filter_by(id=id).first()

    form = MarketStockForm()
    form.nome.data = produto.nome
    form.quantidade.data = produto.quantidade
    form.medida.data = produto.medida.value
    form.estocado.data = produto.estocado
    form.unidade.data = produto.unidade.value
    form.valor_unitario.data = produto.valor_unitario

    return render_template('editar_produto.html', titulo_pagina='Editando Produto', titulo='Editar Produto', form=form, id=id)

@APP.route('/atualizar', methods=['POST',])
def atualizar():
    form = MarketStockForm(request.form)

    if form.validate_on_submit():
        produto = Produtos.query.filter_by(id=request.form['id']).first()

        produto.nome = form.nome.data.title()
        produto.quantidade = form.quantidade.data
        produto.medida = form.medida.data
        produto.estocado = form.estocado.data
        produto.unidade = form.unidade.data
        produto.valor_unitario = form.valor_unitario.data

        DB.session.add(produto)
        DB.session.commit()

    return redirect(url_for('visualizar_estoque'))

@APP.route('/deletar/<int:id>')
def deletar(id):
    Produtos.query.filter_by(id=id).delete()
    DB.session.commit()

    return redirect(url_for('visualizar_estoque'))
