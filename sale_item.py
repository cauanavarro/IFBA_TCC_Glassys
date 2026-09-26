from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame

from ui_sale_item import Ui_Form


class SaleItem(QFrame):

    increase_requested = Signal()
    decrease_requested = Signal()
    remove_requested = Signal()

    def __init__(self, item_venda):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.item_venda = item_venda

        self.ui.increaseButton.clicked.connect(
            self.increase_requested.emit
        )

        self.ui.decreaseButton.clicked.connect(
            self.decrease_requested.emit
        )

        self.ui.removeButton.clicked.connect(
            self.remove_requested.emit
        )

        self.update_display()
    
    def update_display(self):

        produto = self.item_venda.produto
        quantidade = self.item_venda.quantidade

        self.ui.productNameLabel.setText(
            produto["nome"]
        )

        self.ui.productQuantityLabel.setText(
                    str(quantidade)
                )
        
        self.ui.productBasePriceLabel.setText(
            f'R$ {produto["valor_unitario"]:.2f} x {quantidade}'
        )

        self.ui.productTotalPriceLabel.setText(
            f'R$ {self.item_venda.subtotal:.2f}'
        )

        self.ui.increaseButton.setEnabled(
            quantidade < produto["estoque"]
        )

        self.ui.decreaseButton.setEnabled(
            quantidade > 1
        )


    def remove_item(self):

        self.remove_requested.emit()