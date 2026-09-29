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
        self.verticalLayout_2 = QVBoxLayout(finalizeSaleDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(finalizeSaleDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.verticalLayout.addWidget(self.titleLabel)

        self.customerTitleLabel = QLabel(finalizeSaleDialog)
        self.customerTitleLabel.setObjectName(u"customerTitleLabel")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
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
        self.confirmSaleButton = QPushButton(self.finalizeSaleButtonsContainer)
        self.confirmSaleButton.setObjectName(u"confirmSaleButton")

        self.finalizeSaleButtonsLayout.addWidget(self.confirmSaleButton)

        self.cancelSaleButton = QPushButton(self.finalizeSaleButtonsContainer)
        self.cancelSaleButton.setObjectName(u"cancelSaleButton")

        self.finalizeSaleButtonsLayout.addWidget(self.cancelSaleButton)


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
        self.confirmSaleButton.setText(QCoreApplication.translate("finalizeSaleDialog", u"Confirmar Venda", None))
        self.cancelSaleButton.setText(QCoreApplication.translate("finalizeSaleDialog", u"Cancelar", None))
    # retranslateUi

