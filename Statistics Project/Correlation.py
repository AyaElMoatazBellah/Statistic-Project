# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Correlation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import math
class Ui_Correlation(object):
    def on_Add_X_click(self):
        textboxValue = self.Txt_Xaxis.text()
        self.Txt_All_X_Values.setText(self.Txt_All_X_Values.text() + " " + textboxValue)

    def on_Add_Y_click(self):
        textboxValue = self.Txt_Yaxis.text()
        self.Txt_All_Y_Values.setText(self.Txt_All_Y_Values.text() + " " + textboxValue)

    def clearX(self):
        self.Txt_Xaxis.setText("")

    def clearY(self):
        self.Txt_Yaxis.setText("")


    def calculate_mean(list1):
        list1 = []
        ungrouped_data = self.Txt_All_Values.text()
        list1 = ungrouped_data.split()
        list1.sort()

        sum1 = 0
        for num in list1:
            sum1 = sum1 + int(num)

        count_n = len(list1)
        men_val = int(sum1) / count_n
        return men_val

    def zscore(x, list):
        Z = (x - mean(list)) / stanDiv(list)
        return (Z)

    def correlation(self):
        list1=(self.Txt_All_X_Values.text()).split()
        list2=(self.Txt_All_Y_Values.text()).split()
###################################################
        list3 = []
        ungrouped_data = self.Txt_All_X_Values.text()
        list3 = ungrouped_data.split()
        list3.sort()
        sum1 = 0
        for num in list3:
            sum1 = sum1 + int(num)
        count_n = len(list3)
        men_val_1 = int(sum1) / count_n

##############################################3
        list4 = []
        ungrouped_data = self.Txt_All_Y_Values.text()
        list4 = ungrouped_data.split()
        list4.sort()
        sum1 = 0
        for num in list4:
            sum1 = sum1 + int(num)
        count_n = len(list4)
        men_val_2 = int(sum1) / count_n

 #########################################
        result1 = 0
        for i in range(len(list1)):
            x = float(list1[i])
            result1 += math.pow((x - men_val_1), 2)
        stand1 = math.sqrt(result1 / (len(list1) - 1))

 #############################################
        result2 = 0
        for i in range(len(list2)):
            x = float(list2[i])
            result2 += math.pow((x - men_val_2), 2)
        stand2 = math.sqrt(result2 / (len(list2) - 1))

##########################################################
        result = 0
        listt = [float(x) for x in list1]
        listtt = [float(x) for x in list2]
        for i in range(len(list1)):
            zx = ( listt[i] - men_val_1) / stand1
            zy= ( listtt[i] -   men_val_2) / stand2
            #zx =self.zscore(list1[i], list1)
            # zy =self.zscore(list2[i], list2)
            result += zx * zy
        corr = result / (len(list1) - 1)
        co = (float(corr) * float(corr))
        self.Lbl_C_Coff.setText(str(corr))
        #QMessageBox.question(self, 'PyQt5 message',"this means that"+str(co * 100)+ "% of the variation in Y can be described by X" ,QMessageBox.Yes , QMessageBox.No)
        self.Lbl_Coff_Det.setText(str(co))
        return corr





    def check(self):
        list1 = self.Txt_All_X_Values.text()
        list2 = self.Txt_All_Y_Values.text()
        corr = correlation()
        if corr == 1:
            QMessageBox.question(self, "Perfect Positive",QMessageBox.Ok, QMessageBox.Ok)
        elif corr == -1:
            QMessageBox.question(self, "Perfect Negative",QMessageBox.Ok, QMessageBox.Ok)
        elif 0.7 <= corr <= 0.9:
            QMessageBox.question(self, "Strong Positive",QMessageBox.Ok, QMessageBox.Ok)
        elif -0.7 >= corr >= -0.9:
            QMessageBox.question(self, "Strong Negative",QMessageBox.Ok, QMessageBox.Ok)
        elif 0.4 <= corr <= 0.6:
            QMessageBox.question(self, "Moderate Positive",QMessageBox.Ok, QMessageBox.Ok)
        elif -0.4 >= corr >= -0.6:
            QMessageBox.question(self, "Moderate Negative",QMessageBox.Ok, QMessageBox.Ok)
        elif .01 <= corr <= 0.3:
            QMessageBox.question(self, "Weak Positive",QMessageBox.Ok, QMessageBox.Ok)
        elif -0.1 >= corr >= -0.3:
            QMessageBox.question(self, "Weak Negative",QMessageBox.Ok, QMessageBox.Ok)

    def setupUi(self, Correlation):
        Correlation.setObjectName("Correlation")
        Correlation.resize(598, 401)
        self.Btn_Add_X_Value = QtWidgets.QPushButton(Correlation)
        self.Btn_Add_X_Value.setGeometry(QtCore.QRect(250, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add_X_Value.setFont(font)
        self.Btn_Add_X_Value.setObjectName("Btn_Add_X_Value")
        self.Btn_Add_X_Value.clicked.connect(self.on_Add_X_click)
        self.Btn_Add_X_Value.clicked.connect(self.clearX)
        self.label_2 = QtWidgets.QLabel(Correlation)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Correlation)
        self.label.setGeometry(QtCore.QRect(40, 30, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Btn_ShowHistogram = QtWidgets.QPushButton(Correlation)
        self.Btn_ShowHistogram.setGeometry(QtCore.QRect(400, 300, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_ShowHistogram.setFont(font)
        self.Btn_ShowHistogram.setObjectName("Btn_ShowHistogram")
        self.Btn_ShowHistogram.clicked.connect(self.correlation)
     #   self.Btn_ShowHistogram.clicked.connect(self.check)
        self.Btn_Add_Y_Value = QtWidgets.QPushButton(Correlation)
        self.Btn_Add_Y_Value.setGeometry(QtCore.QRect(250, 200, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add_Y_Value.setFont(font)
        self.Btn_Add_Y_Value.setObjectName("Btn_Add_Y_Value")
        self.Btn_Add_Y_Value.clicked.connect(self.on_Add_Y_click)
        self.Btn_Add_Y_Value.clicked.connect(self.clearY)
        self.label_3 = QtWidgets.QLabel(Correlation)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Correlation)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Lbl_C_Coff = QtWidgets.QLabel(Correlation)
        self.Lbl_C_Coff.setGeometry(QtCore.QRect(280, 300, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_C_Coff.setFont(font)
        self.Lbl_C_Coff.setText("")
        self.Lbl_C_Coff.setObjectName("Lbl_C_Coff")
        self.Lbl_Coff_Det = QtWidgets.QLabel(Correlation)
        self.Lbl_Coff_Det.setGeometry(QtCore.QRect(280, 330, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Coff_Det.setFont(font)
        self.Lbl_Coff_Det.setText("")
        self.Lbl_Coff_Det.setObjectName("Lbl_Coff_Det")
        self.Txt_Xaxis = QtWidgets.QLineEdit(Correlation)
        self.Txt_Xaxis.setGeometry(QtCore.QRect(250, 20, 61, 31))
        self.Txt_Xaxis.setObjectName("Txt_Xaxis")
        self.Txt_Yaxis = QtWidgets.QLineEdit(Correlation)
        self.Txt_Yaxis.setGeometry(QtCore.QRect(250, 160, 61, 31))
        self.Txt_Yaxis.setObjectName("Txt_Yaxis")
        self.Txt_All_X_Values = QtWidgets.QLineEdit(Correlation)
        self.Txt_All_X_Values.setGeometry(QtCore.QRect(350, 60, 211, 81))
        self.Txt_All_X_Values.setObjectName("Txt_All_X_Values")
        self.Txt_All_Y_Values = QtWidgets.QLineEdit(Correlation)
        self.Txt_All_Y_Values.setGeometry(QtCore.QRect(350, 200, 211, 81))
        self.Txt_All_Y_Values.setObjectName("Txt_All_Y_Values")

        self.retranslateUi(Correlation)
        QtCore.QMetaObject.connectSlotsByName(Correlation)

    def retranslateUi(self, Correlation):
        _translate = QtCore.QCoreApplication.translate
        Correlation.setWindowTitle(_translate("Correlation", "Correlation"))
        self.Btn_Add_X_Value.setText(_translate("Correlation", "Add"))
        self.label_2.setText(_translate("Correlation", "Enter the Y-axis Values"))
        self.label.setText(_translate("Correlation", "Enter the X-axis Values"))
        self.Btn_ShowHistogram.setText(_translate("Correlation", "Calculate"))
        self.Btn_Add_Y_Value.setText(_translate("Correlation", "Add"))
        self.label_3.setText(_translate("Correlation", "Correlation Coffecient"))
        self.label_4.setText(_translate("Correlation", "Coffecient of Determination"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Correlation = QtWidgets.QDialog()
    ui = Ui_Correlation()
    ui.setupUi(Correlation)
    Correlation.show()
    sys.exit(app.exec_())

