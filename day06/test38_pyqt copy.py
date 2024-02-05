# date : 2024-02-05
# desc : Qt디자이너로 만든 ui와 연동 

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): 
    def __init__(self) -> None:
        super().__init__() 
        uic.loadUi('./day06/testApp.ui', self) 

if __name__ == '__main__': 
    loop = QApplication(sys.argv)
    istance = qtwin_exam()
    istance.show()
    loop.exec_()
    
