from database.produto_repository import ProdutoRepository


repository = ProdutoRepository()

produtos = repository.buscar_todos()

for produto in produtos:
    print(produto)