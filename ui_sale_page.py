# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sale_page.ui'
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
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_salePage(object):
    def setupUi(self, salePage):
        if not salePage.objectName():
            salePage.setObjectName(u"salePage")
        salePage.resize(1080, 720)
        salePage.setStyleSheet(u"\n"
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
"\n"
"\n"
"/* =========================================================\n"
"   4. CAMPO DE BUSCA\n"
"   ========================================================= */\n"
"\n"
"QLineEdit#productSearch {\n"
"\n"
"    b"
                        "ackground-color: #FFFFFF;\n"
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
"QPushButton#lensCategoryButton,\n"
"QPushButton#sunglassesCategoryButton,\n"
"QPushButton#contactLensesCategoryButton,\n"
"QPushButton#accessoriesCategoryButton {\n"
"\n"
"    background-color: #FFFFFF;\n"
"\n"
""
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
"QPushButton#accessoriesCategoryButton:pressed {\n"
"\n"
"    background-color: #E8EEF3;\n"
"}\n"
"\n"
"\n"
"QPushButton#allCategoriesButton:checked,\n"
"QPushButton#frameCategoryButton:checked,\n"
"QPushButton#lensCa"
                        "tegoryButton:checked,\n"
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
"QWidget#productsContainer {\n"
"\n"
"    background-color: #F8F9FA;\n"
"\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   8. SALE FRAME - SUA VENDA\n"
"   ================"
                        "========================================= */\n"
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
"    background-color: #F8F9FA;\n"
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
"/* ==================="
                        "======================================\n"
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
"/* ---------- Pre\u00e7o unit\u00e1rio ---------- */\n"
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
""
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
"/* =========================================================\n"
"   11. BOT\u00d5ES + E -\n"
"   ========================================================= */\n"
"\n"
"QPushButton#decreaseButton,\n"
"QPushButton#increaseButton {\n"
"\n"
"    background-color: #F3"
                        "F4F6;\n"
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
"    f"
                        "ont-size: 13px;\n"
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
"    color: #111827;\n"
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
""
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
"   ========================================================= */\n"
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
"    border-radiu"
                        "s: 5px;\n"
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
"   Os estilos espec\u00edficos acima t\u00eam prioridade por\n"
"   utilizarem objectName.\n"
"   ========================================================= */\n"
"\n"
"QPushButton {\n"
"\n"
"    background-color: #FFFFFF;\n"
"\n"
"   "
                        " color: #1F2937;\n"
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
        self.verticalLayout_11 = QVBoxLayout(salePage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.salePageContainer = QWidget(salePage)
        self.salePageContainer.setObjectName(u"salePageContainer")
        self.salePageContainer.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_6 = QHBoxLayout(self.salePageContainer)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.salePageContainerLayout = QHBoxLayout()
        self.salePageContainerLayout.setSpacing(0)
        self.salePageContainerLayout.setObjectName(u"salePageContainerLayout")
        self.contentFrame = QFrame(self.salePageContainer)
        self.contentFrame.setObjectName(u"contentFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy)
        self.contentFrame.setMinimumSize(QSize(320, 0))
        self.contentFrame.setStyleSheet(u"")
        self.contentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.contentLayout = QVBoxLayout()
        self.contentLayout.setSpacing(16)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(24, 24, 24, 24)
        self.pageTitleLabel = QLabel(self.contentFrame)
        self.pageTitleLabel.setObjectName(u"pageTitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pageTitleLabel.sizePolicy().hasHeightForWidth())
        self.pageTitleLabel.setSizePolicy(sizePolicy1)
        self.pageTitleLabel.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.pageTitleLabel.setFont(font)

        self.contentLayout.addWidget(self.pageTitleLabel)

        self.productSearch = QLineEdit(self.contentFrame)
        self.productSearch.setObjectName(u"productSearch")
        self.productSearch.setMinimumSize(QSize(0, 40))

        self.contentLayout.addWidget(self.productSearch)

        self.categoriesLabel = QLabel(self.contentFrame)
        self.categoriesLabel.setObjectName(u"categoriesLabel")
        self.categoriesLabel.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setWeight(QFont.DemiBold)
        self.categoriesLabel.setFont(font1)

        self.contentLayout.addWidget(self.categoriesLabel)

        self.categoryContainer = QWidget(self.contentFrame)
        self.categoryContainer.setObjectName(u"categoryContainer")
        self.horizontalLayout_7 = QHBoxLayout(self.categoryContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
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


        self.horizontalLayout_7.addLayout(self.horizontalLayout)


        self.contentLayout.addWidget(self.categoryContainer)

        self.productsLabel = QLabel(self.contentFrame)
        self.productsLabel.setObjectName(u"productsLabel")
        self.productsLabel.setFont(font1)

        self.contentLayout.addWidget(self.productsLabel)

        self.productScrollArea = QScrollArea(self.contentFrame)
        self.productScrollArea.setObjectName(u"productScrollArea")
        self.productScrollArea.setWidgetResizable(True)
        self.productsContainer = QWidget()
        self.productsContainer.setObjectName(u"productsContainer")
        self.productsContainer.setGeometry(QRect(0, 0, 608, 404))
        self.gridLayout_3 = QGridLayout(self.productsContainer)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.productsGridLayout = QGridLayout()
        self.productsGridLayout.setSpacing(16)
        self.productsGridLayout.setObjectName(u"productsGridLayout")
        self.productsGridLayout.setContentsMargins(12, 12, 12, 12)

        self.gridLayout_3.addLayout(self.productsGridLayout, 0, 0, 1, 1)

        self.productScrollArea.setWidget(self.productsContainer)

        self.contentLayout.addWidget(self.productScrollArea)


        self.verticalLayout_5.addLayout(self.contentLayout)


        self.salePageContainerLayout.addWidget(self.contentFrame)

        self.saleFrame = QFrame(self.salePageContainer)
        self.saleFrame.setObjectName(u"saleFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.saleFrame.sizePolicy().hasHeightForWidth())
        self.saleFrame.setSizePolicy(sizePolicy2)
        self.saleFrame.setMinimumSize(QSize(330, 0))
        self.saleFrame.setMaximumSize(QSize(400, 16777215))
        self.saleFrame.setBaseSize(QSize(0, 0))
        self.saleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.saleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.saleFrame)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_9 = QVBoxLayout(self.customerContainer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.customerContainerLayout = QVBoxLayout()
        self.customerContainerLayout.setObjectName(u"customerContainerLayout")

        self.verticalLayout_9.addLayout(self.customerContainerLayout)


        self.verticalLayout.addWidget(self.customerContainer)

        self.saleScrollArea = QScrollArea(self.saleFrame)
        self.saleScrollArea.setObjectName(u"saleScrollArea")
        self.saleScrollArea.setWidgetResizable(True)
        self.saleLayoutWidgetContents = QWidget()
        self.saleLayoutWidgetContents.setObjectName(u"saleLayoutWidgetContents")
        self.saleLayoutWidgetContents.setGeometry(QRect(0, 0, 348, 476))
        self.verticalLayout_10 = QVBoxLayout(self.saleLayoutWidgetContents)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.saleItemsVLayout = QVBoxLayout()
        self.saleItemsVLayout.setObjectName(u"saleItemsVLayout")

        self.verticalLayout_10.addLayout(self.saleItemsVLayout)

        self.saleScrollArea.setWidget(self.saleLayoutWidgetContents)

        self.verticalLayout.addWidget(self.saleScrollArea)

        self.subTotalValueContainer = QWidget(self.saleFrame)
        self.subTotalValueContainer.setObjectName(u"subTotalValueContainer")
        self.horizontalLayout_8 = QHBoxLayout(self.subTotalValueContainer)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.subTotalLayout = QHBoxLayout()
        self.subTotalLayout.setObjectName(u"subTotalLayout")
        self.subtotalLabel = QLabel(self.subTotalValueContainer)
        self.subtotalLabel.setObjectName(u"subtotalLabel")
        self.subtotalLabel.setFont(font1)

        self.subTotalLayout.addWidget(self.subtotalLabel)

        self.subtotalValueLabel = QLabel(self.subTotalValueContainer)
        self.subtotalValueLabel.setObjectName(u"subtotalValueLabel")
        self.subtotalValueLabel.setFont(font)

        self.subTotalLayout.addWidget(self.subtotalValueLabel)


        self.horizontalLayout_8.addLayout(self.subTotalLayout)


        self.verticalLayout.addWidget(self.subTotalValueContainer)

        self.finishSaleButton = QPushButton(self.saleFrame)
        self.finishSaleButton.setObjectName(u"finishSaleButton")
        self.finishSaleButton.setFont(font1)

        self.verticalLayout.addWidget(self.finishSaleButton)


        self.verticalLayout_8.addLayout(self.verticalLayout)


        self.salePageContainerLayout.addWidget(self.saleFrame)


        self.horizontalLayout_6.addLayout(self.salePageContainerLayout)


        self.verticalLayout_11.addWidget(self.salePageContainer)


        self.retranslateUi(salePage)

        QMetaObject.connectSlotsByName(salePage)
    # setupUi

    def retranslateUi(self, salePage):
        salePage.setWindowTitle(QCoreApplication.translate("salePage", u"Form", None))
        self.pageTitleLabel.setText(QCoreApplication.translate("salePage", u"Nova Venda", None))
        self.productSearch.setPlaceholderText(QCoreApplication.translate("salePage", u"Buscar produto...", None))
        self.categoriesLabel.setText(QCoreApplication.translate("salePage", u"Categorias", None))
        self.allCategoriesButton.setText(QCoreApplication.translate("salePage", u"Todos", None))
        self.frameCategory.setText(QCoreApplication.translate("salePage", u"Arma\u00e7\u00f5es", None))
        self.lensCategoryButton.setText(QCoreApplication.translate("salePage", u"Lentes", None))
        self.pushButton.setText(QCoreApplication.translate("salePage", u"\u00d3culos de Sol", None))
        self.contactLensesCategoryButton.setText(QCoreApplication.translate("salePage", u"Lentes de Contato", None))
        self.accessoriesCategoryButton.setText(QCoreApplication.translate("salePage", u"Acess\u00f3rios", None))
        self.productsLabel.setText(QCoreApplication.translate("salePage", u"Produtos", None))
        self.yourSaleLabel.setText(QCoreApplication.translate("salePage", u"Sua Venda", None))
        self.subtotalLabel.setText(QCoreApplication.translate("salePage", u"Subtotal:", None))
        self.subtotalValueLabel.setText(QCoreApplication.translate("salePage", u"R$ 0000,00", None))
        self.finishSaleButton.setText(QCoreApplication.translate("salePage", u"Finalizar Venda", None))
    # retranslateUi

