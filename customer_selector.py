from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QFrame, QListWidgetItem
from database.cliente_repository import ClienteRepository
from ui_customer_selector import Ui_Form


class CustomerSelector(QFrame):

    customer_selected = Signal(dict)

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.selectedCustomerFrame.hide()
        self.repository = ClienteRepository()
        self.customers = self.repository.buscar_todos()

        self.ui.customerSearchInput.textChanged.connect(
            self.filter_customers
        )

        self.ui.customerResultsList.itemClicked.connect(
            self.select_customer
        )

        self.ui.changeCustomerButton.clicked.connect(
            self.change_customer
        )

        self.display_customers(self.customers)

    def display_customers(self, customers):

        self.ui.customerResultsList.clear()

        for customer in customers:

            text = (
                f'{customer["nome"]}\n'
                f'CPF: {customer["cpf"]}'
            )

            item = QListWidgetItem(text)

            item.setData(
                Qt.ItemDataRole.UserRole,
                customer
            )

            self.ui.customerResultsList.addItem(item)

    def filter_customers(self, text):

        text = text.lower().strip()

        filtered_customers = []

        for customer in self.customers:

            nome = customer["nome"].lower()
            cpf = customer["cpf"]

            if text in nome or text in cpf:
                filtered_customers.append(customer)

        self.display_customers(filtered_customers)

    def select_customer(self, item):

        customer = item.data(
            Qt.ItemDataRole.UserRole
        )

        self.ui.selectedCustomerNameLabel.setText(
            customer["nome"]
        )

        self.ui.selectedCustomerCpfLabel.setText(
            f'CPF: {customer["cpf"]}'
        )

        self.ui.customerSearchInput.hide()
        self.ui.customerResultsList.hide()

        self.ui.selectedCustomerFrame.show()

        self.customer_selected.emit(customer)

    def change_customer(self):

        self.ui.selectedCustomerFrame.hide()

        self.ui.customerSearchInput.show()
        self.ui.customerResultsList.show()

        self.ui.customerSearchInput.clear()
        self.ui.customerResultsList.clear()

        self.display_customers(self.customers)
    def reset(self):

        self.ui.selectedCustomerFrame.hide()

        self.ui.customerSearchInput.show()
        self.ui.customerResultsList.show()

        self.ui.customerSearchInput.clear()

        self.display_customers(
            self.customers
        )