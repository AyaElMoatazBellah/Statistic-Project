# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Box_Plot.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Label
import math
#import numpy as np
#import matplotlib.pyplot as plt
class Ui_Box_plot(object):

    def on_Add_click(self):
        textboxValue = self.Txt_Val.text()
        self.Txt_All_Values.setText(self.Txt_All_Values.text() + " " + textboxValue )

    def clear(self):
        self.Txt_Val.setText("")


    def cal_boxplot(self):

        population = []
        v = self.Txt_All_Values.text()
        population = v.split()
        plt.boxplot(population)
        plt.title('Box Plot Graph')
        plt.legend()
        plt.show()

    def calculate_median(list2=[]):
        n = len(list2)
        if n % 2 != 0:
            new_n = int(n / 2)
            val = list2[new_n]
        elif n % 2 == 0:
            new_n = int(n / 2)
            val = (int(list2[new_n]) + int(list2[new_n - 1])) / 2
        return val


    def calc_IQR(self):

        List1 = []
        v = self.Txt_All_Values.text()
        list4 = v.split()
        list4.sort()

        n = len(list4)
        if n % 2 != 0:
            new_n = int(n / 2)
            val = list4[new_n]
        elif n % 2 == 0:
            new_n = int(n / 2)
            val = (int(list4[new_n]) + int(list4[new_n - 1])) / 2

        n = len(list4)
        min_va = min(list4)
        max_va = max(list4)
        # value of q2
        if n % 2 != 0:
            new_val = n / 2
            print(new_val)
            new_list = range(int(list4[0]), int(list4[math.ceil(new_val) - 1]))
            n = len(new_list)
            if n % 2 != 0:
                new_n = int(n / 2)
                val = new_list[new_n]
            elif n % 2 == 0:
                new_n = int(n / 2)
                val = (int(new_list[new_n]) + int(new_list[new_n - 1])) / 2
            q1 = val  # value of q1

            new_list1 = range(int(list4[math.ceil(new_val)]), int(list4[n - 1]) + 1)
            n = len(new_list1)
            if n % 2 != 0:
                new_n = int(n / 2)
                val = new_list1[new_n]
            elif n % 2 == 0:
                new_n = int(n / 2)
                print(new_n)
                val = (int(new_list1[new_n]) + int(new_list1[new_n - 1])) / 2
            q3 = val   # value of q3

        elif n % 2 == 0:
            new_val = n / 2
            new_list = range(int(list4[0]), int(list4[math.ceil(new_val)]))
            n = len(new_list)
            if n % 2 != 0:
                new_n = int(n / 2)
                val = new_list[new_n]
            elif n % 2 == 0:
                new_n = int(n / 2)
                val = (int(new_list[new_n]) + int(new_list[new_n - 1])) / 2

            q1 = val  # value of q1
            new_list1 = range(int(list4[math.ceil(new_val) - 1]), int(list4[n - 1]) + 1)
            n = len(new_list1)
            if n % 2 != 0:
                new_n = int(n / 2)
                val = new_list1[new_n]
            elif n % 2 == 0:
                new_n = int(n / 2)
                val = (int(new_list1[new_n]) + int(new_list1[new_n - 1])) / 2
            q3 = val  # value of q3

        IQR = q3 - q1
        outliers = np.arange(q1 - (1.5 * IQR), q3 + (1.5 * IQR))
        extreme_values = np.arange(q1 - (3 * IQR), q3 + (3 * IQR))
        self.Lbl_Max.setText( max_va)
        self.Lbl_Min.setText(min_va)
        self.Lbl_IQR.setText(IQR)
        self.Lbl_Q1.setText(q1)
        self.Lbl_Q2.setText(q2)
        self.Lbl_Q3.setText(q3)
        self.Lbl_Outliers.setText(outliers)
        self.Lbl_E_V.setText(extreme_values)


    def setupUi(self, Box_plot):
        Box_plot.setObjectName("Box_plot")
        Box_plot.resize(553, 370)
        self.label_5 = QtWidgets.QLabel(Box_plot)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Box_plot)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Box_plot)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Box_plot)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Box_plot)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Box_plot)
        self.label_8.setGeometry(QtCore.QRect(20, 240, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Box_plot)
        self.label_9.setGeometry(QtCore.QRect(20, 300, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Box_plot)
        self.label_10.setGeometry(QtCore.QRect(20, 330, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Btn_Calc = QtWidgets.QPushButton(Box_plot)
        self.Btn_Calc.setGeometry(QtCore.QRect(370, 210, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Calc.setFont(font)
        self.Btn_Calc.setObjectName("Btn_Calc")
        self.Btn_Calc.clicked.connect(self.calc_IQR)
        self.Btn_Calc.clicked.connect(self.calculate_median)
        self.label = QtWidgets.QLabel(Box_plot)
        self.label.setGeometry(QtCore.QRect(20, 40, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Txt_All_Values = QtWidgets.QLineEdit(Box_plot)
        self.Txt_All_Values.setGeometry(QtCore.QRect(352, 80, 191, 81))
        self.Txt_All_Values.setObjectName("Txt_All_Values")
        self.Txt_Val = QtWidgets.QLineEdit(Box_plot)
        self.Txt_Val.setGeometry(QtCore.QRect(180, 30, 41, 31))
        self.Txt_Val.setObjectName("Txt_Val")
        self.label_2 = QtWidgets.QLabel(Box_plot)
        self.label_2.setGeometry(QtCore.QRect(360, 50, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Btn_Add = QtWidgets.QPushButton(Box_plot)
        self.Btn_Add.setGeometry(QtCore.QRect(240, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add.setFont(font)
        self.Btn_Add.setObjectName("Btn_Add")
        self.Btn_Add.clicked.connect(self.on_Add_click)
        self.Btn_Add.clicked.connect(self.clear)
        self.Btn_ShowBoxPlot = QtWidgets.QPushButton(Box_plot)
        self.Btn_ShowBoxPlot.setGeometry(QtCore.QRect(320, 280, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_ShowBoxPlot.setFont(font)
        self.Btn_ShowBoxPlot.setObjectName("Btn_ShowBoxPlot")
        self.Btn_ShowBoxPlot.clicked.connect(self.cal_boxplot)
        self.Lbl_Max = QtWidgets.QLabel(Box_plot)
        self.Lbl_Max.setGeometry(QtCore.QRect(170, 150, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Max.setFont(font)
        self.Lbl_Max.setText("")
        self.Lbl_Max.setObjectName("Lbl_Max")
        self.Lbl_Min = QtWidgets.QLabel(Box_plot)
        self.Lbl_Min.setGeometry(QtCore.QRect(170, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Min.setFont(font)
        self.Lbl_Min.setText("")
        self.Lbl_Min.setObjectName("Lbl_Min")
        self.Lbl_Q1 = QtWidgets.QLabel(Box_plot)
        self.Lbl_Q1.setGeometry(QtCore.QRect(170, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Q1.setFont(font)
        self.Lbl_Q1.setText("")
        self.Lbl_Q1.setObjectName("Lbl_Q1")
        self.Lbl_Q3 = QtWidgets.QLabel(Box_plot)
        self.Lbl_Q3.setGeometry(QtCore.QRect(170, 240, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Q3.setFont(font)
        self.Lbl_Q3.setText("")
        self.Lbl_Q3.setObjectName("Lbl_Q3")
        self.Lbl_Q2 = QtWidgets.QLabel(Box_plot)
        self.Lbl_Q2.setGeometry(QtCore.QRect(170, 210, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Q2.setFont(font)
        self.Lbl_Q2.setText("")
        self.Lbl_Q2.setObjectName("Lbl_Q2")
        self.Lbl_E_V = QtWidgets.QLabel(Box_plot)
        self.Lbl_E_V.setGeometry(QtCore.QRect(170, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_E_V.setFont(font)
        self.Lbl_E_V.setText("")
        self.Lbl_E_V.setObjectName("Lbl_E_V")
        self.Lbl_IQR = QtWidgets.QLabel(Box_plot)
        self.Lbl_IQR.setGeometry(QtCore.QRect(170, 330, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_IQR.setFont(font)
        self.Lbl_IQR.setText("")
        self.Lbl_IQR.setObjectName("Lbl_IQR")
        self.Lbl_Outliers = QtWidgets.QLabel(Box_plot)
        self.Lbl_Outliers.setGeometry(QtCore.QRect(170, 300, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Outliers.setFont(font)
        self.Lbl_Outliers.setText("")
        self.Lbl_Outliers.setObjectName("Lbl_Outliers")

        self.retranslateUi(Box_plot)
        QtCore.QMetaObject.connectSlotsByName(Box_plot)

    def retranslateUi(self, Box_plot):
        _translate = QtCore.QCoreApplication.translate
        Box_plot.setWindowTitle(_translate("Box_plot", "Box Plot"))
        self.label_5.setText(_translate("Box_plot", "Q1"))
        self.label_3.setText(_translate("Box_plot", "Minimum Value"))
        self.label_4.setText(_translate("Box_plot", "Maxmium Value"))
        self.label_6.setText(_translate("Box_plot", "Q2"))
        self.label_7.setText(_translate("Box_plot", "Extrem Values"))
        self.label_8.setText(_translate("Box_plot", "Q3"))
        self.label_9.setText(_translate("Box_plot", "Outliers"))
        self.label_10.setText(_translate("Box_plot", "IQR"))
        self.Btn_Calc.setText(_translate("Box_plot", "Calculate"))
        self.label.setText(_translate("Box_plot", "Enter the Values"))
        self.label_2.setText(_translate("Box_plot", " The Entered Values"))
        self.Btn_Add.setText(_translate("Box_plot", "Add"))
        self.Btn_ShowBoxPlot.setText(_translate("Box_plot", "Show Box Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Box_plot = QtWidgets.QDialog()
    ui = Ui_Box_plot()
    ui.setupUi(Box_plot)
    Box_plot.show()
    sys.exit(app.exec_())

