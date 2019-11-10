import sys
import cv2 as cv
import numpy as np
import socket

from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QMessageBox)


class mythred(QThread):
    sinOut = pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__()


    def run(self):
        while True:
            self.timer = QTimer(self)
            # self.timer.timeout.connect(self.recv)
          #  print("线程开启")
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.bind(("", 8080))
            recv_data = udp_socket.recvfrom(1024)
            ip = recv_data[1]
            r = int(recv_data[0].decode("utf_8"))
           # print(">>>%s: %s " % (str(ip), r))
            self.sinOut.emit(r)
            self.timer.start(1000)


class win(QDialog):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle("circle")
        self.label = QLabel(self)
        self.label.setGeometry(50,50,400,400)
        self.btnOpen = QPushButton('start', self)
        self.btnOpen.move(400,500)

        # 信号与槽连接, PyQt5与Qt5相同, 信号可绑定普通成员函数
        self.btnOpen.clicked.connect(self.star)



    def star(self):
        self.thread = mythred()
        self.thread.sinOut.connect(self.openSlot)
        self.thread.start()





    # def start_dynamic_plot(self):
    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.recv)
    #     self.timer.start(1000)
    #     #self.timer.stop()


    # def recv(self):
    #     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     udp_socket.bind(("", 8080))
    #     recv_data = udp_socket.recvfrom(1024)
    #     ip = recv_data[1]
    #     global i
    #     i = int(recv_data[0].decode("utf_8"))
    #     print(">>>%s: %s " % (str(ip), i))
    #     self.openSlot()

    def openSlot(self,r):
        # 采用opencv函数读取数据
        # if i == 10:
        #     global tag
        #     tag = 1
        # elif i <= 0:
        #     tag = 0
        #
        # if tag == 1:
        #     global i
        #     i = i - 1
        # elif tag == 0:
        #     i = i + 1



        img = np.zeros((400,400,3), np.uint8)

        point_color = (0, 0, 255)
        self.img = cv.circle(img,(200, 200), 15*int(r), point_color,thickness=-1)


        self.refreshShow()

    def refreshShow(self):
        # 提取图像的尺寸和通道, 用于将opencv下的image转换成Qimage
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()

        # 将Qimage显示出来
        self.label.setPixmap(QPixmap.fromImage(self.qImg))

    def closeEvent(self, event):

            reply =QMessageBox.question(self,
                                            '本程序',
                                            "是否要退出程序？",
                                            QMessageBox.Yes |QMessageBox.No,
                                            QMessageBox.No)
            if reply ==QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()






if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = win()
    w.show()
    sys.exit(a.exec_())