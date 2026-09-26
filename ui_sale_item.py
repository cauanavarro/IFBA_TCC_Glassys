# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sale_item.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(265, 120)
        Form.setMinimumSize(QSize(0, 120))
        Form.setMaximumSize(QSize(16777215, 124))
        Form.setStyleSheet(u"/* =========================================================\n"
"   SALE ITEM\n"
"   ========================================================= */\n"
"\n"
"QFrame#saleItem {\n"
"    background-color: #FFFFFF;\n"
"\n"
"    border: 1px solid #E1E5E9;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   CONTAINER DO PRODUTO\n"
"   ========================================================= */\n"
"\n"
"QWidget#productContainer {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QWidget#productNameAndPrice {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   NOME DO PRODUTO\n"
"   ========================================================= */\n"
"\n"
"QLabel#productNameLabel {\n"
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
""
                        "/* =========================================================\n"
"   PRE\u00c7O UNIT\u00c1RIO \u00d7 QUANTIDADE\n"
"   ========================================================= */\n"
"\n"
"QWidget#productPricexQuantityWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#productBasePriceLabel {\n"
"    color: #4B5563;\n"
"\n"
"    font-size: 13px;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#productQuantity {\n"
"    color: #4B5563;\n"
"\n"
"    font-size: 13px;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   PRE\u00c7O TOTAL DO ITEM\n"
"   ========================================================= */\n"
"\n"
"QLabel#productTotalPrice {\n"
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
"/* =========================="
                        "===============================\n"
"   \u00c1REA DOS BOT\u00d5ES\n"
"   ========================================================= */\n"
"\n"
"QWidget#quantityButtons {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   BOT\u00c3O -\n"
"   ========================================================= */\n"
"\n"
"QPushButton#decreaseButton {\n"
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
"QPushButton#decreaseButton:hover {\n"
"\n"
"    background-color: #E9EEF2;\n"
"\n"
"    color: #24516F;\n"
"\n"
"    border: 1px solid #B8C5CF;\n"
"}\n"
"\n"
"QPushButton#decreaseButton:pressed {\n"
"\n"
"    background-color: #DCE6EC;\n"
"}\n"
""
                        "\n"
"QPushButton#decreaseButton:disabled {\n"
"	color: #C3C3C3\n"
"}\n"
"\n"
"/* =========================================================\n"
"   BOT\u00c3O +\n"
"   ========================================================= */\n"
"\n"
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
"QPushButton#increaseButton:hover {\n"
"\n"
"    background-color: #E9EEF2;\n"
"\n"
"    color: #24516F;\n"
"\n"
"    border: 1px solid #B8C5CF;\n"
"}\n"
"\n"
"QPushButton#increaseButton:pressed {\n"
"\n"
"    background-color: #DCE6EC;\n"
"}\n"
"\n"
"QPushButton#increaseButton:disabled {\n"
"	color: #C3C3C3\n"
"}\n"
"/* =========================================================\n"
"   QUANTIDADE\n"
"   =========="
                        "=============================================== */\n"
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
"   BOT\u00c3O REMOVER\n"
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
"    font-size: 13px;\n"
"}\n"
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
"QPushButton#removeItem:pressed {\n"
"\n"
"    background-color: #FEE2E2;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saleItem = QFrame(Form)
        self.saleItem.setObjectName(u"saleItem")
        self.saleItem.setStyleSheet(u"")
        self.saleItem.setFrameShape(QFrame.Shape.StyledPanel)
        self.saleItem.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.saleItem)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardLayout = QVBoxLayout()
        self.cardLayout.setSpacing(8)
        self.cardLayout.setObjectName(u"cardLayout")
        self.cardLayout.setContentsMargins(12, 12, 12, 12)
        self.productContainer = QWidget(self.saleItem)
        self.productContainer.setObjectName(u"productContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.productContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.productContainerLayout = QHBoxLayout()
        self.productContainerLayout.setObjectName(u"productContainerLayout")
        self.productContainerLayout.setContentsMargins(-1, -1, -1, 0)
        self.productNameAndPrice = QWidget(self.productContainer)
        self.productNameAndPrice.setObjectName(u"productNameAndPrice")
        self.verticalLayout_4 = QVBoxLayout(self.productNameAndPrice)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.productNameAndPriceLayout = QVBoxLayout()
        self.productNameAndPriceLayout.setSpacing(7)
        self.productNameAndPriceLayout.setObjectName(u"productNameAndPriceLayout")
        self.productNameLabel = QLabel(self.productNameAndPrice)
        self.productNameLabel.setObjectName(u"productNameLabel")
        font = QFont()
        font.setWeight(QFont.DemiBold)
        self.productNameLabel.setFont(font)

        self.productNameAndPriceLayout.addWidget(self.productNameLabel)

        self.productPricexQuantityWidget = QWidget(self.productNameAndPrice)
        self.productPricexQuantityWidget.setObjectName(u"productPricexQuantityWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.productPricexQuantityWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.productPricexQuantityLayout = QHBoxLayout()
        self.productPricexQuantityLayout.setObjectName(u"productPricexQuantityLayout")
        self.productBasePriceLabel = QLabel(self.productPricexQuantityWidget)
        self.productBasePriceLabel.setObjectName(u"productBasePriceLabel")
        font1 = QFont()
        self.productBasePriceLabel.setFont(font1)

        self.productPricexQuantityLayout.addWidget(self.productBasePriceLabel)

        self.productPricexQuantityHS = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.productPricexQuantityLayout.addItem(self.productPricexQuantityHS)


        self.horizontalLayout_4.addLayout(self.productPricexQuantityLayout)


        self.productNameAndPriceLayout.addWidget(self.productPricexQuantityWidget)


        self.verticalLayout_4.addLayout(self.productNameAndPriceLayout)


        self.productContainerLayout.addWidget(self.productNameAndPrice)

        self.productTotalPriceLabel = QLabel(self.productContainer)
        self.productTotalPriceLabel.setObjectName(u"productTotalPriceLabel")
        font2 = QFont()
        font2.setBold(True)
        self.productTotalPriceLabel.setFont(font2)

        self.productContainerLayout.addWidget(self.productTotalPriceLabel)


        self.horizontalLayout_3.addLayout(self.productContainerLayout)


        self.cardLayout.addWidget(self.productContainer)

        self.quantityButtons = QWidget(self.saleItem)
        self.quantityButtons.setObjectName(u"quantityButtons")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantityButtons.sizePolicy().hasHeightForWidth())
        self.quantityButtons.setSizePolicy(sizePolicy)
        self.quantityButtons.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.quantityButtons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.quantityButtonsLayout = QHBoxLayout()
        self.quantityButtonsLayout.setObjectName(u"quantityButtonsLayout")
        self.qttButtonHSpacerL = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.quantityButtonsLayout.addItem(self.qttButtonHSpacerL)

        self.decreaseButton = QPushButton(self.quantityButtons)
        self.decreaseButton.setObjectName(u"decreaseButton")
        self.decreaseButton.setMinimumSize(QSize(32, 32))
        self.decreaseButton.setMaximumSize(QSize(32, 32))

        self.quantityButtonsLayout.addWidget(self.decreaseButton)

        self.productQuantityLabel = QLabel(self.quantityButtons)
        self.productQuantityLabel.setObjectName(u"productQuantityLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.productQuantityLabel.sizePolicy().hasHeightForWidth())
        self.productQuantityLabel.setSizePolicy(sizePolicy1)
        self.productQuantityLabel.setScaledContents(False)
        self.productQuantityLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.quantityButtonsLayout.addWidget(self.productQuantityLabel)

        self.increaseButton = QPushButton(self.quantityButtons)
        self.increaseButton.setObjectName(u"increaseButton")
        self.increaseButton.setMinimumSize(QSize(32, 32))
        self.increaseButton.setMaximumSize(QSize(32, 32))

        self.quantityButtonsLayout.addWidget(self.increaseButton)

        self.qttButtonHSpacerR = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.quantityButtonsLayout.addItem(self.qttButtonHSpacerR)

        self.removeButton = QPushButton(self.quantityButtons)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setMinimumSize(QSize(90, 28))

        self.quantityButtonsLayout.addWidget(self.removeButton)


        self.horizontalLayout_2.addLayout(self.quantityButtonsLayout)


        self.cardLayout.addWidget(self.quantityButtons)


        self.verticalLayout_3.addLayout(self.cardLayout)


        self.verticalLayout_2.addWidget(self.saleItem)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.productNameLabel.setText(QCoreApplication.translate("Form", u"Ray-Ban RX123", None))
        self.productBasePriceLabel.setText(QCoreApplication.translate("Form", u"R$ 599,90 x", None))
        self.productTotalPriceLabel.setText(QCoreApplication.translate("Form", u"R$ 599,90", None))
        self.decreaseButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.productQuantityLabel.setText(QCoreApplication.translate("Form", u"1", None))
        self.increaseButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.removeButton.setText(QCoreApplication.translate("Form", u"Remover", None))
    # retranslateUi

