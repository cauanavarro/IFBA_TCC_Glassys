# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_selector.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 387)
        Form.setStyleSheet(u"QFrame#customerSelectorFrame, QFrame#selectedCustomerFrame {\n"
"    background-color: white;\n"
"    border: 1px solid #D9E0E5;\n"
"    border-radius: 8px;\n"
"}\n"
"QLineEdit#customerSearchInput {\n"
"    border: 1px solid #D9E0E5;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit#customerSearchInput:focus {\n"
"    border: 1px solid #8FA4B5;\n"
"}\n"
"QListWidget#customerResultsList {\n"
"    border: 1px solid #D9E0E5;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QListWidget#customerResultsList::item {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QListWidget#customerResultsList::item:selected {\n"
"    background-color: #E8EEF2;\n"
"    color: black;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.customerSelectorFrame = QFrame(Form)
        self.customerSelectorFrame.setObjectName(u"customerSelectorFrame")
        self.customerSelectorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.customerSelectorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.customerSelectorFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.customerLayout = QVBoxLayout()
        self.customerLayout.setSpacing(8)
        self.customerLayout.setObjectName(u"customerLayout")
        self.customerTitleLabel = QLabel(self.customerSelectorFrame)
        self.customerTitleLabel.setObjectName(u"customerTitleLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.customerTitleLabel.setFont(font)

        self.customerLayout.addWidget(self.customerTitleLabel)

        self.customerSearchInput = QLineEdit(self.customerSelectorFrame)
        self.customerSearchInput.setObjectName(u"customerSearchInput")
        self.customerSearchInput.setMinimumSize(QSize(0, 40))

        self.customerLayout.addWidget(self.customerSearchInput)

        self.customerResultsList = QListWidget(self.customerSelectorFrame)
        self.customerResultsList.setObjectName(u"customerResultsList")
        self.customerResultsList.setMinimumSize(QSize(0, 100))

        self.customerLayout.addWidget(self.customerResultsList)


        self.verticalLayout_3.addLayout(self.customerLayout)

        self.selectedCustomerFrame = QFrame(self.customerSelectorFrame)
        self.selectedCustomerFrame.setObjectName(u"selectedCustomerFrame")
        self.selectedCustomerFrame.setMinimumSize(QSize(0, 20))
        self.selectedCustomerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.selectedCustomerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.selectedCustomerFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.selectedCustomerLayout = QVBoxLayout()
        self.selectedCustomerLayout.setObjectName(u"selectedCustomerLayout")
        self.selectedCustomerNameLabel = QLabel(self.selectedCustomerFrame)
        self.selectedCustomerNameLabel.setObjectName(u"selectedCustomerNameLabel")

        self.selectedCustomerLayout.addWidget(self.selectedCustomerNameLabel)

        self.selectedCustomerCpfLabel = QLabel(self.selectedCustomerFrame)
        self.selectedCustomerCpfLabel.setObjectName(u"selectedCustomerCpfLabel")

        self.selectedCustomerLayout.addWidget(self.selectedCustomerCpfLabel)

        self.changeCustomerButton = QPushButton(self.selectedCustomerFrame)
        self.changeCustomerButton.setObjectName(u"changeCustomerButton")

        self.selectedCustomerLayout.addWidget(self.changeCustomerButton)


        self.verticalLayout_4.addLayout(self.selectedCustomerLayout)


        self.verticalLayout_3.addWidget(self.selectedCustomerFrame)


        self.verticalLayout_2.addWidget(self.customerSelectorFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.customerTitleLabel.setText(QCoreApplication.translate("Form", u"Cliente", None))
        self.selectedCustomerNameLabel.setText(QCoreApplication.translate("Form", u"Nome do Cliente", None))
        self.selectedCustomerCpfLabel.setText(QCoreApplication.translate("Form", u"CPF: 000.000.000-00", None))
        self.changeCustomerButton.setText(QCoreApplication.translate("Form", u"Trocar Cliente", None))
    # retranslateUi

