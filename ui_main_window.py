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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

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
"")
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

        self.pagesStackedWidget = QStackedWidget(self.centralwidget)
        self.pagesStackedWidget.setObjectName(u"pagesStackedWidget")
        self.salePage = QWidget()
        self.salePage.setObjectName(u"salePage")
        self.horizontalLayout_8 = QHBoxLayout(self.salePage)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pagesStackedWidget.addWidget(self.salePage)
        self.ordersPage = QWidget()
        self.ordersPage.setObjectName(u"ordersPage")
        self.pagesStackedWidget.addWidget(self.ordersPage)

        self.centralLayout.addWidget(self.pagesStackedWidget)


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
    # retranslateUi

