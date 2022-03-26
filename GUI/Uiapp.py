# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIviews\Uiapp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 698)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color : rgb(35,35,35)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget_login = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_login.setObjectName("stackedWidget_login")
        self.application_page = QtWidgets.QWidget()
        self.application_page.setObjectName("application_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.application_page)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.TheApplication = QtWidgets.QFrame(self.application_page)
        self.TheApplication.setStyleSheet("")
        self.TheApplication.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TheApplication.setObjectName("TheApplication")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TheApplication)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.THEAPPLICATIONCHILD = QtWidgets.QVBoxLayout()
        self.THEAPPLICATIONCHILD.setObjectName("THEAPPLICATIONCHILD")
        self.TOPbar = QtWidgets.QFrame(self.TheApplication)
        self.TOPbar.setMinimumSize(QtCore.QSize(0, 81))
        self.TOPbar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.TOPbar.setStyleSheet("background-color : rgb(35, 35, 35)")
        self.TOPbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TOPbar.setObjectName("TOPbar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.TOPbar)
        self.horizontalLayout_2.setContentsMargins(20, 9, 20, 9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.more_panal = QtWidgets.QPushButton(self.TOPbar)
        self.more_panal.setMinimumSize(QtCore.QSize(40, 40))
        self.more_panal.setMaximumSize(QtCore.QSize(40, 40))
        self.more_panal.setBaseSize(QtCore.QSize(30, 30))
        self.more_panal.setStyleSheet("QPushButton{ \n"
"border-radius: 10px;\n"
"border-width: 3px;\n"
"border-color: black ;\n"
"padding : 0px;\n"
" }\n"
"")
        self.more_panal.setText("")
        self.more_panal.setIcon(icon)
        self.more_panal.setIconSize(QtCore.QSize(35, 35))
        self.more_panal.setObjectName("more_panal")
        self.horizontalLayout_2.addWidget(self.more_panal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.TOPbar)
        self.label.setStyleSheet("font: 87 14pt \"Segoe UI Black\";\n"
"color : #858585;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.THEAPPLICATIONCHILD.addWidget(self.TOPbar)
        self.PAGES = QtWidgets.QHBoxLayout()
        self.PAGES.setObjectName("PAGES")
        self.LESPAGES = QtWidgets.QStackedWidget(self.TheApplication)
        self.LESPAGES.setStyleSheet("QWidget{\n"
"background-color :  rgb(45,45,45);\n"
"font: 12pt \"Segoe UI\";\n"
"color : black;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"      border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #005EB8;\n"
"    min-width: 25px;\n"
"      border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"       border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"       border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"       border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical { \n"
"       background: #005EB8;\n"
"        min-height: 25px;\n"
"       border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"       border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"       border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"       border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"QLineEdit {\n"
"background-color: transparent;\n"
"border-radius: 15px;\n"
"color :white ;\n"
"border: 2px solid #858585;\n"
"padding-left: 15px;\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid #005EB8 ;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #005EB8 ;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox {\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"color :white ;\n"
"border: 1px solid white;\n"
"padding: 3px;\n"
"font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: transparent;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 0px;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/image/DownArrow_white.png);\n"
" width: 15px; \n"
" height: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(70, 130, 180) ;\n"
"}\n"
"\n"
"QCheckBox{\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color : white;\n"
"\n"
"}\n"
"QPushButton{ \n"
"background-color:#00acd2 ;\n"
"border-radius: 5px;\n"
"color : white ;\n"
"border: 1px solid white;\n"
"padding: 3px;\n"
"    font: 87 12pt \"Segoe UI Black\";\n"
" }\n"
"QPushButton:hover{\n"
"    font: 87 12.5pt \"Segoe UI Black\";\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"background-color:#005EB8 ;\n"
"border-radius: 5px;\n"
"color :white ;\n"
"border: 2px solid #858585;\n"
"padding: 5px;\n"
"font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"")
        self.LESPAGES.setObjectName("LESPAGES")
        self.Home = QtWidgets.QWidget()
        self.Home.setStyleSheet("")
        self.Home.setObjectName("Home")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.Home)
        self.gridLayout_17.setHorizontalSpacing(6)
        self.gridLayout_17.setVerticalSpacing(15)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.msg = QtWidgets.QLineEdit(self.Home)
        self.msg.setMinimumSize(QtCore.QSize(0, 35))
        self.msg.setMaximumSize(QtCore.QSize(16777215, 35))
        self.msg.setObjectName("msg")
        self.horizontalLayout_3.addWidget(self.msg)
        self.files = QtWidgets.QPushButton(self.Home)
        self.files.setMinimumSize(QtCore.QSize(40, 40))
        self.files.setMaximumSize(QtCore.QSize(40, 40))
        self.files.setBaseSize(QtCore.QSize(30, 30))
        self.files.setStyleSheet("QPushButton{ \n"
"padding : 0px;\n"
"border : none;\n"
"background-color : none;\n"
" }")
        self.files.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/uicons-regular-rounded/uicons-regular-rounded/svg/fi-rr-clip.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.files.setIcon(icon1)
        self.files.setIconSize(QtCore.QSize(20, 20))
        self.files.setObjectName("files")
        self.horizontalLayout_3.addWidget(self.files)
        self.send = QtWidgets.QPushButton(self.Home)
        self.send.setMinimumSize(QtCore.QSize(40, 40))
        self.send.setMaximumSize(QtCore.QSize(40, 40))
        self.send.setBaseSize(QtCore.QSize(30, 30))
        self.send.setStyleSheet("QPushButton{ \n"
"padding : 0px;\n"
"border : none;\n"
"background-color : none;\n"
" }")
        self.send.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/uicons-solid-rounded/uicons-solid-rounded/svg/fi-sr-undo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send.setIcon(icon2)
        self.send.setIconSize(QtCore.QSize(20, 20))
        self.send.setObjectName("send")
        self.horizontalLayout_3.addWidget(self.send)
        self.gridLayout_17.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.Home)
        self.scrollArea.setStyleSheet("border : none; ")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 685, 490))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_17.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.typing = QtWidgets.QLabel(self.Home)
        self.typing.setStyleSheet("background-color:none ;\n"
"color :#858585 ;\n"
"font: italic 10pt \"Segoe UI\";\n"
"border : none ;")
        self.typing.setObjectName("typing")
        self.gridLayout_17.addWidget(self.typing, 2, 0, 1, 1)
        self.LESPAGES.addWidget(self.Home)
        self.PAGES.addWidget(self.LESPAGES)
        self.THEAPPLICATIONCHILD.addLayout(self.PAGES)
        self.horizontalLayout.addLayout(self.THEAPPLICATIONCHILD)
        self.gridLayout_4.addWidget(self.TheApplication, 0, 0, 1, 1)
        self.stackedWidget_login.addWidget(self.application_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.dropShadowFrame = QtWidgets.QFrame(self.page)
        self.dropShadowFrame.setStyleSheet("QFrame {    \n"
"    background-color: rgb(35, 35, 35 );    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 5px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dropShadowFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logo = QtWidgets.QPushButton(self.dropShadowFrame)
        self.logo.setMinimumSize(QtCore.QSize(80, 80))
        self.logo.setMaximumSize(QtCore.QSize(80, 80))
        self.logo.setStyleSheet("QPushButton{ \n"
"background-color :  transparent;\n"
" }")
        self.logo.setText("")
        self.logo.setIcon(icon)
        self.logo.setIconSize(QtCore.QSize(80, 80))
        self.logo.setObjectName("logo")
        self.verticalLayout_3.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter)
        self.label_title = QtWidgets.QLabel(self.dropShadowFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("\n"
"\n"
"QLabel{\n"
"color : white ; \n"
"font: 25 24pt \"Segoe UI Light\";\n"
"background-color : none;\n"
"}")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_3.addWidget(self.label_title)
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 15))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(98, 114, 164);\n"
"    color:white;\n"
"    border-style: none;\n"
"    border-radius: 5px;\n"
"    text-align: center;   \n"
"    font: 7pt \"Roboto\";\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 5px;\n"
"   background-color:qlineargradient(spread:pad, x1:0, y1:0.478, x2:0.96, y2:0.483, stop:0.0113636 rgba(0, 94, 184, 255), stop:1 rgba(52, 115, 231, 255))\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.label_loading = QtWidgets.QLabel(self.dropShadowFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("\n"
"\n"
"QLabel{\n"
"color: white;\n"
"background-color : none; \n"
"}\n"
"")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.verticalLayout_3.addWidget(self.label_loading)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.dropShadowFrame, 0, 0, 1, 1)
        self.stackedWidget_login.addWidget(self.page)
        self.gridLayout.addWidget(self.stackedWidget_login, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_login.setCurrentIndex(1)
        self.LESPAGES.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NHS CHATBOT"))
        self.label.setText(_translate("MainWindow", "NHS ChatBot"))
        self.msg.setPlaceholderText(_translate("MainWindow", "Type something ...."))
        self.typing.setText(_translate("MainWindow", "Bot typing ...."))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p>NHS CHATBOT </p></body></html>"))
        self.label_loading.setText(_translate("MainWindow", "loading..."))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())