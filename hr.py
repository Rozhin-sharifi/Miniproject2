# This Python file uses the following encoding: utf-8
import sys
import os
import cv2

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QImage, QPixmap
from sqlite3 import connect

con = connect("HR.db")
my_cursor = con.cursor()


class HR(QWidget):
    def __init__(self):
        super(HR, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("mainwindow.ui")
        self.ui.show()
        self.ui.btn1.clicked.connect(self.show)
        self.ui.btn3.clicked.connect(self.insert)
        self.ui.btn2.clicked.connect(self.edit)

    def show(self):
        my_cursor.execute("SELECT DISTINCT first_name, last_name, Pic FROM workers")
        result = my_cursor.fetchall()
        self.ui.tb1.setText(str(result))

    def insert(self):
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        return_value, image = camera.read()
        cv2.imwrite("image.png", image)
        camera.release()
        pixmap=QPixmap('image.png')
        self.ui.pic1.setPixmap(pixmap)
        my_cursor.execute("INSERT INTO workers(ID,first_name,last_name,Na_code,Pic) VALUES(3,'nima','gnb',8,'')")

    def edit(self):
        my_cursor.execute("UPDATE workers SET first_name='amin' WHERE ID=3")



if __name__=="__main__":
    app = QApplication([])
    window = HR()
    sys.exit(app.exec())



