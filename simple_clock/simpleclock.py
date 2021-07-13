from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time

class window:
    am_pm_str = time.strftime('%p')
    def __init__(self):
        self.widget = QWidget()
        self.label = QLabel(self.widget)
        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.label)
        self.widget.setLayout(self.layout)

#window-style
        
        self.label.move(25,25)
        self.widget.setWindowIcon(QtGui.QIcon('simple_clock_png.png'))
        self.widget.setWindowTitle('Clock')
        self.widget.setFixedSize(650,100)
        self.widget.show()
#style
        
        self.label.setAlignment(Qt.AlignCenter)

        value = ('AM','PM')

        if self.am_pm_str == value[0]:
            self.widget.setStyleSheet("QWidget{background-color:#005153;}")
            self.label.setStyleSheet("QLabel{font:60px;color:#003032;}") #[if day background green and color black]
        else:
            self.widget.setStyleSheet("QWidget{background-color:#0e2f44;}")
            self.label.setStyleSheet("QLabel{font:60px;color:#b1b4e2;}") #[else do opposit]


#loop
       
        self.timer = QTimer()
        self.timer.timeout.connect(self.startClock)
        self.timer.start(1000)

    def startClock(self):
        currentTime = (time.localtime())
        currentTime_str = str(currentTime[3]-12)+' : '+str(currentTime[4])+' : '+str(currentTime[5])+' : '+self.am_pm_str+' '+ str(currentTime[2])+'/'+str(currentTime[1])
        self.label.setText(currentTime_str)

     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    sys.exit(app.exec_())