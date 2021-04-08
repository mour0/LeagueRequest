# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindowvzveAK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 800))
        MainWindow.setMaximumSize(QSize(700, 800))
        font = QFont()
        font.setFamily(u"Roboto")
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"Icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(33, 33, 33);\n"
"border-radius: 10px;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_bar = QFrame(self.frame)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 60))
        self.top_bar.setStyleSheet(u"background-color: none;")
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 9, 9, 0)
        self.frame_7 = QFrame(self.top_bar)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(900, 16777215))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(800, 16777215))
        font1 = QFont()
        font1.setFamily(u"Roboto Medium")
        font1.setPointSize(15)
        font1.setUnderline(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout_11.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.top_bar)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(100, 16777215))
        self.frame_8.setStyleSheet(u"background-color: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, 9, -1)
        self.btnMinimize = QPushButton(self.frame_8)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(16, 16))
        self.btnMinimize.setMaximumSize(QSize(17, 17))
        self.btnMinimize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(229, 185, 25);\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 206, 28);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.frame_8)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(16, 16))
        self.btnClose.setMaximumSize(QSize(17, 17))
        self.btnClose.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 26, 41);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 10, 26);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnClose)


        self.horizontalLayout_11.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.top_bar)

        self.mid_bar = QFrame(self.frame)
        self.mid_bar.setObjectName(u"mid_bar")
        self.mid_bar.setEnabled(True)
        self.mid_bar.setMaximumSize(QSize(16777215, 760))
        self.mid_bar.setStyleSheet(u"background-color: none;")
        self.mid_bar.setFrameShape(QFrame.StyledPanel)
        self.mid_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mid_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.mid_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.statusFrame = QFrame(self.page)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setMaximumSize(QSize(16777215, 500))
        self.statusFrame.setStyleSheet(u"")
        self.statusFrame.setFrameShape(QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.statusFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.statusFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 9)
        self.txtStatus = QPlainTextEdit(self.frame_5)
        self.txtStatus.setObjectName(u"txtStatus")
        self.txtStatus.setMinimumSize(QSize(0, 400))
        self.txtStatus.setMaximumSize(QSize(16777215, 400))
        font2 = QFont()
        font2.setFamily(u"Roboto Medium")
        font2.setPointSize(9)
        self.txtStatus.setFont(font2)
        self.txtStatus.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txtStatus.setCenterOnScroll(False)

        self.verticalLayout_3.addWidget(self.txtStatus)

        self.btnStatus = QPushButton(self.frame_5)
        self.btnStatus.setObjectName(u"btnStatus")
        self.btnStatus.setMinimumSize(QSize(0, 25))
        self.btnStatus.setMaximumSize(QSize(16777215, 25))
        self.btnStatus.setStyleSheet(u"background-color: rgb(22, 0, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")

        self.verticalLayout_3.addWidget(self.btnStatus)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.statusFrame)

        self.backgroundFrame = QFrame(self.page)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setStyleSheet(u"")
        self.backgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.backgroundFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.txtBg = QLineEdit(self.backgroundFrame)
        self.txtBg.setObjectName(u"txtBg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txtBg.sizePolicy().hasHeightForWidth())
        self.txtBg.setSizePolicy(sizePolicy1)
        self.txtBg.setMinimumSize(QSize(500, 25))
        self.txtBg.setMaximumSize(QSize(16777215, 16777215))
        self.txtBg.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txtBg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.txtBg)

        self.btnBg = QPushButton(self.backgroundFrame)
        self.btnBg.setObjectName(u"btnBg")
        self.btnBg.setMinimumSize(QSize(100, 25))
        self.btnBg.setMaximumSize(QSize(100, 25))
        self.btnBg.setStyleSheet(u"background-color: rgb(22, 0, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")

        self.horizontalLayout_10.addWidget(self.btnBg)


        self.verticalLayout_4.addWidget(self.backgroundFrame)

        self.iconFrame = QFrame(self.page)
        self.iconFrame.setObjectName(u"iconFrame")
        self.iconFrame.setMaximumSize(QSize(16777215, 55))
        self.iconFrame.setStyleSheet(u"")
        self.iconFrame.setFrameShape(QFrame.StyledPanel)
        self.iconFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.iconFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.spinIC = QComboBox(self.iconFrame)
        self.spinIC.setObjectName(u"spinIC")
        self.spinIC.setMinimumSize(QSize(0, 25))
        self.spinIC.setMaximumSize(QSize(500, 25))
        font3 = QFont()
        font3.setFamily(u"Roboto Medium")
        self.spinIC.setFont(font3)
        self.spinIC.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.spinIC.setEditable(False)

        self.horizontalLayout_7.addWidget(self.spinIC)

        self.btnIC = QPushButton(self.iconFrame)
        self.btnIC.setObjectName(u"btnIC")
        self.btnIC.setMinimumSize(QSize(100, 25))
        self.btnIC.setMaximumSize(QSize(100, 25))
        self.btnIC.setStyleSheet(u"background-color: rgb(22, 0, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")

        self.horizontalLayout_7.addWidget(self.btnIC)


        self.verticalLayout_4.addWidget(self.iconFrame)

        self.customIconFrame = QFrame(self.page)
        self.customIconFrame.setObjectName(u"customIconFrame")
        self.customIconFrame.setMaximumSize(QSize(16777215, 55))
        self.customIconFrame.setFrameShape(QFrame.StyledPanel)
        self.customIconFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.customIconFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.txtCIC = QLineEdit(self.customIconFrame)
        self.txtCIC.setObjectName(u"txtCIC")
        sizePolicy1.setHeightForWidth(self.txtCIC.sizePolicy().hasHeightForWidth())
        self.txtCIC.setSizePolicy(sizePolicy1)
        self.txtCIC.setMinimumSize(QSize(500, 25))
        self.txtCIC.setMaximumSize(QSize(500, 25))
        self.txtCIC.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txtCIC.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.txtCIC)

        self.btnCIC = QPushButton(self.customIconFrame)
        self.btnCIC.setObjectName(u"btnCIC")
        self.btnCIC.setMinimumSize(QSize(100, 25))
        self.btnCIC.setMaximumSize(QSize(100, 25))
        self.btnCIC.setStyleSheet(u"background-color: rgb(22, 0, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")

        self.horizontalLayout_8.addWidget(self.btnCIC)


        self.verticalLayout_4.addWidget(self.customIconFrame)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spinQueue = QComboBox(self.frame_2)
        self.spinQueue.setObjectName(u"spinQueue")
        self.spinQueue.setMaximumSize(QSize(16777215, 25))
        self.spinQueue.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.spinQueue)

        self.spinTier = QComboBox(self.frame_2)
        self.spinTier.setObjectName(u"spinTier")
        self.spinTier.setMaximumSize(QSize(16777215, 25))
        self.spinTier.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.spinTier)

        self.spinDiv = QComboBox(self.frame_2)
        self.spinDiv.setObjectName(u"spinDiv")
        self.spinDiv.setMaximumSize(QSize(16777215, 25))
        self.spinDiv.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.spinDiv)

        self.btnDiv = QPushButton(self.frame_2)
        self.btnDiv.setObjectName(u"btnDiv")
        self.btnDiv.setMaximumSize(QSize(16777215, 25))
        self.btnDiv.setStyleSheet(u"background-color: rgb(22, 0, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")

        self.verticalLayout_2.addWidget(self.btnDiv)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_9 = QFrame(self.page_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 75))
        self.frame_9.setMaximumSize(QSize(16777215, 25))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 4))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.lineEdit)

        self.btnOffline = QPushButton(self.frame_9)
        self.btnOffline.setObjectName(u"btnOffline")
        self.btnOffline.setMinimumSize(QSize(0, 25))
        self.btnOffline.setStyleSheet(u"background-color: rgb(22, 0, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")

        self.verticalLayout_11.addWidget(self.btnOffline)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_13 = QFrame(self.page_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.spinnerMethod = QComboBox(self.frame_13)
        self.spinnerMethod.setObjectName(u"spinnerMethod")
        self.spinnerMethod.setMinimumSize(QSize(100, 0))
        self.spinnerMethod.setMaximumSize(QSize(16777215, 25))
        self.spinnerMethod.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"QComboBox::down-arrow { image: none; }")
        self.spinnerMethod.setEditable(False)

        self.horizontalLayout_13.addWidget(self.spinnerMethod)

        self.txtEndpoint = QLineEdit(self.frame_13)
        self.txtEndpoint.setObjectName(u"txtEndpoint")
        self.txtEndpoint.setMinimumSize(QSize(0, 25))
        self.txtEndpoint.setMaximumSize(QSize(16777215, 25))
        self.txtEndpoint.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txtEndpoint.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.txtEndpoint)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.frame_11 = QFrame(self.page_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.txtData = QPlainTextEdit(self.frame_11)
        self.txtData.setObjectName(u"txtData")
        self.txtData.setMaximumSize(QSize(16777215, 16777215))
        self.txtData.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.txtData)

        self.txtResp = QPlainTextEdit(self.frame_11)
        self.txtResp.setObjectName(u"txtResp")
        self.txtResp.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.txtResp)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.page_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 25))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnSend = QPushButton(self.frame_12)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setMinimumSize(QSize(0, 25))
        self.btnSend.setStyleSheet(u"background-color: rgb(22, 0, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")

        self.horizontalLayout_12.addWidget(self.btnSend)

        self.txtCode = QLabel(self.frame_12)
        self.txtCode.setObjectName(u"txtCode")
        self.txtCode.setMaximumSize(QSize(100, 25))
        self.txtCode.setStyleSheet(u"background-color: rgb(22, 0, 61);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;")
        self.txtCode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.txtCode)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.mid_bar)

        self.bot_bar = QFrame(self.frame)
        self.bot_bar.setObjectName(u"bot_bar")
        sizePolicy.setHeightForWidth(self.bot_bar.sizePolicy().hasHeightForWidth())
        self.bot_bar.setSizePolicy(sizePolicy)
        self.bot_bar.setMinimumSize(QSize(0, 40))
        self.bot_bar.setMaximumSize(QSize(16777215, 40))
        self.bot_bar.setStyleSheet(u"background-color: rgb(22, 0, 61);")
        self.bot_bar.setFrameShape(QFrame.StyledPanel)
        self.bot_bar.setFrameShadow(QFrame.Raised)
        self.bot_bar.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.bot_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gotoPage1 = QPushButton(self.bot_bar)
        self.gotoPage1.setObjectName(u"gotoPage1")
        self.gotoPage1.setMinimumSize(QSize(0, 40))
        self.gotoPage1.setFont(font2)
        self.gotoPage1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")

        self.horizontalLayout_3.addWidget(self.gotoPage1)

        self.line = QFrame(self.bot_bar)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(1, 1))
        self.line.setMaximumSize(QSize(16777215, 16777215))
        self.line.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.gotoPage2 = QPushButton(self.bot_bar)
        self.gotoPage2.setObjectName(u"gotoPage2")
        self.gotoPage2.setMinimumSize(QSize(0, 40))
        self.gotoPage2.setFont(font2)
        self.gotoPage2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.gotoPage2)

        self.line_2 = QFrame(self.bot_bar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(1, 1))
        self.line_2.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.gotoAdvanced = QPushButton(self.bot_bar)
        self.gotoAdvanced.setObjectName(u"gotoAdvanced")
        self.gotoAdvanced.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Medium")
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setWeight(50)
        self.gotoAdvanced.setFont(font4)
        self.gotoAdvanced.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")

        self.horizontalLayout_3.addWidget(self.gotoAdvanced)

        self.gotoPage1.raise_()
        self.gotoPage2.raise_()
        self.gotoAdvanced.raise_()
        self.line.raise_()
        self.line_2.raise_()

        self.verticalLayout.addWidget(self.bot_bar)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.spinIC.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LeagueRequest", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LeagueRequest", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
        self.txtStatus.setPlainText("")
        self.txtStatus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom Status", None))
        self.btnStatus.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.txtBg.setText("")
        self.txtBg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Background Code", None))
        self.btnBg.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.spinIC.setCurrentText("")
        self.spinIC.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Icon Code", None))
        self.btnIC.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.txtCIC.setText("")
        self.txtCIC.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom Icon Code (0 - 4902)", None))
        self.btnCIC.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.spinDiv.setPlaceholderText("")
        self.btnDiv.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.btnOffline.setText(QCoreApplication.translate("MainWindow", u"Offline Status [Off]", None))
        self.spinnerMethod.setCurrentText("")
        self.spinnerMethod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.txtEndpoint.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endpoint", None))
        self.txtData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data to send", None))
        self.txtResp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Answer", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Send Request", None))
        self.txtCode.setText(QCoreApplication.translate("MainWindow", u"Status Code", None))
        self.gotoPage1.setText(QCoreApplication.translate("MainWindow", u"Icon | Background", None))
        self.gotoPage2.setText(QCoreApplication.translate("MainWindow", u"Division | Offline", None))
        self.gotoAdvanced.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
    # retranslateUi

