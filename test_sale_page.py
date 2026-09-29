# test_sale_page.py

import sys

from PySide6.QtWidgets import QApplication

from pages.sale_page import SalePage


app = QApplication(sys.argv)

window = SalePage()
window.show()

sys.exit(app.exec())