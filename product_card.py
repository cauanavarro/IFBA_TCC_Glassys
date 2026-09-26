from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Signal
from ui_product_card import Ui_Form


class ProductCard(QFrame):

    product_added = Signal(dict)

    def __init__(self, produto):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.produto = produto

        self.ui.productNameLabel.setText(
            produto["nome"]
        )

        self.ui.productPriceLabel.setText(
            f'R$ {produto["valor_unitario"]:.2f}'
        )

        self.ui.productStockLabel.setText(
            f'Estoque: {produto["estoque"]}'
        )
        self.ui.addProductButton.clicked.connect(
            self.add_product
        )

    def add_product(self):

        self.product_added.emit(self.produto)