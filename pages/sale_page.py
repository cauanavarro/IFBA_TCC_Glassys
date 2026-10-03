from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QMessageBox, QDialog

from ui_sale_page import Ui_salePage

from customer_selector import CustomerSelector
from product_card import ProductCard
from sale_item import SaleItem
from finalize_sale_dialog import FinalizeSaleDialog

from database.produto_repository import ProdutoRepository
from database.venda_repository import VendaRepository

from models.venda_atual import VendaAtual


class SalePage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_salePage()
        self.ui.setupUi(self)

        # -------------------------
        # Estado da página
        # -------------------------

        self.venda_atual = VendaAtual()

        self.sale_items = []

        self.products = []

        self.current_columns = 0

        # -------------------------
        # Repositories
        # -------------------------

        self.products_repository = ProdutoRepository()

        self.venda_repository = VendaRepository()

        # -------------------------
        # Configuração dos layouts
        # -------------------------

        self.ui.saleItemsVLayout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        self.ui.productsGridLayout.setAlignment(
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        # -------------------------
        # Seletor de cliente
        # -------------------------

        self.customer_selector = CustomerSelector()

        self.ui.customerContainerLayout.addWidget(
            self.customer_selector
        )

        self.customer_selector.customer_selected.connect(
            self.select_customer
        )

        self.customer_selector.customer_cleared.connect(
            self.clear_customer
        )
        
        # -------------------------
        # Botão finalizar
        # -------------------------

        self.ui.finishSaleButton.clicked.connect(
            self.finalize_sale
        )

        # -------------------------
        # Produtos
        # -------------------------

        self.load_products()

        # Aguarda o Qt calcular o tamanho real
        # da página antes de montar o grid.
        QTimer.singleShot(
            0,
            self.display_products
        )

    # =========================================================
    # PRODUTOS
    # =========================================================

    def load_products(self, force=False):

        self.products = (
            self.products_repository.buscar_todos()
        )

        self.display_products(
            force=force
        )

    def clear_products(self):

        while self.ui.productsGridLayout.count():

            item = (
                self.ui.productsGridLayout.takeAt(0)
            )

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

    def calculate_columns(self):

        largura = (
            self.ui.productsContainer.width()
        )

        return max(
            1,
            largura // 212
        )

    def display_products(self, force=False):

        colunas = self.calculate_columns()

        if (
            colunas == self.current_columns
            and not force
        ):
            return

        self.current_columns = colunas

        self.clear_products()

        for index, produto in enumerate(
            self.products
        ):

            card = ProductCard(produto)

            card.product_added.connect(
                self.add_product_to_sale
            )

            linha = index // colunas
            coluna = index % colunas

            self.ui.productsGridLayout.addWidget(
                card,
                linha,
                coluna
            )

    # =========================================================
    # RESPONSIVIDADE
    # =========================================================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.display_products()

    # =========================================================
    # VENDA
    # =========================================================

    def add_product_to_sale(self, produto):

        item_existente = (
            self.venda_atual.buscar_item(
                produto["id"]
            )
        )

        sucesso = (
            self.venda_atual.adicionar_produto(
                produto
            )
        )

        if not sucesso:
            return

        if item_existente is not None:

            sale_item = self.find_sale_item(
                produto["id"]
            )

            if sale_item is not None:
                sale_item.update_display()

        else:

            item_venda = (
                self.venda_atual.buscar_item(
                    produto["id"]
                )
            )

            self.create_sale_item(
                item_venda
            )

        self.update_subtotal()

    def find_sale_item(self, produto_id):

        for sale_item in self.sale_items:

            if (
                sale_item.item_venda.produto["id"]
                == produto_id
            ):
                return sale_item

        return None

    def create_sale_item(
        self,
        item_venda
    ):

        sale_item = SaleItem(
            item_venda
        )

        sale_item.increase_requested.connect(
            lambda:
            self.increase_sale_item(
                sale_item
            )
        )

        sale_item.decrease_requested.connect(
            lambda:
            self.decrease_sale_item(
                sale_item
            )
        )

        sale_item.remove_requested.connect(
            lambda:
            self.remove_sale_item(
                sale_item
            )
        )

        self.sale_items.append(
            sale_item
        )

        self.ui.saleItemsVLayout.addWidget(
            sale_item
        )

    def increase_sale_item(
        self,
        sale_item
    ):

        produto_id = (
            sale_item
            .item_venda
            .produto["id"]
        )

        sucesso = (
            self.venda_atual
            .aumentar_quantidade(
                produto_id
            )
        )

        if not sucesso:
            return

        sale_item.update_display()

        self.update_subtotal()

    def decrease_sale_item(
        self,
        sale_item
    ):

        produto_id = (
            sale_item
            .item_venda
            .produto["id"]
        )

        sucesso = (
            self.venda_atual
            .diminuir_quantidade(
                produto_id
            )
        )

        if not sucesso:
            return

        sale_item.update_display()

        self.update_subtotal()

    def remove_sale_item(
        self,
        sale_item
    ):

        produto_id = (
            sale_item
            .item_venda
            .produto["id"]
        )

        sucesso = (
            self.venda_atual
            .remover_produto(
                produto_id
            )
        )

        if not sucesso:
            return

        if sale_item in self.sale_items:

            self.sale_items.remove(
                sale_item
            )

        sale_item.deleteLater()

        self.update_subtotal()

    # =========================================================
    # CLIENTE
    # =========================================================

    def select_customer(
        self,
        customer
    ):

        self.venda_atual.selecionar_cliente(
            customer
        )

    # =========================================================
    # SUBTOTAL
    # =========================================================

    def update_subtotal(self):

        subtotal = (
            self.venda_atual.subtotal
        )

        self.ui.subtotalValueLabel.setText(
            f"R$ {subtotal:.2f}"
        )

    # =========================================================
    # FINALIZAÇÃO
    # =========================================================

    def finalize_sale(self):

        if self.venda_atual.cliente is None:

            QMessageBox.warning(
                self,
                "Venda",
                "Selecione um cliente antes "
                "de finalizar."
            )

            return

        if not self.venda_atual.itens:

            QMessageBox.warning(
                self,
                "Venda",
                "Adicione pelo menos um "
                "produto à venda."
            )

            return

        dialog = FinalizeSaleDialog(
            self.venda_atual,
            self
        )

        if (
            dialog.exec()
            != QDialog.DialogCode.Accepted
        ):
            return

        try:

            venda_id = (
                self.venda_repository.finalizar(
                    venda=self.venda_atual,
                    funcionario_id=1,
                    forma_pagamento_id=(
                        dialog.forma_pagamento_id
                    )
                )
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Erro ao finalizar venda",
                str(error)
            )

            return

        QMessageBox.information(
            self,
            "Venda finalizada",
            (
                f"Venda #{venda_id} "
                "realizada com sucesso."
            )
        )

        QTimer.singleShot(
            0,
            self.reset_sale
        )

    # =========================================================
    # RESET
    # =========================================================

    def reset_sale(self):

        for sale_item in self.sale_items:
            sale_item.deleteLater()

        self.sale_items.clear()

        self.venda_atual = VendaAtual()

        self.customer_selector.reset()

        self.update_subtotal()

        self.load_products(
            force=True
        )

    # =========================================================
    # LIMPAR SELEÇÃO DE CLIENTE
    # =========================================================

    def clear_customer(self):

        self.venda_atual.selecionar_cliente(
            None
        )