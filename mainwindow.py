import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QTimer
from customer_selector import CustomerSelector
from ui_main_window import Ui_MainWindow
from product_card import ProductCard
from sale_item import SaleItem
from database.produto_repository import ProdutoRepository
from decimal import Decimal
from models.venda_atual import VendaAtual

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.saleItemsVLayout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )   
        self.ui.productsGridLayout.setAlignment(
             Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )   
        self.venda_atual = VendaAtual()
        self.current_columns = 0
        self.sale_items = []
        self.productsRepository = ProdutoRepository()
        self.setup_navigation()
        self.load_products()
        QTimer.singleShot(0, self.display_products)

        self.customer_selector = CustomerSelector()
        self.ui.customerContainerLayout.addWidget(
           self.customer_selector
        )
        self.customer_selector.customer_selected.connect(
            self.select_customer
        )
        


    def setup_navigation(self):
        self.ui.sellButton.clicked.connect(
            lambda: self.select_page(self.ui.sellButton)
        )

        self.ui.ordersButton.clicked.connect(
            lambda: self.select_page(self.ui.ordersButton)
        )

        self.ui.productsButton.clicked.connect(
            lambda: self.select_page(self.ui.productsButton)
        )

        self.ui.customersButton.clicked.connect(
            lambda: self.select_page(self.ui.customersButton)
        )

        self.ui.prescriptionsButton.clicked.connect(
            lambda: self.select_page(self.ui.prescriptionsButton)
        )

        self.ui.statisticsButton.clicked.connect(
            lambda: self.select_page(self.ui.statisticsButton)
        )

        self.ui.assistantButton.clicked.connect(
            lambda: self.select_page(self.ui.assistantButton)
        )

    def select_page(self, selected_button):

        buttons = [
            self.ui.sellButton,
            self.ui.ordersButton,
            self.ui.productsButton,
            self.ui.customersButton,
            self.ui.prescriptionsButton,
            self.ui.statisticsButton,
            self.ui.assistantButton
        ]

        for button in buttons:
            button.setChecked(button == selected_button)

    def load_products(self):
        self.products = self.productsRepository.buscar_todos()

        self.display_products()

    def clear_products(self):

        while self.ui.productsGridLayout.count():

            item = self.ui.productsGridLayout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

    def calculate_columns(self):
        largura = self.ui.productsContainer.width()

        return max(1, largura // 212)

    def display_products(self):
        colunas = self.calculate_columns()

        if colunas == self.current_columns:
            return

        self.current_columns = colunas

        self.clear_products()

        for index, produto in enumerate(self.products):

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

    def resizeEvent(self, event):
        self.display_products()

        super().resizeEvent(event)

    def add_product_to_sale(self, produto):

        item_existente = self.venda_atual.buscar_item(
            produto["id"]
        )

        sucesso = self.venda_atual.adicionar_produto(
            produto
        )

        if not sucesso:
            return

        if item_existente is not None:

            sale_item = self.find_sale_item(
                produto["id"]
            )

            sale_item.update_display()

        else:

            item_venda = self.venda_atual.buscar_item(
                produto["id"]
            )

            self.create_sale_item(item_venda)

        self.update_subtotal()

    def find_sale_item(self, produto_id):

        for sale_item in self.sale_items:

            if (
                sale_item.item_venda.produto["id"]
                == produto_id
            ):
                return sale_item

        return None
        
    def update_subtotal(self):

        subtotal = self.venda_atual.subtotal

        self.ui.subtotalValueLabel.setText(
            f"R$ {subtotal:.2f}"
        )

    def increase_sale_item(self, sale_item):

        produto_id = (
            sale_item.item_venda.produto["id"]
        )

        sucesso = (
            self.venda_atual.aumentar_quantidade(
                produto_id
            )
        )

        if not sucesso:
            return

        sale_item.update_display()

        self.update_subtotal()

    def decrease_sale_item(self, sale_item):

        produto_id = (
            sale_item.item_venda.produto["id"]
        )

        sucesso = (
            self.venda_atual.diminuir_quantidade(
                produto_id
            )
        )

        if not sucesso:
            return

        sale_item.update_display()

        self.update_subtotal()

    def create_sale_item(self, item_venda):

        sale_item = SaleItem(item_venda)

        sale_item.increase_requested.connect(
            lambda: self.increase_sale_item(sale_item)
        )

        sale_item.decrease_requested.connect(
            lambda: self.decrease_sale_item(sale_item)
        )

        sale_item.remove_requested.connect(
            lambda: self.remove_sale_item(sale_item)
        )

        self.sale_items.append(sale_item)

        self.ui.saleItemsVLayout.addWidget(
            sale_item
        )

    def remove_sale_item(self, sale_item):

        produto_id = (
            sale_item.item_venda.produto["id"]
        )

        sucesso = (
            self.venda_atual.remover_produto(
                produto_id
            )
        )

        if not sucesso:
            return

        if sale_item in self.sale_items:
            self.sale_items.remove(sale_item)

        sale_item.deleteLater()

        self.update_subtotal()

    def select_customer(self, customer):

            self.venda_atual.selecionar_cliente(
               customer
            )
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())