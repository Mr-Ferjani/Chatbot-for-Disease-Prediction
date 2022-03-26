
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
import os
import sys
from PyQt5.QtGui import *
from Uiapp import Ui_MainWindow
from functools import partial
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QDateTime
from modules import *
counter = 0
class MainWindow(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        ############################################################### them 
        Theme.inint_ui(self)
        Theme.actionbutton(self)
        ############################################################### uifunctions
        Uifunctions.inint_ui(self)
        Uifunctions.actionbutton(self)
        ############################################################### splash screen 
        self.timer = QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.progress2)
        self.timer.start()
    # progresse bar for splash screen
    def progress2(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.ui.stackedWidget_login.setCurrentIndex(0)
        counter +=1
       


if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = MainWindow()
    sys.exit(app.exec_())




