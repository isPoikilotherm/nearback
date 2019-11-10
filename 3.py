import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.pyplot import MultipleLocator
import cv2 as cv
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QGridLayout,
                             QLabel, QPushButton)
from PyQt5.QtCore import QTimer

import matplotlib.pyplot as plt
import numpy as np
import sys
i=0
tag=0

class My_Main_window(QtWidgets.QMainWindow):


    def __init__(self,parent=None):

        super(My_Main_window,self).__init__(parent)
        # 重新调整大小
        self.resize(800, 659)

        self.lable=QtWidgets.QLabel(self)
        self.lable.move(50,50)
        self.lable.setText("你好？")


        # 添加菜单中的按钮
        self.menu = QtWidgets.QMenu("绘图")
        self.menu_action = QtWidgets.QAction("绘制",self.menu)
        self.menu.addAction(self.menu_action)
        self.menuBar().addMenu(self.menu)
        # 添加事件
        self.menu_action.triggered.connect(self.start_dynamic_plot)
        self.setCentralWidget(QtWidgets.QWidget())

    def start_dynamic_plot(self):
        timer = QTimer(self)
        timer.timeout.connect(self.plot_)
        timer.start(1000)



    # 绘图方法
    def plot_(self):


        img = np.zeros((320, 320, 3), np.uint8)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()

        point_color = (0, 0, 255)

        cv.circle(img, (160, 160), 60, point_color, 0)

        self.lable.setPixmap(QPixmap.fromImage(self.qImg))


    # 将绘制好的图像设置为中心 Widget





       #  # 清屏
       #  plt.cla()
       #
       #  if i==10:
       #      global tag
       #      tag=1
       #  elif i<=0:
       #      tag=0
       #
       #  if tag==1:
       #      global i
       #      i = i-1
       #  elif tag==0:
       #      i=i+1
       #
       #  fig = plt.figure(dpi=40)
       #  fig.add_subplot(111)
       #  # x1=np.arange(-2,2,0.001)
       #  # y1=np.sqrt(6-x1*x1)
       #  # x2 = np.arange(-2, 2, 0.001)
       #  # y2 = -1*np.sqrt(6 - x2 * x2)
       #  # plt.plot(x1,y1,x2,y2)
       #
       #
       #  Q = np.arange(0, np.pi*2, 0.0001)
       #
       #  x_major_locator = MultipleLocator(5)
       #  # 把x轴的刻度间隔设置为5，并存在变量里
       #  y_major_locator = MultipleLocator(5)
       #
       #  ax = plt.gca()
       #  ax.xaxis.set_major_locator(x_major_locator)
       #  # 把x轴的主刻度设置为1的倍数
       #  ax.yaxis.set_major_locator(y_major_locator)
       #
       #
       #
       #
       #  plt.xlim(-20, 20)
       #  plt.ylim(-20, 20)
       #  # plt.plot(i * np.cos(Q), i * np.sin(Q), color='pink')
       #  plt.scatter(i * np.cos(Q), i * np.sin(Q))
       #
       #  plt.axis('equal')
       # # print(x,y)np.pi * 2
       #
       #  #plt.axis('off')
       #  cavans = FigureCanvas(fig)
       #  # 将绘制好的图像设置为中心 Widget
       #  self.setCentralWidget(cavans)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_Main_window()
    main_window.show()
    app.exec()
