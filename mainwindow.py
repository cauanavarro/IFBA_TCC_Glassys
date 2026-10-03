import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QButtonGroup
)

from ui_main_window import Ui_MainWindow
from pages.sale_page import SalePage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_sidebar_buttons()
        self.setup_pages()
        self.setup_navigation()

        # Página inicial
        self.change_page(
            self.sale_page,
            self.ui.sellButton
        )

    # =========================================================
    # PÁGINAS
    # =========================================================

    def setup_pages(self):

        self.sale_page = SalePage(self)

        self.ui.pagesStackedWidget.addWidget(
            self.sale_page
        )


    # =========================================================
    # NAVEGAÇÃO
    # =========================================================

    def setup_navigation(self):

        self.ui.sellButton.clicked.connect(
            lambda:
            self.change_page(
                self.sale_page,
                self.ui.sellButton
            )
        )

        # As outras páginas serão conectadas
        # conforme forem criadas.

    def change_page(
        self,
        page,
        selected_button
    ):

        self.ui.pagesStackedWidget.setCurrentWidget(
            page
        )

        selected_button.setChecked(True)


    def setup_sidebar_buttons(self):

        self.sidebar_button_group = QButtonGroup(self)

        self.sidebar_button_group.setExclusive(True)

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
            button.setCheckable(True)

            self.sidebar_button_group.addButton(
                button
            )
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())