# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Regression.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  math
class Ui_Regression(object):
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

    def simpleregression(self):
        list1 = (self.Txt_All_X_Values.text()).split()
        list2 = (self.Txt_All_Y_Values.text()).split()
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
            zx = (listt[i] - men_val_1) / stand1
            zy = (listtt[i] - men_val_2) / stand2
            result += zx * zy
        corr = result / (len(list1) - 1)

        b1 = corr * (stand2 / stand1)
        b0 = men_val_2 - b1 * men_val_1
        self.Lbl_S_Reg.setText("Y="+str( "{:.4f}".format(b0))+"+X("+str( "{:.1f}".format(b1))+")")

    def setupUi(self, Regression):
        Regression.setObjectName("Regression")
        Regression.resize(591, 403)
        self.label_3 = QtWidgets.QLabel(Regression)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Regression)
        self.label.setGeometry(QtCore.QRect(40, 30, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Txt_Yaxis = QtWidgets.QLineEdit(Regression)
        self.Txt_Yaxis.setGeometry(QtCore.QRect(250, 160, 61, 31))
        self.Txt_Yaxis.setObjectName("Txt_Yaxis")
        self.Txt_All_X_Values = QtWidgets.QLineEdit(Regression)
        self.Txt_All_X_Values.setGeometry(QtCore.QRect(350, 60, 211, 81))
        self.Txt_All_X_Values.setObjectName("Txt_All_X_Values")
        self.Btn_Add_Y_Value = QtWidgets.QPushButton(Regression)
        self.Btn_Add_Y_Value.setGeometry(QtCore.QRect(250, 200, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add_Y_Value.setFont(font)
        self.Btn_Add_Y_Value.setObjectName("Btn_Add_Y_Value")
        self.Btn_Add_Y_Value.clicked.connect(self.on_Add_Y_click)
        self.Btn_Add_Y_Value.clicked.connect(self.clearY)
        self.Btn_Calc = QtWidgets.QPushButton(Regression)
        self.Btn_Calc.setGeometry(QtCore.QRect(450, 300, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Calc.setFont(font)
        self.Btn_Calc.setObjectName("Btn_Calc")
        self.Btn_Calc.clicked.connect(self.simpleregression)
        self.Txt_All_Y_Values = QtWidgets.QLineEdit(Regression)
        self.Txt_All_Y_Values.setGeometry(QtCore.QRect(350, 200, 211, 81))
        self.Txt_All_Y_Values.setObjectName("Txt_All_Y_Values")
        self.Btn_Add_X_Value = QtWidgets.QPushButton(Regression)
        self.Btn_Add_X_Value.setGeometry(QtCore.QRect(250, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add_X_Value.setFont(font)
        self.Btn_Add_X_Value.setObjectName("Btn_Add_X_Value")
        self.Btn_Add_X_Value.clicked.connect(self.on_Add_X_click)
        self.Btn_Add_X_Value.clicked.connect(self.clearX)
        self.label_2 = QtWidgets.QLabel(Regression)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Txt_Xaxis = QtWidgets.QLineEdit(Regression)
        self.Txt_Xaxis.setGeometry(QtCore.QRect(250, 20, 61, 31))
        self.Txt_Xaxis.setObjectName("Txt_Xaxis")
        self.Lbl_S_Reg = QtWidgets.QLabel(Regression)
        self.Lbl_S_Reg.setGeometry(QtCore.QRect(170, 290, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_S_Reg.setFont(font)
        self.Lbl_S_Reg.setText("")
        self.Lbl_S_Reg.setObjectName("Lbl_S_Reg")

        self.retranslateUi(Regression)
        QtCore.QMetaObject.connectSlotsByName(Regression)

    def retranslateUi(self, Regression):
        _translate = QtCore.QCoreApplication.translate
        Regression.setWindowTitle(_translate("Regression", "Regression"))
        self.label_3.setText(_translate("Regression", "Sample Regression"))
        self.label.setText(_translate("Regression", "Enter the X-axis Values"))
        self.Btn_Add_Y_Value.setText(_translate("Regression", "Add"))
        self.Btn_Calc.setText(_translate("Regression", "Calculate"))
        self.Btn_Add_X_Value.setText(_translate("Regression", "Add"))
        self.label_2.setText(_translate("Regression", "Enter the Y-axis Values"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Regression = QtWidgets.QDialog()
    ui = Ui_Regression()
    ui.setupUi(Regression)
    Regression.show()
    sys.exit(app.exec_())

