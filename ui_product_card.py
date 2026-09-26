# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_card.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(220, 266)
        Form.setMinimumSize(QSize(180, 0))
        Form.setMaximumSize(QSize(280, 280))
        Form.setStyleSheet(u"/* =========================================================\n"
"   PRODUCT CARD\n"
"   ========================================================= */\n"
"\n"
"QFrame#productCard {\n"
"    background-color: #FFFFFF;\n"
"\n"
"    border: 1px solid #DDE3E8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   IMAGEM DO PRODUTO\n"
"   ========================================================= */\n"
"\n"
"QLabel#productImageLabel {\n"
"    background-color: #F7F8FA;\n"
"\n"
"    color: #6B7280;\n"
"\n"
"    border: 1px solid #EEF0F2;\n"
"    border-radius: 7px;\n"
"\n"
"    font-size: 13px;\n"
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
"   PRE\u00c7O\n"
"   ========================================================= */\n"
"\n"
"QLabel#productPriceLabel {\n"
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
"   ESTOQUE\n"
"   ========================================================= */\n"
"\n"
"QLabel#productStockLabel {\n"
"    color: #6B7280;\n"
"\n"
"    font-size: 13px;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   BOT\u00c3O ADICIONAR\n"
"   ========================================================= */\n"
"\n"
"QPushButton#addProductButton {\n"
"    background-color: #FFFFFF;\n"
"\n"
"    color: #374151;\n"
"\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"\n"
"    min-height: 34"
                        "px;\n"
"\n"
"    padding: 6px 12px;\n"
"\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"\n"
"/* Hover */\n"
"\n"
"QPushButton#addProductButton:hover {\n"
"    background-color: #EEF4F8;\n"
"\n"
"    color: #24516F;\n"
"\n"
"    border: 1px solid #9FB5C5;\n"
"}\n"
"\n"
"\n"
"/* Pressionado */\n"
"\n"
"QPushButton#addProductButton:pressed {\n"
"    background-color: #DDEAF2;\n"
"\n"
"    border: 1px solid #8EAABB;\n"
"}\n"
"\n"
"\n"
"/* Desabilitado */\n"
"\n"
"QPushButton#addProductButton:disabled {\n"
"    background-color: #F3F4F6;\n"
"\n"
"    color: #9CA3AF;\n"
"\n"
"    border: 1px solid #E5E7EB;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.productCard = QFrame(Form)
        self.productCard.setObjectName(u"productCard")
        self.productCard.setStyleSheet(u"")
        self.productCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.productCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.productCard)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cardLayout = QVBoxLayout()
        self.cardLayout.setSpacing(8)
        self.cardLayout.setObjectName(u"cardLayout")
        self.cardLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.cardLayout.setContentsMargins(12, 12, 12, 12)
        self.productImageLabel = QLabel(self.productCard)
        self.productImageLabel.setObjectName(u"productImageLabel")
        self.productImageLabel.setMinimumSize(QSize(0, 110))
        self.productImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cardLayout.addWidget(self.productImageLabel)

        self.productNameLabel = QLabel(self.productCard)
        self.productNameLabel.setObjectName(u"productNameLabel")
        font = QFont()
        font.setWeight(QFont.DemiBold)
        self.productNameLabel.setFont(font)
        self.productNameLabel.setWordWrap(True)

        self.cardLayout.addWidget(self.productNameLabel)

        self.productPriceLabel = QLabel(self.productCard)
        self.productPriceLabel.setObjectName(u"productPriceLabel")
        font1 = QFont()
        font1.setBold(True)
        self.productPriceLabel.setFont(font1)

        self.cardLayout.addWidget(self.productPriceLabel)

        self.productStockLabel = QLabel(self.productCard)
        self.productStockLabel.setObjectName(u"productStockLabel")

        self.cardLayout.addWidget(self.productStockLabel)

        self.addProductButton = QPushButton(self.productCard)
        self.addProductButton.setObjectName(u"addProductButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addProductButton.sizePolicy().hasHeightForWidth())
        self.addProductButton.setSizePolicy(sizePolicy)
        self.addProductButton.setMinimumSize(QSize(0, 48))

        self.cardLayout.addWidget(self.addProductButton)


        self.verticalLayout_3.addLayout(self.cardLayout)


        self.verticalLayout_2.addWidget(self.productCard)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.productImageLabel.setText(QCoreApplication.translate("Form", u"IMAGEM", None))
        self.productNameLabel.setText(QCoreApplication.translate("Form", u"Rayban RX123", None))
        self.productPriceLabel.setText(QCoreApplication.translate("Form", u"R$ 599,90", None))
        self.productStockLabel.setText(QCoreApplication.translate("Form", u"Estoque: 4", None))
        self.addProductButton.setText(QCoreApplication.translate("Form", u"Adicionar", None))
    # retranslateUi

