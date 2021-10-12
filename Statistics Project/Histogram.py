# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Histogram.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
class Ui_Histogram(object):
    def drawhistogram(self):

       population_ages = [1, 15, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70]  # histogram
       bins = [1, 5, 3, 4, 5, 6, 7]
       cols = ['r', 'c']
       plt.hist(population_ages, bins, histtype='bar', rwidth=0.9)
       plt.title('Histogram graph')
       plt.legend()
       plt.show()


    def setupUi(self, Histogram):
        Histogram.setObjectName("Histogram")
        Histogram.resize(545, 426)
        self.Btn_Add_Y_Value = QtWidgets.QPushButton(Histogram)
        self.Btn_Add_Y_Value.setGeometry(QtCore.QRect(210, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add_Y_Value.setFont(font)
        self.Btn_Add_Y_Value.setObjectName("Btn_Add_Y_Value")
        self.Txt_All_X_Values = QtWidgets.QTextEdit(Histogram)
        self.Txt_All_X_Values.setGeometry(QtCore.QRect(323, 70, 211, 81))
        self.Txt_All_X_Values.setObjectName("Txt_All_X_Values")
        self.Txt_Xaxis = QtWidgets.QTextEdit(Histogram)
        self.Txt_Xaxis.setGeometry(QtCore.QRect(220, 30, 91, 31))
        self.Txt_Xaxis.setObjectName("Txt_Xaxis")
        self.label_2 = QtWidgets.QLabel(Histogram)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Histogram)
        self.label.setGeometry(QtCore.QRect(10, 40, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Txt_Yaxis = QtWidgets.QTextEdit(Histogram)
        self.Txt_Yaxis.setGeometry(QtCore.QRect(220, 170, 91, 31))
        self.Txt_Yaxis.setObjectName("Txt_Yaxis")
        self.Txt_All_Y_Values = QtWidgets.QTextEdit(Histogram)
        self.Txt_All_Y_Values.setGeometry(QtCore.QRect(323, 210, 211, 81))
        self.Txt_All_Y_Values.setObjectName("Txt_All_Y_Values")
        self.Btn_Add_X_Value = QtWidgets.QPushButton(Histogram)
        self.Btn_Add_X_Value.setGeometry(QtCore.QRect(210, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Add_X_Value.setFont(font)
        self.Btn_Add_X_Value.setObjectName("Btn_Add_X_Value")
        self.Btn_ShowHistogram = QtWidgets.QPushButton(Histogram)
        self.Btn_ShowHistogram.setGeometry(QtCore.QRect(100, 330, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_ShowHistogram.setFont(font)
        self.Btn_ShowHistogram.setObjectName("Btn_ShowHistogram")

        self.retranslateUi(Histogram)
        QtCore.QMetaObject.connectSlotsByName(Histogram)

    def retranslateUi(self, Histogram):
        _translate = QtCore.QCoreApplication.translate
        Histogram.setWindowTitle(_translate("Histogram", "Histogram"))
        self.Btn_Add_Y_Value.setText(_translate("Histogram", "Add"))
        self.label_2.setText(_translate("Histogram", "Enter the Y-axis Values"))
        self.label.setText(_translate("Histogram", "Enter the X-axis Values"))
        self.Btn_Add_X_Value.setText(_translate("Histogram", "Add"))
        self.Btn_ShowHistogram.setText(_translate("Histogram", "Show Histogram"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Histogram = QtWidgets.QDialog()
    ui = Ui_Histogram()
    ui.setupUi(Histogram)
    Histogram.show()
    sys.exit(app.exec_())

