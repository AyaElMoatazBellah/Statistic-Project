# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z_Score.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math
class Ui_Z_Score(object):
    def on_Add_click(self):
        textboxValue = self.Txt_Val.text()
        self.Txt_All_Values.setText(self.Txt_All_Values.text() + " " + textboxValue)

    def clear(self):
        self.Txt_Val.setText("")

    def calculate(self):
        list1 = []
        ungrouped_data = self.Txt_All_Values.text()
        list1 = ungrouped_data.split()
        list1.sort()

        sum1 = 0
        for num in list1:
            sum1 = sum1 + int(num)

        count_n = len(list1)
        men_val_1 = int(sum1) / count_n
        self.Lbl_Mean.setText(str(men_val_1))
        list1 = self.Txt_All_Values.text().split()

        result1 = 0
        for i in range(len(list1)):
            x = float(list1[i])
            result1 += math.pow((x - men_val_1), 2)
        stand1 = math.sqrt(result1 / (len(list1) - 1))
        self.Lbl_SD.setText(str(stand1))

        for i in range(len(list1)):
            x = float(list1[i])
            Z = "{:.1f}".format((x - men_val_1) / stand1)
            self.Lbl_Z_Score.setText((self.Lbl_Z_Score.text()) +"  "+ str(Z))

    def setupUi(self, Z_Score):
        Z_Score.setObjectName("Z_Score")
        Z_Score.resize(571, 252)
        self.label_6 = QtWidgets.QLabel(Z_Score)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(Z_Score)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Z_Score)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Lbl_SD = QtWidgets.QLabel(Z_Score)
        self.Lbl_SD.setGeometry(QtCore.QRect(200, 130, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_SD.setFont(font)
        self.Lbl_SD.setText("")
        self.Lbl_SD.setObjectName("Lbl_SD")
        self.Lbl_Mean = QtWidgets.QLabel(Z_Score)
        self.Lbl_Mean.setGeometry(QtCore.QRect(200, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Mean.setFont(font)
        self.Lbl_Mean.setText("")
        self.Lbl_Mean.setObjectName("Lbl_Mean")
        self.Lbl_Z_Score = QtWidgets.QLabel(Z_Score)
        self.Lbl_Z_Score.setGeometry(QtCore.QRect(200, 160, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Z_Score.setFont(font)
        self.Lbl_Z_Score.setText("")
        self.Lbl_Z_Score.setObjectName("Lbl_Z_Score")
        self.Txt_Val = QtWidgets.QLineEdit(Z_Score)
        self.Txt_Val.setGeometry(QtCore.QRect(180, 20, 41, 31))
        self.Txt_Val.setObjectName("Txt_Val")
        self.Btn_Add = QtWidgets.QPushButton(Z_Score)
        self.Btn_Add.setGeometry(QtCore.QRect(240, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add.setFont(font)
        self.Btn_Add.setObjectName("Btn_Add")
        self.Btn_Add.clicked.connect(self.on_Add_click)
        self.Btn_Add.clicked.connect(self.clear)
        self.Txt_All_Values = QtWidgets.QLineEdit(Z_Score)
        self.Txt_All_Values.setGeometry(QtCore.QRect(352, 70, 191, 81))
        self.Txt_All_Values.setObjectName("Txt_All_Values")
        self.label = QtWidgets.QLabel(Z_Score)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Z_Score)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Btn_Calc = QtWidgets.QPushButton(Z_Score)
        self.Btn_Calc.setGeometry(QtCore.QRect(340, 200, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Calc.setFont(font)
        self.Btn_Calc.setObjectName("Btn_Calc")
        self.Btn_Calc.clicked.connect(self.calculate)
        self.retranslateUi(Z_Score)
        QtCore.QMetaObject.connectSlotsByName(Z_Score)

    def retranslateUi(self, Z_Score):
        _translate = QtCore.QCoreApplication.translate
        Z_Score.setWindowTitle(_translate("Z_Score", "Z_Score"))
        self.label_6.setText(_translate("Z_Score", "Z_Score"))
        self.label_3.setText(_translate("Z_Score", "Mean"))
        self.label_4.setText(_translate("Z_Score", "Standard Deviation"))
        self.Btn_Add.setText(_translate("Z_Score", "Add"))
        self.label.setText(_translate("Z_Score", "Enter the Values"))
        self.label_2.setText(_translate("Z_Score", " The Entered Values"))
        self.Btn_Calc.setText(_translate("Z_Score", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Z_Score = QtWidgets.QDialog()
    ui = Ui_Z_Score()
    ui.setupUi(Z_Score)
    Z_Score.show()
    sys.exit(app.exec_())

