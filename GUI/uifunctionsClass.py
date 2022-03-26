from Setup import reply
from App import *
from functools import partial
from PyQt5 import QtTest
from PyQt5.QtWidgets import *
class Uifunctions(MainWindow):

    def inint_ui(self):
        self.ui.typing.hide()
    def actionbutton(self):
        # create a enter key listener for sending messages 
        self.shortcut_savefile = QShortcut(QKeySequence(Qt.Key_Enter), self)
        self.shortcut_savefile1 = QShortcut(QKeySequence(Qt.Key_Return), self)
        self.shortcut_savefile.activated.connect(partial(Uifunctions.entremessage, self))
        self.shortcut_savefile1.activated.connect(partial(Uifunctions.entremessage, self))
        # create a listener for the send text message  button 
        self.ui.send.clicked.connect(partial(Uifunctions.entremessage, self))
        # create a listener for send file button 
        self.ui.files.clicked.connect(partial(Uifunctions.sendimage , self ))

        
    

    def entremessage(self):
        # get the message from the edit line 
        the_message = self.ui.msg.text()
        #Uifunctions.messageuser(self)
        #QtTest.QTest.qWait(700)
        #self.ui.typing.show()
        #QtTest.QTest.qWait(700)
        #Uifunctions.botmessage(self,the_message)
        
        if the_message !='' :
            # create user message
            Uifunctions.messageuser(self)
            # deley for 0.7 sec 
            QtTest.QTest.qWait(700)
            # show typing bot label 
            self.ui.typing.show()
            # deley for 0.7 sec 
            QtTest.QTest.qWait(700)
            # create bot message
            Uifunctions.botmessage(self,the_message)
        
    def messageuser(self):
        self.messgeuser = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        self.messgeuser.setMinimumSize(QtCore.QSize(200, 30))
        self.messgeuser.setObjectName("messgeuser")
        self.ui.verticalLayout_2.addWidget(self.messgeuser, 0, QtCore.Qt.AlignRight)
        if len(self.ui.msg.text()) > 20 : 
            self.messgeuser.setText(self.ui.msg.text()[0:20]+'\n'+self.ui.msg.text()[20:])
        else :
            self.messgeuser.setText(self.ui.msg.text())
        self.ui.msg.setText('')
        
    def botmessage(self,the_message):
        self.messagebot = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        self.messagebot.setMinimumSize(QtCore.QSize(200, 30))
        
        self.messagebot.setStyleSheet("background-color:#858585 ;\n"
                                    "border-radius: 5px;\n"
                                    "color :white ;\n"
                                    "padding-left: 8px;\n"
                                    "font: 10pt \"Segoe UI\";")
        self.messagebot.setObjectName("messagebot")
        self.ui.verticalLayout_2.addWidget(self.messagebot, 0, QtCore.Qt.AlignLeft)
        #self.messagebot.setText('bot response ! ')
        #msg = f'Dr.Stone: {the_message}\n'
        #self.messagebot.setText(msg)
        self.messagebot.setText(reply(the_message))
        self.ui.typing.hide()
            

    

    def sendimage(self):
        print('send images !')

    


    