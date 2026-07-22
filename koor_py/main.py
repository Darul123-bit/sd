from random import randint
import math as m
import sys

from PySide6.GtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Central area")
        self.setWindowIcon(QIcon("icons/file.png"))
        
        centralArea = QWidget()
        
        centralArea.setStyleSheet("background: #1A1A1A")
        
        self.setCentralWidget(centralArea)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec())

    
    


