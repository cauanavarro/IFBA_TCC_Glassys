from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ItemVenda:
    produto: dict
    quantidade: int = 1

    @property
    def subtotal(self) -> Decimal:
        return (
            self.produto["valor_unitario"]
            * self.quantidade
        )

class VendaAtual:

    def __init__(self):
        self.cliente = None
        self.itens = []
        self.desconto = Decimal("0.00")
    
    def selecionar_cliente(self, cliente):
        self.cliente = cliente

    def buscar_item(self, produto_id):

        for item in self.itens:

            if item.produto["id"] == produto_id:
                return item

        return None

    def adicionar_produto(self, produto):

        item = self.buscar_item(produto["id"])

        if item is not None:

            if item.quantidade >= produto["estoque"]:
                return False

            item.quantidade += 1
            return True

        if produto["estoque"] <= 0:
            return False

        self.itens.append(
            ItemVenda(produto=produto)
        )

        return True

    def diminuir_quantidade(self, produto_id):

        item = self.buscar_item(produto_id)

        if item is None:
            return False

        if item.quantidade <= 1:
            return False

        item.quantidade -= 1

        return True

    def aumentar_quantidade(self, produto_id):

        item = self.buscar_item(produto_id)

        if item is None:
            return False

        if item.quantidade >= item.produto["estoque"]:
            return False

        item.quantidade += 1

        return True

    def remover_produto(self, produto_id):

        item = self.buscar_item(produto_id)

        if item is None:
            return False

        self.itens.remove(item)

        return True

    @property
    def subtotal(self) -> Decimal:

        return sum(
            (item.subtotal for item in self.itens),
            Decimal("0.00")
        )

    @property
    def total(self) -> Decimal:

        total = self.subtotal - self.desconto

        return max(
            total,
            Decimal("0.00")
        )