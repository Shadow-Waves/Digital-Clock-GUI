from PyQt6.QtCore import QTime,QTimer,QDate
from PyQt6.QtWidgets import QWidget,QApplication,QLabel
from PyQt6.QtGui import QIcon
from sys import argv

class DateTime(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DateTime")
        self.setWindowIcon(QIcon("C:\\Users\\Hafedh\\Desktop\\Time\\dt.png"))
        self.setFixedSize(400,200)
        self.setStyleSheet("background-color:black;")

        self.mainfield = QLabel(QTime.currentTime().toString(),self)
        self.mainfield.setGeometry(20,0,400,180)
        self.mainfield.setStyleSheet("background-color:transparent;color:magenta;font-size:100px;")
        
        self.date = QLabel(QDate.currentDate().toString(),self)
        self.date.setGeometry(120,50,400,200)
        self.date.setStyleSheet("background-color:transparent;color:lightgreen;font-size:20px;")
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changer)
        self.timer.start()

        self.show()

    def changer(self):
        self.mainfield.setText(QTime.currentTime().toString())
        self.date.setText(QDate.currentDate().toString())

if __name__ == "__main__":
    application = QApplication(argv)
    DT = DateTime()
    application.exec()