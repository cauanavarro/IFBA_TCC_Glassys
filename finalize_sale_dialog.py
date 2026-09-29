from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from ui_finalize_sale_dialog import Ui_finalizeSaleDialog
from database.forma_pagamento_repository import (
    FormaPagamentoRepository
)


class FinalizeSaleDialog(QDialog):

    def __init__(self, venda, parent=None):
        super().__init__(parent)

        self.ui = Ui_finalizeSaleDialog()
        self.ui.setupUi(self)

        self.venda = venda

        self.forma_pagamento_repository = (
            FormaPagamentoRepository()
        )

        self.setup_sale()
        self.load_payment_methods()

        self.ui.cancelSaleButton.clicked.connect(
            self.reject
        )

        self.ui.confirmSaleButton.clicked.connect(
            self.accept
        )

    def setup_sale(self):

        self.ui.customerNameLabel.setText(
            self.venda.cliente["nome"]
        )

        self.ui.totalValueLabel.setText(
            f"R$ {self.venda.total:.2f}"
        )

    def load_payment_methods(self):

        formas = (
            self.forma_pagamento_repository
            .buscar_todas()
        )

        self.ui.paymentComboBox.clear()

        for forma in formas:

            self.ui.paymentComboBox.addItem(
                forma["nome"],
                forma["id"]
            )

    @property
    def forma_pagamento_id(self):

        return self.ui.paymentComboBox.currentData()