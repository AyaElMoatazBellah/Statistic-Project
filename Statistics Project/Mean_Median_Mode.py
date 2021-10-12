# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mean_Median_Mode.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import math
class Ui_Mean_Median_Mode(object):

    def on_Add_click(self):
        textboxValue = self.Txt_Val.text()
        self.Txt_All_Values.setText(self.Txt_All_Values.text() + " " + textboxValue )

    def clear(self):
        self.Txt_Val.setText("")

    def calculate_mean(self):
        list1 = []
        ungrouped_data = self.Txt_All_Values.text()
        list1 = ungrouped_data.split()
        list1.sort()

        sum1=0
        for num in list1:
             sum1 = sum1+int(num)

        count_n = len(list1)
        men_val = int(sum1) / count_n
        self.Lbl_Mean.setText(str(men_val))



    def calculate_median(self):

        list1 = []
        ungrouped_data = self.Txt_All_Values.text()
        list1 = ungrouped_data.split()
        list1.sort()
        n = len(list1)
        if n % 2 != 0:
            new_n = int(n / 2)
            valueee=list1[new_n]
            self.Lbl_Median.setText(str(valueee))


        elif n % 2 == 0:
            new_n = int(n / 2)
            valuee = (int(list1[new_n]) + int(list1[new_n - 1])) / 2
            self.Lbl_Median.setText(str(valuee))

    def calculate_mode(self):
        list1 = []
        ungrouped_data = self.Txt_All_Values.text()
        list1 = ungrouped_data.split()
        list1.sort()
        counter = 0
        num = list1[0]

        for i in list1:
            curr_frequency = list1.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                num = i
        self.Lbl_Mode.setText(str(num))



    def setupUi(self, Mean_Median_Mode):
        Mean_Median_Mode.setObjectName("Mean_Median_Mode")
        Mean_Median_Mode.resize(575, 276)
        self.centralwidget = QtWidgets.QWidget(Mean_Median_Mode)
        self.centralwidget.setObjectName("centralwidget")
        self.Btn_Add = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Add.setGeometry(QtCore.QRect(240, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add.setFont(font)
        self.Btn_Add.setObjectName("Btn_Add")
        self.Btn_Add.clicked.connect(self.on_Add_click)
        self.Btn_Add.clicked.connect(self.clear)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 40, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Btn_Calc = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Calc.setGeometry(QtCore.QRect(240, 190, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Calc.setFont(font)
        self.Btn_Calc.setObjectName("Btn_Calc")
        self.Btn_Calc.clicked.connect(self.calculate_median)
        self.Btn_Calc.clicked.connect(self.calculate_mode)
        self.Btn_Calc.clicked.connect(self.calculate_mean)
        self.Txt_Val = QtWidgets.QLineEdit(self.centralwidget)
        self.Txt_Val.setGeometry(QtCore.QRect(180, 30, 41, 31))
        self.Txt_Val.setObjectName("Txt_Val")
        self.Txt_All_Values = QtWidgets.QLineEdit(self.centralwidget)
        self.Txt_All_Values.setGeometry(QtCore.QRect(352, 80, 191, 81))
        self.Txt_All_Values.setObjectName("Txt_All_Values")
        self.Lbl_Mean = QtWidgets.QLabel(self.centralwidget)
        self.Lbl_Mean.setGeometry(QtCore.QRect(110, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Mean.setFont(font)
        self.Lbl_Mean.setObjectName("Lbl_Mean")
        self.Lbl_Median = QtWidgets.QLabel(self.centralwidget)
        self.Lbl_Median.setGeometry(QtCore.QRect(110, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Median.setFont(font)
        self.Lbl_Median.setObjectName("Lbl_Median")
        self.Lbl_Mode = QtWidgets.QLabel(self.centralwidget)
        self.Lbl_Mode.setGeometry(QtCore.QRect(110, 190, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Mode.setFont(font)
        self.Lbl_Mode.setObjectName("Lbl_Mode")
        Mean_Median_Mode.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Mean_Median_Mode)
        self.statusbar.setObjectName("statusbar")
        Mean_Median_Mode.setStatusBar(self.statusbar)

        self.retranslateUi(Mean_Median_Mode)
        QtCore.QMetaObject.connectSlotsByName(Mean_Median_Mode)

    def retranslateUi(self, Mean_Median_Mode):
        _translate = QtCore.QCoreApplication.translate
        Mean_Median_Mode.setWindowTitle(_translate("Mean_Median_Mode", " Mean_Median_Mode"))
        self.Btn_Add.setText(_translate("Mean_Median_Mode", "Add"))
        self.label_5.setText(_translate("Mean_Median_Mode", "Mode"))
        self.label_3.setText(_translate("Mean_Median_Mode", "Mean"))
        self.label_2.setText(_translate("Mean_Median_Mode", " The Entered Values"))
        self.label_4.setText(_translate("Mean_Median_Mode", "Median"))
        self.label.setText(_translate("Mean_Median_Mode", "Enter the Values"))
        self.Btn_Calc.setText(_translate("Mean_Median_Mode", "Calculate"))
        self.Lbl_Mean.setText(_translate("Mean_Median_Mode", "TextLabel"))
        self.Lbl_Median.setText(_translate("Mean_Median_Mode", "TextLabel"))
        self.Lbl_Mode.setText(_translate("Mean_Median_Mode", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mean_Median_Mode = QtWidgets.QMainWindow()
    ui = Ui_Mean_Median_Mode()
    ui.setupUi(Mean_Median_Mode)
    Mean_Median_Mode.show()
    sys.exit(app.exec_())

