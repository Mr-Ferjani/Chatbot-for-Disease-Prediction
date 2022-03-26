from App import *
from functools import partial

class Theme(MainWindow):

    def inint_ui(self):
        self.ui.more_panal.setIcon(Theme.QIcon_from_svg(self , ':/image/logo.svg' , 'white'))
        self.ui.files.setIcon(Theme.QIcon_from_svg(self , ':/image/uicons-regular-rounded/uicons-regular-rounded/svg/fi-rr-clip.svg' , 'white'))
        self.ui.send.setIcon(Theme.QIcon_from_svg(self , ':/image/uicons-solid-rounded/uicons-solid-rounded/svg/fi-sr-undo.svg' , 'white'))
        self.ui.logo.setIcon(Theme.QIcon_from_svg(self , ':/image/logo.svg' , 'white'))

    def actionbutton(self):
        pass
    
    def QIcon_from_svg(self , svg_filepath, color):
        img = QPixmap(svg_filepath)
        qp = QPainter(img)
        qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
        qp.fillRect( img.rect(), QColor(color) )
        qp.end()
        return QIcon(img)
    
    def Qmessage(self , titel , the_message , type):
        # warning / error =====> the cloud image 
        # information / confirmation  ===== > the comment image
        if type ==1 :
            msgBox = QMessageBox(self)
            msgBox.setWindowTitle(titel)
            msgBox.setText(the_message)
            msgBox.setIconPixmap(QPixmap(':/image/cil-rain.png')) 
            msgBox.exec()
        else:
            msgBox = QMessageBox(self)
            msgBox.setWindowTitle(titel)
            msgBox.setText(the_message)
            msgBox.setIconPixmap(QPixmap(':/image/cil-comment-bubble.png'))
            msgBox.exec()
   
    def FramQmessage_box(color_theme):
        Qwidget = "QWidget{background-color :transparent ;color : white;}"
        Qmsg1 = "QMessageBox {background-color: rgb(35, 35, 35);}"
        Qmsg2 = "QMessageBox QLabel {color: rgb(255, 255, 255);	font: 10pt \"Segoe UI\";}"
        Qmsg3 = "QMessageBox QPushButton {background-color: rgb(50, 50, 50);border: 2px solid rgb(60, 60, 60);border-radius: 2px;color: white;font: 10pt \"Segoe UI\";Width : 100 px;	Height : 30 px;}"
        Qmsg4 = "QMessageBox QPushButton:hover {background-color: "+color_theme+";border: 2px solid rgb(70, 70, 70);}"
        Qmsg5 = "QMessageBox QPushButton:pressed {background-color:"+color_theme+";	border: 2px solid "+color_theme+" ;color: white;}"
        Qcss_fram_main =  Qwidget + Qmsg1 +Qmsg2 +Qmsg3 + Qmsg4 +Qmsg5
        return Qcss_fram_main
    
    

  
        








