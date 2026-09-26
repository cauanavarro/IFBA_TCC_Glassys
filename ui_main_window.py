# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* =========================================================\n"
"   GLASSYS\n"
"   LIGHT THEME\n"
"   PySide6 / Qt Widgets\n"
"   ========================================================= */\n"
"\n"
"\n"
"/* =========================================================\n"
"   1. ESTILO GERAL\n"
"   ========================================================= */\n"
"\n"
"QMainWindow {\n"
"    background-color: #F5F7FA;\n"
"}\n"
"\n"
"QWidget {\n"
"    font-family: \"Segoe UI\";\n"
"    color: #1F2937;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   2. SIDEBAR\n"
"   ========================================================= */\n"
"\n"
"QFrame#sidebarFrame {\n"
"    background-color: #1F3342;\n"
"    border: none;\n"
"    border-right: 1px solid #D9E0E5;\n"
"}\n"
"\n"
"\n"
"/* ---------- Logo ---------- */\n"
"\n"
"QLabel#logoLabel {\n"
"    color: #FFFFFF;\n"
"\n"
"    font-size: 27px;\n"
"    font-weight: 700;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
""
                        "\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"/* ---------- Divis\u00f3rias ---------- */\n"
"\n"
"QFrame#upperSidebarLine,\n"
"QFrame#bottomSidebarLine {\n"
"    background-color: #385061;\n"
"    color: #385061;\n"
"\n"
"    border: none;\n"
"\n"
"    max-height: 1px;\n"
"}\n"
"\n"
"\n"
"/* ---------- Bot\u00f5es da Sidebar ---------- */\n"
"\n"
"QPushButton#sellButton,\n"
"QPushButton#ordersButton,\n"
"QPushButton#productsButton,\n"
"QPushButton#customersButton,\n"
"QPushButton#prescriptionsButton,\n"
"QPushButton#statisticsButton,\n"
"QPushButton#assistantButton {\n"
"\n"
"    background-color: transparent;\n"
"\n"
"    color: #E8EEF2;\n"
"\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"\n"
"    text-align: left;\n"
"\n"
"    padding-left: 16px;\n"
"    padding-top: 9px;\n"
"    padding-bottom: 9px;\n"
"\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"\n"
"/* Hover */\n"
"\n"
"QPushButton#sellButton:hover,\n"
"QPushButton#ordersButton:hover,\n"
"QPushButton#productsButton:hover,"
                        "\n"
"QPushButton#customersButton:hover,\n"
"QPushButton#prescriptionsButton:hover,\n"
"QPushButton#statisticsButton:hover,\n"
"QPushButton#assistantButton:hover {\n"
"\n"
"    background-color: #2B4659;\n"
"\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"/* Selecionado */\n"
"\n"
"QPushButton#sellButton:checked,\n"
"QPushButton#ordersButton:checked,\n"
"QPushButton#productsButton:checked,\n"
"QPushButton#customersButton:checked,\n"
"QPushButton#prescriptionsButton:checked,\n"
"QPushButton#statisticsButton:checked,\n"
"QPushButton#assistantButton:checked {\n"
"\n"
"    background-color: #365A72;\n"
"\n"
"    color: #FFFFFF;\n"
"\n"
"    font-weight: 600;\n"
"\n"
"    border-left: 3px solid #8EB4CC;\n"
"\n"
"    padding-left: 13px;\n"
"}\n"
"\n"
"\n"
"/* ---------- Usu\u00e1rio ---------- */\n"
"\n"
"QLabel#userNameLabel {\n"
"    color: #FFFFFF;\n"
"\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"\n"
""
                        "QLabel#userRoleLabel {\n"
"    color: #AFC0CC;\n"
"\n"
"    font-size: 12px;\n"
"    font-weight: 400;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   3. CONTENT FRAME - NOVA VENDA\n"
"   ========================================================= */\n"
"\n"
"QFrame#contentFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E5E7EB;\n"
"}\n"
"\n"
"\n"
"/* ---------- T\u00edtulo ---------- */\n"
"\n"
"QLabel#pageTitleLabel {\n"
"    color: #111827;\n"
"\n"
"    font-size: 32px;\n"
"    font-weight: 700;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* ---------- T\u00edtulos de se\u00e7\u00e3o ---------- */\n"
"\n"
"QLabel#categoriesLabel,\n"
"QLabel#productsLabel {\n"
"\n"
"    color: #111827;\n"
"\n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
""
                        "\n"
"\n"
"/* =========================================================\n"
"   4. CAMPO DE BUSCA\n"
"   ========================================================= */\n"
"\n"
"QLineEdit#productSearch {\n"
"\n"
"    background-color: #FFFFFF;\n"
"\n"
"    color: #1F2937;\n"
"\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 7px;\n"
"\n"
"    padding: 9px 12px;\n"
"\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"\n"
"QLineEdit#productSearch:hover {\n"
"    border: 1px solid #9CA3AF;\n"
"}\n"
"\n"
"\n"
"QLineEdit#productSearch:focus {\n"
"    background-color: #FFFFFF;\n"
"\n"
"    border: 1px solid #4F7FA3;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   5. CATEGORIAS\n"
"   ========================================================= */\n"
"\n"
"QWidget#categoryContainer {\n"
"    background-color: transparent;\n"
"\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* ---------- Bot\u00f5es ---------- */\n"
"\n"
"QPushButton#allCategoriesButton,\n"
"QPushButton#frameCategoryButton,\n"
""
                        "QPushButton#lensCategoryButton,\n"
"QPushButton#sunglassesCategoryButton,\n"
"QPushButton#contactLensesCategoryButton,\n"
"QPushButton#accessoriesCategoryButton {\n"
"\n"
"    background-color: #FFFFFF;\n"
"\n"
"    color: #374151;\n"
"\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"\n"
"    padding: 7px 13px;\n"
"\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"\n"
"QPushButton#allCategoriesButton:hover,\n"
"QPushButton#frameCategoryButton:hover,\n"
"QPushButton#lensCategoryButton:hover,\n"
"QPushButton#sunglassesCategoryButton:hover,\n"
"QPushButton#contactLensesCategoryButton:hover,\n"
"QPushButton#accessoriesCategoryButton:hover {\n"
"\n"
"    background-color: #F3F6F9;\n"
"\n"
"    color: #24516F;\n"
"\n"
"    border: 1px solid #9CAFC0;\n"
"}\n"
"\n"
"\n"
"QPushButton#allCategoriesButton:pressed,\n"
"QPushButton#frameCategoryButton:pressed,\n"
"QPushButton#lensCategoryButton:pressed,\n"
"QPushButton#sunglassesCategoryButton:pressed,\n"
"QPushButton#contactLensesCategoryButton:pressed,\n"
"QPus"
                        "hButton#accessoriesCategoryButton:pressed {\n"
"\n"
"    background-color: #E8EEF3;\n"
"}\n"
"\n"
"\n"
"QPushButton#allCategoriesButton:checked,\n"
"QPushButton#frameCategoryButton:checked,\n"
"QPushButton#lensCategoryButton:checked,\n"
"QPushButton#sunglassesCategoryButton:checked,\n"
"QPushButton#contactLensesCategoryButton:checked,\n"
"QPushButton#accessoriesCategoryButton:checked {\n"
"\n"
"    background-color: #E7F0F7;\n"
"\n"
"    color: #24516F;\n"
"\n"
"    border: 1px solid #7FA4BF;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   6. \u00c1REA DOS PRODUTOS\n"
"   ========================================================= */\n"
"\n"
"QScrollArea#productScrollArea {\n"
"\n"
"    background-color: #F8F9FA;\n"
"\n"
"    border: 1px solid #E1E5E9;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QScrollArea#productScrollArea QWidget#qt_scrollarea_viewport {\n"
"\n"
"    background-color: #F8F9FA;\n"
"\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QWidget#productsCont"
                        "ainer {\n"
"\n"
"    background-color: #F8F9FA;\n"
"\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   8. SALE FRAME - SUA VENDA\n"
"   ========================================================= */\n"
"\n"
"QFrame#saleFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E5E7EB;\n"
"}\n"
"\n"
"\n"
"/* ---------- T\u00edtulo ---------- */\n"
"\n"
"QLabel#yourSaleLabel {\n"
"\n"
"    color: #111827;\n"
"\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   9. SALE SCROLL AREA\n"
"   ========================================================= */\n"
"\n"
"QScrollArea#saleScrollArea {\n"
"\n"
"    background-color: #F8F9FA;\n"
"\n"
"    border: 1px solid #E1E5E9;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QScrollArea#saleScrollArea QWidget#qt_scrollarea_viewport {\n"
"\n"
"    background-c"
                        "olor: #F8F9FA;\n"
"\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QWidget#saleLayoutWidgetContents {\n"
"\n"
"    background-color: #F8F9FA;\n"
"\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   10. SALE ITEM\n"
"   ========================================================= */\n"
"\n"
"QFrame#saleItem {\n"
"\n"
"    background-color: #FFFFFF;\n"
"\n"
"    border: 1px solid #E1E5E9;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"\n"
"/* ---------- Container ---------- */\n"
"\n"
"QWidget#productContainer,\n"
"QWidget#productNameAndPrice,\n"
"QWidget#productPriceXQuantityWidget,\n"
"QWidget#quantityButtons {\n"
"\n"
"    background-color: transparent;\n"
"\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* ---------- Nome ---------- */\n"
"\n"
"QLabel#productNameLabel {\n"
"\n"
"    color: #111827;\n"
"\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* ---------- Pre\u00e7"
                        "o unit\u00e1rio ---------- */\n"
"\n"
"QLabel#productBasePriceLabel {\n"
"\n"
"    color: #4B5563;\n"
"\n"
"    font-size: 13px;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* ---------- Quantidade no pre\u00e7o ---------- */\n"
"\n"
"QLabel#productQuantity {\n"
"\n"
"    color: #4B5563;\n"
"\n"
"    font-size: 13px;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* ---------- Pre\u00e7o total ---------- */\n"
"\n"
"QLabel#productTotalPrice {\n"
"\n"
"    color: #111827;\n"
"\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* ---------- Quantidade ---------- */\n"
"\n"
"QLabel#productQuantityLabel {\n"
"\n"
"    color: #374151;\n"
"\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"\n"
"/* ============================================"
                        "=============\n"
"   11. BOT\u00d5ES + E -\n"
"   ========================================================= */\n"
"\n"
"QPushButton#decreaseButton,\n"
"QPushButton#increaseButton {\n"
"\n"
"    background-color: #F3F4F6;\n"
"\n"
"    color: #374151;\n"
"\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"\n"
"    padding: 0;\n"
"\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"\n"
"QPushButton#decreaseButton:hover,\n"
"QPushButton#increaseButton:hover {\n"
"\n"
"    background-color: #E9EEF2;\n"
"\n"
"    color: #24516F;\n"
"\n"
"    border: 1px solid #B8C5CF;\n"
"}\n"
"\n"
"\n"
"QPushButton#decreaseButton:pressed,\n"
"QPushButton#increaseButton:pressed {\n"
"\n"
"    background-color: #DCE6EC;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   12. REMOVER ITEM\n"
"   ========================================================= */\n"
""
                        "\n"
"QPushButton#removeItem {\n"
"\n"
"    background-color: #FFFFFF;\n"
"\n"
"    color: #6B7280;\n"
"\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"\n"
"    padding: 6px 11px;\n"
"\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"\n"
"QPushButton#removeItem:hover {\n"
"\n"
"    background-color: #FEF2F2;\n"
"\n"
"    color: #B42318;\n"
"\n"
"    border: 1px solid #F0B4B4;\n"
"}\n"
"\n"
"\n"
"QPushButton#removeItem:pressed {\n"
"\n"
"    background-color: #FEE2E2;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   13. SUBTOTAL\n"
"   ========================================================= */\n"
"\n"
"QWidget#subTotalValueContainer {\n"
"\n"
"    background-color: transparent;\n"
"\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"QLabel#subtotalLabel {\n"
"\n"
"    color: #111827;\n"
"\n"
"    font-size: 17px;\n"
"    font-weight: 600;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"QLabel#subtotalValueLabel {\n"
"\n"
"    color:"
                        " #111827;\n"
"\n"
"    font-size: 17px;\n"
"    font-weight: 700;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   14. FINALIZAR VENDA\n"
"   ========================================================= */\n"
"\n"
"QPushButton#finishSaleButton {\n"
"\n"
"    background-color: #365F7A;\n"
"\n"
"    color: #FFFFFF;\n"
"\n"
"    border: none;\n"
"    border-radius: 7px;\n"
"\n"
"    min-height: 38px;\n"
"\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"\n"
"QPushButton#finishSaleButton:hover {\n"
"\n"
"    background-color: #2E526A;\n"
"}\n"
"\n"
"\n"
"QPushButton#finishSaleButton:pressed {\n"
"\n"
"    background-color: #274657;\n"
"}\n"
"\n"
"\n"
"QPushButton#finishSaleButton:disabled {\n"
"\n"
"    background-color: #CBD5DC;\n"
"\n"
"    color: #F8FAFC;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   15. SCROLLBARS\n"
"   ==============================="
                        "========================== */\n"
"\n"
"QScrollBar:vertical {\n"
"\n"
"    background-color: #F8F9FA;\n"
"\n"
"    width: 10px;\n"
"\n"
"    margin: 4px 3px 4px 0px;\n"
"\n"
"    border: none;\n"
"\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"\n"
"    background-color: #C7CDD4;\n"
"\n"
"    min-height: 40px;\n"
"\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"\n"
"    background-color: #AEB7C1;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"\n"
"    height: 0px;\n"
"\n"
"    border: none;\n"
"\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   16. BOT\u00d5ES GEN\u00c9RICOS\n"
"   =========================================================\n"
"   \n"
"   Mantido propositalmente no final.\n"
"   Os estilos esp"
                        "ec\u00edficos acima t\u00eam prioridade por\n"
"   utilizarem objectName.\n"
"   ========================================================= */\n"
"\n"
"QPushButton {\n"
"\n"
"    background-color: #FFFFFF;\n"
"\n"
"    color: #1F2937;\n"
"\n"
"    border: 1px solid #D1D5DB;\n"
"\n"
"    border-radius: 6px;\n"
"\n"
"    padding: 7px 12px;\n"
"\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background-color: #F3F4F6;\n"
"\n"
"    border: 1px solid #B7BEC7;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: #E5E7EB;\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"\n"
"    background-color: #F3F4F6;\n"
"\n"
"    color: #9CA3AF;\n"
"\n"
"    border: 1px solid #E5E7EB;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.centralLayout = QHBoxLayout()
        self.centralLayout.setSpacing(0)
        self.centralLayout.setObjectName(u"centralLayout")
        self.centralLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebarFrame.sizePolicy().hasHeightForWidth())
        self.sidebarFrame.setSizePolicy(sizePolicy)
        self.sidebarFrame.setMinimumSize(QSize(180, 0))
        self.sidebarFrame.setMaximumSize(QSize(220, 16777215))
        self.sidebarFrame.setStyleSheet(u"")
        self.sidebarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebarlLayout = QVBoxLayout()
        self.sidebarlLayout.setSpacing(10)
        self.sidebarlLayout.setObjectName(u"sidebarlLayout")
        self.sidebarlLayout.setContentsMargins(0, 20, 0, 20)
        self.logoLabel = QLabel(self.sidebarFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logoLabel.sizePolicy().hasHeightForWidth())
        self.logoLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.logoLabel.setFont(font)
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.logoLabel.setMargin(0)

        self.sidebarlLayout.addWidget(self.logoLabel)

        self.upperSidebarLine = QFrame(self.sidebarFrame)
        self.upperSidebarLine.setObjectName(u"upperSidebarLine")
        self.upperSidebarLine.setStyleSheet(u"background-color: #344C63;")
        self.upperSidebarLine.setFrameShape(QFrame.Shape.HLine)
        self.upperSidebarLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.sidebarlLayout.addWidget(self.upperSidebarLine)

        self.sellButton = QPushButton(self.sidebarFrame)
        self.sellButton.setObjectName(u"sellButton")
        self.sellButton.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setWeight(QFont.Medium)
        self.sellButton.setFont(font1)
        self.sellButton.setStyleSheet(u"")
        self.sellButton.setCheckable(True)
        self.sellButton.setChecked(True)

        self.sidebarlLayout.addWidget(self.sellButton)

        self.ordersButton = QPushButton(self.sidebarFrame)
        self.ordersButton.setObjectName(u"ordersButton")
        self.ordersButton.setMinimumSize(QSize(0, 40))
        self.ordersButton.setFont(font1)
        self.ordersButton.setCheckable(True)

        self.sidebarlLayout.addWidget(self.ordersButton)

        self.productsButton = QPushButton(self.sidebarFrame)
        self.productsButton.setObjectName(u"productsButton")
        self.productsButton.setMinimumSize(QSize(0, 40))
        self.productsButton.setFont(font1)
        self.productsButton.setCheckable(True)

        self.sidebarlLayout.addWidget(self.productsButton)

        self.customersButton = QPushButton(self.sidebarFrame)
        self.customersButton.setObjectName(u"customersButton")
        self.customersButton.setMinimumSize(QSize(0, 40))
        self.customersButton.setFont(font1)
        self.customersButton.setCheckable(True)

        self.sidebarlLayout.addWidget(self.customersButton)

        self.prescriptionsButton = QPushButton(self.sidebarFrame)
        self.prescriptionsButton.setObjectName(u"prescriptionsButton")
        self.prescriptionsButton.setMinimumSize(QSize(0, 40))
        self.prescriptionsButton.setFont(font1)
        self.prescriptionsButton.setCheckable(True)

        self.sidebarlLayout.addWidget(self.prescriptionsButton)

        self.statisticsButton = QPushButton(self.sidebarFrame)
        self.statisticsButton.setObjectName(u"statisticsButton")
        self.statisticsButton.setMinimumSize(QSize(0, 40))
        self.statisticsButton.setFont(font1)
        self.statisticsButton.setCheckable(True)

        self.sidebarlLayout.addWidget(self.statisticsButton)

        self.assistantButton = QPushButton(self.sidebarFrame)
        self.assistantButton.setObjectName(u"assistantButton")
        self.assistantButton.setMinimumSize(QSize(0, 40))
        self.assistantButton.setFont(font1)
        self.assistantButton.setCheckable(True)

        self.sidebarlLayout.addWidget(self.assistantButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarlLayout.addItem(self.verticalSpacer)

        self.bottomSidebarLine = QFrame(self.sidebarFrame)
        self.bottomSidebarLine.setObjectName(u"bottomSidebarLine")
        self.bottomSidebarLine.setStyleSheet(u"background-color: #344C63;")
        self.bottomSidebarLine.setFrameShape(QFrame.Shape.HLine)
        self.bottomSidebarLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.sidebarlLayout.addWidget(self.bottomSidebarLine)

        self.userNameLabel = QLabel(self.sidebarFrame)
        self.userNameLabel.setObjectName(u"userNameLabel")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setWeight(QFont.DemiBold)
        self.userNameLabel.setFont(font2)

        self.sidebarlLayout.addWidget(self.userNameLabel)

        self.userRoleLabel = QLabel(self.sidebarFrame)
        self.userRoleLabel.setObjectName(u"userRoleLabel")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        self.userRoleLabel.setFont(font3)

        self.sidebarlLayout.addWidget(self.userRoleLabel)


        self.verticalLayout_2.addLayout(self.sidebarlLayout)


        self.centralLayout.addWidget(self.sidebarFrame)

        self.contentFrame = QFrame(self.centralwidget)
        self.contentFrame.setObjectName(u"contentFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy2)
        self.contentFrame.setMinimumSize(QSize(320, 0))
        self.contentFrame.setStyleSheet(u"")
        self.contentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentLayout = QVBoxLayout()
        self.contentLayout.setSpacing(16)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(24, 24, 24, 24)
        self.pageTitleLabel = QLabel(self.contentFrame)
        self.pageTitleLabel.setObjectName(u"pageTitleLabel")
        sizePolicy1.setHeightForWidth(self.pageTitleLabel.sizePolicy().hasHeightForWidth())
        self.pageTitleLabel.setSizePolicy(sizePolicy1)
        self.pageTitleLabel.setMaximumSize(QSize(16777215, 40))
        self.pageTitleLabel.setFont(font)

        self.contentLayout.addWidget(self.pageTitleLabel)

        self.productSearch = QLineEdit(self.contentFrame)
        self.productSearch.setObjectName(u"productSearch")
        self.productSearch.setMinimumSize(QSize(0, 40))

        self.contentLayout.addWidget(self.productSearch)

        self.categoriesLabel = QLabel(self.contentFrame)
        self.categoriesLabel.setObjectName(u"categoriesLabel")
        self.categoriesLabel.setMaximumSize(QSize(16777215, 30))
        self.categoriesLabel.setFont(font2)

        self.contentLayout.addWidget(self.categoriesLabel)

        self.categoryContainer = QWidget(self.contentFrame)
        self.categoryContainer.setObjectName(u"categoryContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.categoryContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.allCategoriesButton = QPushButton(self.categoryContainer)
        self.allCategoriesButton.setObjectName(u"allCategoriesButton")
        self.allCategoriesButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.allCategoriesButton)

        self.frameCategory = QPushButton(self.categoryContainer)
        self.frameCategory.setObjectName(u"frameCategory")

        self.horizontalLayout.addWidget(self.frameCategory)

        self.lensCategoryButton = QPushButton(self.categoryContainer)
        self.lensCategoryButton.setObjectName(u"lensCategoryButton")

        self.horizontalLayout.addWidget(self.lensCategoryButton)

        self.pushButton = QPushButton(self.categoryContainer)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.contactLensesCategoryButton = QPushButton(self.categoryContainer)
        self.contactLensesCategoryButton.setObjectName(u"contactLensesCategoryButton")
        self.contactLensesCategoryButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.contactLensesCategoryButton)

        self.accessoriesCategoryButton = QPushButton(self.categoryContainer)
        self.accessoriesCategoryButton.setObjectName(u"accessoriesCategoryButton")

        self.horizontalLayout.addWidget(self.accessoriesCategoryButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.contentLayout.addWidget(self.categoryContainer)

        self.productsLabel = QLabel(self.contentFrame)
        self.productsLabel.setObjectName(u"productsLabel")
        self.productsLabel.setFont(font2)

        self.contentLayout.addWidget(self.productsLabel)

        self.productScrollArea = QScrollArea(self.contentFrame)
        self.productScrollArea.setObjectName(u"productScrollArea")
        self.productScrollArea.setWidgetResizable(True)
        self.productsContainer = QWidget()
        self.productsContainer.setObjectName(u"productsContainer")
        self.productsContainer.setGeometry(QRect(0, 0, 516, 422))
        self.gridLayout_2 = QGridLayout(self.productsContainer)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.productsGridLayout = QGridLayout()
        self.productsGridLayout.setSpacing(16)
        self.productsGridLayout.setObjectName(u"productsGridLayout")
        self.productsGridLayout.setContentsMargins(12, 12, 12, 12)

        self.gridLayout_2.addLayout(self.productsGridLayout, 0, 0, 1, 1)

        self.productScrollArea.setWidget(self.productsContainer)

        self.contentLayout.addWidget(self.productScrollArea)


        self.verticalLayout_3.addLayout(self.contentLayout)


        self.centralLayout.addWidget(self.contentFrame)

        self.saleFrame = QFrame(self.centralwidget)
        self.saleFrame.setObjectName(u"saleFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.saleFrame.sizePolicy().hasHeightForWidth())
        self.saleFrame.setSizePolicy(sizePolicy3)
        self.saleFrame.setMinimumSize(QSize(330, 0))
        self.saleFrame.setMaximumSize(QSize(400, 16777215))
        self.saleFrame.setBaseSize(QSize(0, 0))
        self.saleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.saleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.saleFrame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(24, 24, 24, 24)
        self.yourSaleLabel = QLabel(self.saleFrame)
        self.yourSaleLabel.setObjectName(u"yourSaleLabel")
        self.yourSaleLabel.setFont(font)

        self.verticalLayout.addWidget(self.yourSaleLabel)

        self.customerContainer = QWidget(self.saleFrame)
        self.customerContainer.setObjectName(u"customerContainer")
        self.customerContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.customerContainer)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.customerContainerLayout = QVBoxLayout()
        self.customerContainerLayout.setObjectName(u"customerContainerLayout")

        self.verticalLayout_7.addLayout(self.customerContainerLayout)


        self.verticalLayout.addWidget(self.customerContainer)

        self.saleScrollArea = QScrollArea(self.saleFrame)
        self.saleScrollArea.setObjectName(u"saleScrollArea")
        self.saleScrollArea.setWidgetResizable(True)
        self.saleLayoutWidgetContents = QWidget()
        self.saleLayoutWidgetContents.setObjectName(u"saleLayoutWidgetContents")
        self.saleLayoutWidgetContents.setGeometry(QRect(0, 0, 278, 494))
        self.verticalLayout_6 = QVBoxLayout(self.saleLayoutWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.saleItemsVLayout = QVBoxLayout()
        self.saleItemsVLayout.setObjectName(u"saleItemsVLayout")

        self.verticalLayout_6.addLayout(self.saleItemsVLayout)

        self.saleScrollArea.setWidget(self.saleLayoutWidgetContents)

        self.verticalLayout.addWidget(self.saleScrollArea)

        self.subTotalValueContainer = QWidget(self.saleFrame)
        self.subTotalValueContainer.setObjectName(u"subTotalValueContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.subTotalValueContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.subTotalLayout = QHBoxLayout()
        self.subTotalLayout.setObjectName(u"subTotalLayout")
        self.subtotalLabel = QLabel(self.subTotalValueContainer)
        self.subtotalLabel.setObjectName(u"subtotalLabel")
        self.subtotalLabel.setFont(font2)

        self.subTotalLayout.addWidget(self.subtotalLabel)

        self.subtotalValueLabel = QLabel(self.subTotalValueContainer)
        self.subtotalValueLabel.setObjectName(u"subtotalValueLabel")
        self.subtotalValueLabel.setFont(font)

        self.subTotalLayout.addWidget(self.subtotalValueLabel)


        self.horizontalLayout_5.addLayout(self.subTotalLayout)


        self.verticalLayout.addWidget(self.subTotalValueContainer)

        self.finishSaleButton = QPushButton(self.saleFrame)
        self.finishSaleButton.setObjectName(u"finishSaleButton")
        self.finishSaleButton.setFont(font2)

        self.verticalLayout.addWidget(self.finishSaleButton)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.centralLayout.addWidget(self.saleFrame)


        self.horizontalLayout_2.addLayout(self.centralLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"Glassys", None))
        self.sellButton.setText(QCoreApplication.translate("MainWindow", u"Vender", None))
        self.ordersButton.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.productsButton.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.customersButton.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.prescriptionsButton.setText(QCoreApplication.translate("MainWindow", u"Receitas", None))
        self.statisticsButton.setText(QCoreApplication.translate("MainWindow", u"Estat\u00edsticas", None))
        self.assistantButton.setText(QCoreApplication.translate("MainWindow", u"Assistente", None))
        self.userNameLabel.setText(QCoreApplication.translate("MainWindow", u"Joana Santana", None))
        self.userRoleLabel.setText(QCoreApplication.translate("MainWindow", u"Gerente", None))
        self.pageTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Nova Venda", None))
        self.productSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar produto...", None))
        self.categoriesLabel.setText(QCoreApplication.translate("MainWindow", u"Categorias", None))
        self.allCategoriesButton.setText(QCoreApplication.translate("MainWindow", u"Todos", None))
        self.frameCategory.setText(QCoreApplication.translate("MainWindow", u"Arma\u00e7\u00f5es", None))
        self.lensCategoryButton.setText(QCoreApplication.translate("MainWindow", u"Lentes", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u00d3culos de Sol", None))
        self.contactLensesCategoryButton.setText(QCoreApplication.translate("MainWindow", u"Lentes de Contato", None))
        self.accessoriesCategoryButton.setText(QCoreApplication.translate("MainWindow", u"Acess\u00f3rios", None))
        self.productsLabel.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.yourSaleLabel.setText(QCoreApplication.translate("MainWindow", u"Sua Venda", None))
        self.subtotalLabel.setText(QCoreApplication.translate("MainWindow", u"Subtotal:", None))
        self.subtotalValueLabel.setText(QCoreApplication.translate("MainWindow", u"R$ 0000,00", None))
        self.finishSaleButton.setText(QCoreApplication.translate("MainWindow", u"Finalizar Venda", None))
    # retranslateUi

