from database.cliente_repository import ClienteRepository
from database.produto_repository import ProdutoRepository
from database.venda_repository import VendaRepository
from models.venda_atual import VendaAtual


clientes = ClienteRepository().buscar_todos()
produtos = ProdutoRepository().buscar_todos()

venda = VendaAtual()

venda.selecionar_cliente(
    clientes[0]
)

venda.adicionar_produto(
    produtos[0]
)

repository = VendaRepository()

venda_id = repository.finalizar(
    venda=venda,
    funcionario_id=1,
    forma_pagamento_id=1
)

print(
    f"Venda criada com ID {venda_id}"
)