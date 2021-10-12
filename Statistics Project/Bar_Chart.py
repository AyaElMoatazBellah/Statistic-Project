# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bar_Chart.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
class Ui_BarChart(object):

    def DrawBarChart(self):

       x = [1, 2, 2, 3, 3, 4, 5, 6, 7]
       y = [2, 3, 3, 4, 4, 5, 6, 7, 8]
       x2 = [1, 2, 2, 3, 3, 4, 5, 6, 7]
       y2 = [2, 3, 3, 4, 4, 5, 6, 7, 8]
       plt.bar(x, y, label='Asmaa', color='r')  # bar chart x,y are list
       plt.bar(x2, y2, label='Amany', color='c')
       plt.xlabel('Amany')
       plt.ylabel('Asmaa')
       plt.title('barchart graph')
       plt.legend()
       plt.show()

    def setupUi(self, BarChart):
        BarChart.setObjectName("BarChart")
        BarChart.resize(554, 409)
        self.Btn_Add_X_Value = QtWidgets.QPushButton(BarChart)
        self.Btn_Add_X_Value.setGeometry(QtCore.QRect(217, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add_X_Value.setFont(font)
        self.Btn_Add_X_Value.setObjectName("Btn_Add_X_Value")
        self.label = QtWidgets.QLabel(BarChart)
        self.label.setGeometry(QtCore.QRect(17, 30, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Txt_Yaxis = QtWidgets.QTextEdit(BarChart)
        self.Txt_Yaxis.setGeometry(QtCore.QRect(227, 160, 91, 31))
        self.Txt_Yaxis.setObjectName("Txt_Yaxis")
        self.Btn_ShowHistogram = QtWidgets.QPushButton(BarChart)
        self.Btn_ShowHistogram.setGeometry(QtCore.QRect(107, 320, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_ShowHistogram.setFont(font)
        self.Btn_ShowHistogram.setObjectName("Btn_ShowHistogram")
        self.label_2 = QtWidgets.QLabel(BarChart)
        self.label_2.setGeometry(QtCore.QRect(17, 170, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Txt_Xaxis = QtWidgets.QTextEdit(BarChart)
        self.Txt_Xaxis.setGeometry(QtCore.QRect(227, 20, 91, 31))
        self.Txt_Xaxis.setObjectName("Txt_Xaxis")
        self.Btn_Add_Y_Value = QtWidgets.QPushButton(BarChart)
        self.Btn_Add_Y_Value.setGeometry(QtCore.QRect(217, 200, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add_Y_Value.setFont(font)
        self.Btn_Add_Y_Value.setObjectName("Btn_Add_Y_Value")
        self.Txt_All_Y_Values = QtWidgets.QTextEdit(BarChart)
        self.Txt_All_Y_Values.setGeometry(QtCore.QRect(330, 200, 211, 81))
        self.Txt_All_Y_Values.setObjectName("Txt_All_Y_Values")
        self.Txt_All_X_Values = QtWidgets.QTextEdit(BarChart)
        self.Txt_All_X_Values.setGeometry(QtCore.QRect(330, 60, 211, 81))
        self.Txt_All_X_Values.setObjectName("Txt_All_X_Values")

        self.retranslateUi(BarChart)
        QtCore.QMetaObject.connectSlotsByName(BarChart)

    def retranslateUi(self, BarChart):
        _translate = QtCore.QCoreApplication.translate
        BarChart.setWindowTitle(_translate("BarChart", "Bar Chart"))
        self.Btn_Add_X_Value.setText(_translate("BarChart", "Add"))
        self.label.setText(_translate("BarChart", "Enter the X-axis Values"))
        self.Btn_ShowHistogram.setText(_translate("BarChart", "Show Bar Chart"))
        self.label_2.setText(_translate("BarChart", "Enter the Y-axis Values"))
        self.Btn_Add_Y_Value.setText(_translate("BarChart", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BarChart = QtWidgets.QDialog()
    ui = Ui_BarChart()
    ui.setupUi(BarChart)
    BarChart.show()
    sys.exit(app.exec_())

