# -*- coding: utf-8 -*-
import math

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1277, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 10, 1231, 871))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.radioButton = QtWidgets.QRadioButton(self.page)
        self.radioButton.setGeometry(QtCore.QRect(510, 240, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.page)
        self.radioButton_2.setGeometry(QtCore.QRect(510, 340, 126, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.page)
        self.radioButton_3.setGeometry(QtCore.QRect(510, 290, 110, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.page)
        self.radioButton_4.setGeometry(QtCore.QRect(510, 390, 104, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(530, 480, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(400, 300, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.doubleSpinBoxRadius = QtWidgets.QDoubleSpinBox(self.page_2)
        self.doubleSpinBoxRadius.setGeometry(QtCore.QRect(520, 280, 171, 51))
        self.doubleSpinBoxRadius.setObjectName("doubleSpinBoxRadius")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(480, 480, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(480, 530, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.page_2)
        self.lcdNumber.setGeometry(QtCore.QRect(600, 480, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.page_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(600, 530, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.get_backbutton = QtWidgets.QPushButton(self.page_2)
        self.get_backbutton.setGeometry(QtCore.QRect(530, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_backbutton.setFont(font)
        self.get_backbutton.setObjectName("get_backbutton")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.get_backbutton_2 = QtWidgets.QPushButton(self.page_3)
        self.get_backbutton_2.setGeometry(QtCore.QRect(530, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_backbutton_2.setFont(font)
        self.get_backbutton_2.setObjectName("get_backbutton_2")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(440, 180, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(440, 240, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(440, 300, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.doubleSpinBoxRadius_2 = QtWidgets.QDoubleSpinBox(self.page_3)
        self.doubleSpinBoxRadius_2.setGeometry(QtCore.QRect(530, 290, 171, 51))
        self.doubleSpinBoxRadius_2.setObjectName("doubleSpinBoxRadius_2")
        self.doubleSpinBoxRadius_3 = QtWidgets.QDoubleSpinBox(self.page_3)
        self.doubleSpinBoxRadius_3.setGeometry(QtCore.QRect(530, 230, 171, 51))
        self.doubleSpinBoxRadius_3.setObjectName("doubleSpinBoxRadius_3")
        self.doubleSpinBoxRadius_4 = QtWidgets.QDoubleSpinBox(self.page_3)
        self.doubleSpinBoxRadius_4.setGeometry(QtCore.QRect(530, 170, 171, 51))
        self.doubleSpinBoxRadius_4.setObjectName("doubleSpinBoxRadius_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setGeometry(QtCore.QRect(730, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(460, 440, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(460, 480, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.page_3)
        self.lcdNumber_3.setGeometry(QtCore.QRect(570, 480, 64, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.page_3)
        self.lcdNumber_4.setGeometry(QtCore.QRect(570, 440, 64, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(500, 370, 69, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.get_backbutton_3 = QtWidgets.QPushButton(self.page_4)
        self.get_backbutton_3.setGeometry(QtCore.QRect(530, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_backbutton_3.setFont(font)
        self.get_backbutton_3.setObjectName("get_backbutton_3")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(430, 200, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.doubleSpinBoxRadius_5 = QtWidgets.QDoubleSpinBox(self.page_4)
        self.doubleSpinBoxRadius_5.setGeometry(QtCore.QRect(520, 270, 171, 51))
        self.doubleSpinBoxRadius_5.setObjectName("doubleSpinBoxRadius_5")
        self.doubleSpinBoxRadius_6 = QtWidgets.QDoubleSpinBox(self.page_4)
        self.doubleSpinBoxRadius_6.setGeometry(QtCore.QRect(520, 190, 171, 51))
        self.doubleSpinBoxRadius_6.setObjectName("doubleSpinBoxRadius_6")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(430, 280, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(470, 400, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(470, 460, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.page_4)
        self.lcdNumber_5.setGeometry(QtCore.QRect(590, 400, 64, 23))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.page_4)
        self.lcdNumber_6.setGeometry(QtCore.QRect(590, 460, 64, 23))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_5.setGeometry(QtCore.QRect(720, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.get_backbutton_4 = QtWidgets.QPushButton(self.page_5)
        self.get_backbutton_4.setGeometry(QtCore.QRect(530, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_backbutton_4.setFont(font)
        self.get_backbutton_4.setObjectName("get_backbutton_4")
        self.label_13 = QtWidgets.QLabel(self.page_5)
        self.label_13.setGeometry(QtCore.QRect(410, 230, 70, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.doubleSpinBoxRadius_7 = QtWidgets.QDoubleSpinBox(self.page_5)
        self.doubleSpinBoxRadius_7.setGeometry(QtCore.QRect(510, 220, 171, 51))
        self.doubleSpinBoxRadius_7.setObjectName("doubleSpinBoxRadius_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_6.setGeometry(QtCore.QRect(720, 230, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_14 = QtWidgets.QLabel(self.page_5)
        self.label_14.setGeometry(QtCore.QRect(470, 420, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setGeometry(QtCore.QRect(470, 360, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.page_5)
        self.lcdNumber_7.setGeometry(QtCore.QRect(580, 420, 64, 23))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.page_5)
        self.lcdNumber_8.setGeometry(QtCore.QRect(580, 360, 64, 23))
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.stackedWidget.setCurrentIndex(0)

        self.pushButton.clicked.connect(self.select_shape)
        self.get_backbutton.clicked.connect(self.get_back)
        self.get_backbutton_2.clicked.connect(self.get_back)
        self.get_backbutton_3.clicked.connect(self.get_back)
        self.get_backbutton_4.clicked.connect(self.get_back)

        self.pushButton_3.clicked.connect(self.areaLength_circle)
        self.pushButton_4.clicked.connect(self.areaPerimeter_triangle)
        self.pushButton_5.clicked.connect(self.areaPerimeter_rectangle)
        self.pushButton_6.clicked.connect(self.areaPerimeter_square)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "წრე"))
        self.radioButton_2.setText(_translate("MainWindow", "მართკუთხედი"))
        self.radioButton_3.setText(_translate("MainWindow", "სამკუთხედი"))
        self.radioButton_4.setText(_translate("MainWindow", "კვადრატი"))
        self.pushButton.setText(_translate("MainWindow", "შემდეგი"))
        self.label.setText(_translate("MainWindow", "რადიუსი:"))
        self.label_2.setText(_translate("MainWindow", "ფართობი"))
        self.label_3.setText(_translate("MainWindow", "სიგრძე"))
        self.get_backbutton.setText(_translate("MainWindow", "უკან დაბრუნება"))
        self.pushButton_3.setText(_translate("MainWindow", "გამოთვლა"))
        self.get_backbutton_2.setText(_translate("MainWindow", "უკან დაბრუნება"))
        self.label_4.setText(_translate("MainWindow", "გვერდი1"))
        self.label_5.setText(_translate("MainWindow", "გვერდი2"))
        self.label_6.setText(_translate("MainWindow", "გვერდი3"))
        self.pushButton_4.setText(_translate("MainWindow", "გამოთვლა"))
        self.label_7.setText(_translate("MainWindow", "ფართობი"))
        self.label_8.setText(_translate("MainWindow", "პერიმეტრი"))
        self.label_16.setText(_translate("MainWindow", ""))
        self.get_backbutton_3.setText(_translate("MainWindow", "უკან დაბრუნება"))
        self.label_9.setText(_translate("MainWindow", "გვერდი1"))
        self.label_10.setText(_translate("MainWindow", "გვერდი2"))
        self.label_11.setText(_translate("MainWindow", "ფართობი"))
        self.label_12.setText(_translate("MainWindow", "პერიმეტრი"))
        self.pushButton_5.setText(_translate("MainWindow", "გამოთვლა"))
        self.get_backbutton_4.setText(_translate("MainWindow", "უკან დაბრუნება"))
        self.label_13.setText(_translate("MainWindow", "გვერდი"))
        self.pushButton_6.setText(_translate("MainWindow", "გამოთვლა"))
        self.label_14.setText(_translate("MainWindow", "პერიმეტრი"))
        self.label_15.setText(_translate("MainWindow", "ფართობი"))

    def select_shape(self):
        if self.radioButton.isChecked():
            self.stackedWidget.setCurrentIndex(1)
        elif self.radioButton_3.isChecked():
            self.stackedWidget.setCurrentIndex(2)
        elif self.radioButton_2.isChecked():
            self.stackedWidget.setCurrentIndex(3)
        elif self.radioButton_4.isChecked():
            self.stackedWidget.setCurrentIndex(4)

    def get_back(self):
        self.stackedWidget.setCurrentIndex(0)

    def areaLength_circle(self):
        radius = float(self.doubleSpinBoxRadius.text())
        area = math.pi * radius ** 2
        self.lcdNumber.display(area)
        length = 2 * math.pi * radius
        self.lcdNumber_2.display(length)

    def areaPerimeter_triangle(self):
        try:
            side1 = float(self.doubleSpinBoxRadius_4.text())
            side2 = float(self.doubleSpinBoxRadius_3.text())
            side3 = float(self.doubleSpinBoxRadius_2.text())
            if (side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2:
                s = (side1 + side2 + side3) / 2
                area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
                self.lcdNumber_4.display(area)
                perimeter = side1 + side2 + side3
                self.lcdNumber_3.display(perimeter)
                self.label_16.setText("")
            else:
                self.label_16.setText("ასეთი სამკუთხედი არ არსებობს")
                self.label_16.adjustSize()
        except Exception:
            return None

    def areaPerimeter_rectangle(self):
        try:
            side1 = float(self.doubleSpinBoxRadius_6.text())
            side2 = float(self.doubleSpinBoxRadius_5.text())
            area = side1 * side2
            self.lcdNumber_5.display(area)
            perimeter = 2 * (side1 + side2)
            self.lcdNumber_6.display(perimeter)
        except Exception:
            return None

    def areaPerimeter_square(self):
        try:
            side = float(self.doubleSpinBoxRadius_7.text())
            area = side ** 2
            self.lcdNumber_8.display(area)
            perimeter = 4 * side
            self.lcdNumber_7.display(perimeter)
        except Exception:
            return None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
