# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finalize_sale_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_finalizeSaleDialog(object):
    def setupUi(self, finalizeSaleDialog):
        if not finalizeSaleDialog.objectName():
            finalizeSaleDialog.setObjectName(u"finalizeSaleDialog")
        finalizeSaleDialog.resize(400, 300)
        finalizeSaleDialog.setStyleSheet(u"/* =========================================================\n"
"   FINALIZE SALE DIALOG\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog {\n"
"    background-color: #FFFFFF;\n"
"    color: #1F2937;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   T\u00cdTULO\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QLabel#titleLabel {\n"
"    color: #111827;\n"
"\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    padding-bottom: 4px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   T\u00cdTULOS DOS CAMPOS\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QLabel#customerTitleLabel,\n"
"QDialog#finalizeSaleDialog QLabel#totalTitleLabel,\n"
"QDialog#finalizeSaleDialog QLabel#paymentMethodsTitleLabel {\n"
""
                        "    color: #374151;\n"
"\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    padding-top: 4px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   CLIENTE\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QLabel#customerNameLabel {\n"
"    color: #111827;\n"
"\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"\n"
"    background-color: #F8F9FA;\n"
"\n"
"    border: 1px solid #E5E7EB;\n"
"    border-radius: 6px;\n"
"\n"
"    padding: 9px 11px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   VALOR TOTAL\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QLabel#totalValueLabel {\n"
"    color: #24516F;\n"
"\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"\n"
"    background-color: transparent;\n"
"    border: none;\n"
"\n"
"    padding-top: 2px;"
                        "\n"
"    padding-bottom: 4px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   FORMA DE PAGAMENTO\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QComboBox#paymentComboBox {\n"
"    background-color: #FFFFFF;\n"
"\n"
"    color: #1F2937;\n"
"\n"
"    border: 1px solid #D1D5DB;\n"
"    border-radius: 6px;\n"
"\n"
"    padding: 8px 10px;\n"
"\n"
"    min-height: 20px;\n"
"\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"\n"
"QDialog#finalizeSaleDialog QComboBox#paymentComboBox:hover {\n"
"    border: 1px solid #9CAFC0;\n"
"}\n"
"\n"
"\n"
"QDialog#finalizeSaleDialog QComboBox#paymentComboBox:focus {\n"
"    border: 1px solid #4F7FA3;\n"
"}\n"
"\n"
"\n"
"/* ---------- Seta do ComboBox ---------- */\n"
"\n"
"QDialog#finalizeSaleDialog QComboBox#paymentComboBox::drop-down {\n"
"    border: none;\n"
"\n"
"    width: 30px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   LISTA DO COMBOBOX\n"
" "
                        "  ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QComboBox#paymentComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"\n"
"    color: #1F2937;\n"
"\n"
"    border: 1px solid #D1D5DB;\n"
"\n"
"    selection-background-color: #E7F0F7;\n"
"    selection-color: #24516F;\n"
"\n"
"    outline: none;\n"
"\n"
"    padding: 4px;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   CONTAINER DOS BOT\u00d5ES\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QWidget#finalizeSaleButtonsContainer {\n"
"    background-color: transparent;\n"
"\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   CONFIRMAR VENDA\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QPushButton#confirmSaleButton {\n"
"    background-color: #365F7A;\n"
"\n"
"    color: #FFFFFF;\n"
"\n"
" "
                        "   border: 1px solid #365F7A;\n"
"    border-radius: 7px;\n"
"\n"
"    min-height: 38px;\n"
"\n"
"    padding: 7px 16px;\n"
"\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"\n"
"QDialog#finalizeSaleDialog QPushButton#confirmSaleButton:hover {\n"
"    background-color: #2E526A;\n"
"\n"
"    border: 1px solid #2E526A;\n"
"}\n"
"\n"
"\n"
"QDialog#finalizeSaleDialog QPushButton#confirmSaleButton:pressed {\n"
"    background-color: #274657;\n"
"\n"
"    border: 1px solid #274657;\n"
"}\n"
"\n"
"\n"
"QDialog#finalizeSaleDialog QPushButton#confirmSaleButton:disabled {\n"
"    background-color: #CBD5DC;\n"
"\n"
"    color: #F8FAFC;\n"
"\n"
"    border: 1px solid #CBD5DC;\n"
"}\n"
"\n"
"\n"
"/* =========================================================\n"
"   CANCELAR\n"
"   ========================================================= */\n"
"\n"
"QDialog#finalizeSaleDialog QPushButton#cancelSaleButton {\n"
"    background-color: #FFFFFF;\n"
"\n"
"    color: #4B5563;\n"
"\n"
"    border: 1px solid #D1D5DB"
                        ";\n"
"    border-radius: 7px;\n"
"\n"
"    min-height: 38px;\n"
"\n"
"    padding: 7px 16px;\n"
"\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"\n"
"QDialog#finalizeSaleDialog QPushButton#cancelSaleButton:hover {\n"
"    background-color: #FEF2F2;\n"
"\n"
"    color: #B42318;\n"
"\n"
"    border: 1px solid #F0B4B4;\n"
"}\n"
"\n"
"\n"
"QDialog#finalizeSaleDialog QPushButton#cancelSaleButton:pressed {\n"
"    background-color: #FEE2E2;\n"
"\n"
"    color: #991B1B;\n"
"\n"
"    border: 1px solid #ECA5A5;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(finalizeSaleDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(finalizeSaleDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.verticalLayout.addWidget(self.titleLabel)

        self.customerTitleLabel = QLabel(finalizeSaleDialog)
        self.customerTitleLabel.setObjectName(u"customerTitleLabel")
        font1 = QFont()
        font1.setWeight(QFont.DemiBold)
        self.customerTitleLabel.setFont(font1)

        self.verticalLayout.addWidget(self.customerTitleLabel)

        self.customerNameLabel = QLabel(finalizeSaleDialog)
        self.customerNameLabel.setObjectName(u"customerNameLabel")

        self.verticalLayout.addWidget(self.customerNameLabel)

        self.totalTitleLabel = QLabel(finalizeSaleDialog)
        self.totalTitleLabel.setObjectName(u"totalTitleLabel")
        self.totalTitleLabel.setFont(font1)

        self.verticalLayout.addWidget(self.totalTitleLabel)

        self.totalValueLabel = QLabel(finalizeSaleDialog)
        self.totalValueLabel.setObjectName(u"totalValueLabel")

        self.verticalLayout.addWidget(self.totalValueLabel)

        self.paymentMethodsTitleLabel = QLabel(finalizeSaleDialog)
        self.paymentMethodsTitleLabel.setObjectName(u"paymentMethodsTitleLabel")
        self.paymentMethodsTitleLabel.setFont(font1)

        self.verticalLayout.addWidget(self.paymentMethodsTitleLabel)

        self.paymentComboBox = QComboBox(finalizeSaleDialog)
        self.paymentComboBox.setObjectName(u"paymentComboBox")

        self.verticalLayout.addWidget(self.paymentComboBox)

        self.finalizeSaleButtonsContainer = QWidget(finalizeSaleDialog)
        self.finalizeSaleButtonsContainer.setObjectName(u"finalizeSaleButtonsContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.finalizeSaleButtonsContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.finalizeSaleButtonsLayout = QHBoxLayout()
        self.finalizeSaleButtonsLayout.setObjectName(u"finalizeSaleButtonsLayout")
        self.cancelSaleButton = QPushButton(self.finalizeSaleButtonsContainer)
        self.cancelSaleButton.setObjectName(u"cancelSaleButton")
        self.cancelSaleButton.setMinimumSize(QSize(0, 30))

        self.finalizeSaleButtonsLayout.addWidget(self.cancelSaleButton)

        self.confirmSaleButton = QPushButton(self.finalizeSaleButtonsContainer)
        self.confirmSaleButton.setObjectName(u"confirmSaleButton")
        self.confirmSaleButton.setMinimumSize(QSize(0, 30))

        self.finalizeSaleButtonsLayout.addWidget(self.confirmSaleButton)


        self.horizontalLayout_2.addLayout(self.finalizeSaleButtonsLayout)


        self.verticalLayout.addWidget(self.finalizeSaleButtonsContainer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(finalizeSaleDialog)

        QMetaObject.connectSlotsByName(finalizeSaleDialog)
    # setupUi

    def retranslateUi(self, finalizeSaleDialog):
        finalizeSaleDialog.setWindowTitle(QCoreApplication.translate("finalizeSaleDialog", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("finalizeSaleDialog", u"Finalizar Venda", None))
        self.customerTitleLabel.setText(QCoreApplication.translate("finalizeSaleDialog", u"Cliente", None))
        self.customerNameLabel.setText(QCoreApplication.translate("finalizeSaleDialog", u"Cau\u00e3 Navarro", None))
        self.totalTitleLabel.setText(QCoreApplication.translate("finalizeSaleDialog", u"Total", None))
        self.totalValueLabel.setText(QCoreApplication.translate("finalizeSaleDialog", u"R$ 0,00", None))
        self.paymentMethodsTitleLabel.setText(QCoreApplication.translate("finalizeSaleDialog", u"Forma de pagamento", None))
        self.cancelSaleButton.setText(QCoreApplication.translate("finalizeSaleDialog", u"Cancelar", None))
        self.confirmSaleButton.setText(QCoreApplication.translate("finalizeSaleDialog", u"Confirmar Venda", None))
    # retranslateUi

