# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pie_Chart.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
class Ui_PieChart(object):
    def drawPieChart(self):
        slices = [2, 5, 7, 1]  # piechart
        activities = ['amani', 'asmaa', 'tasnem', 'afnan']
        colors = ['r', 'c', 'm', 'b']
        plt.pie(slices, labels=activities, colors=colors, startangle=180, shadow=True, explode=(0, 0, 0, 0.05),
                autopct='%1.1f%%')

        plt.title('piechart graph')
        plt.legend()
        plt.show()

    def setupUi(self, PieChart):
        PieChart.setObjectName("PieChart")
        PieChart.resize(551, 485)
        self.Btn_AddSlices = QtWidgets.QPushButton(PieChart)
        self.Btn_AddSlices.setGeometry(QtCore.QRect(210, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_AddSlices.setFont(font)
        self.Btn_AddSlices.setObjectName("Btn_AddSlices")
        self.label = QtWidgets.QLabel(PieChart)
        self.label.setGeometry(QtCore.QRect(10, 30, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Txt_AllSlicesValues = QtWidgets.QTextEdit(PieChart)
        self.Txt_AllSlicesValues.setGeometry(QtCore.QRect(323, 60, 211, 81))
        self.Txt_AllSlicesValues.setObjectName("Txt_AllSlicesValues")
        self.Txt_Silces = QtWidgets.QTextEdit(PieChart)
        self.Txt_Silces.setGeometry(QtCore.QRect(220, 20, 91, 31))
        self.Txt_Silces.setObjectName("Txt_Silces")
        self.Btn_AddSlicesName = QtWidgets.QPushButton(PieChart)
        self.Btn_AddSlicesName.setGeometry(QtCore.QRect(210, 200, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_AddSlicesName.setFont(font)
        self.Btn_AddSlicesName.setObjectName("Btn_AddSlicesName")
        self.label_2 = QtWidgets.QLabel(PieChart)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Txt_AllSlicesName = QtWidgets.QTextEdit(PieChart)
        self.Txt_AllSlicesName.setGeometry(QtCore.QRect(323, 200, 211, 81))
        self.Txt_AllSlicesName.setObjectName("Txt_AllSlicesName")
        self.Txt_SlicesNames = QtWidgets.QTextEdit(PieChart)
        self.Txt_SlicesNames.setGeometry(QtCore.QRect(220, 160, 91, 31))
        self.Txt_SlicesNames.setObjectName("Txt_SlicesNames")
        self.Btn_AddColors = QtWidgets.QPushButton(PieChart)
        self.Btn_AddColors.setGeometry(QtCore.QRect(210, 330, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_AddColors.setFont(font)
        self.Btn_AddColors.setObjectName("Btn_AddColors")
        self.label_3 = QtWidgets.QLabel(PieChart)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Txt_AllColors = QtWidgets.QTextEdit(PieChart)
        self.Txt_AllColors.setGeometry(QtCore.QRect(323, 330, 211, 81))
        self.Txt_AllColors.setObjectName("Txt_AllColors")
        self.Txt_Colors = QtWidgets.QTextEdit(PieChart)
        self.Txt_Colors.setGeometry(QtCore.QRect(220, 290, 91, 31))
        self.Txt_Colors.setObjectName("Txt_Colors")
        self.Btn_ShowBarChart = QtWidgets.QPushButton(PieChart)
        self.Btn_ShowBarChart.setGeometry(QtCore.QRect(100, 400, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_ShowBarChart.setFont(font)
        self.Btn_ShowBarChart.setObjectName("Btn_ShowBarChart")

        self.retranslateUi(PieChart)
        QtCore.QMetaObject.connectSlotsByName(PieChart)

    def retranslateUi(self, PieChart):
        _translate = QtCore.QCoreApplication.translate
        PieChart.setWindowTitle(_translate("PieChart", "Pie Chart"))
        self.Btn_AddSlices.setText(_translate("PieChart", "Add"))
        self.label.setText(_translate("PieChart", "Enter the Slices Values"))
        self.Btn_AddSlicesName.setText(_translate("PieChart", "Add"))
        self.label_2.setText(_translate("PieChart", "Enter the Slices Names"))
        self.Btn_AddColors.setText(_translate("PieChart", "Add"))
        self.label_3.setText(_translate("PieChart", "Enter the Colors"))
        self.Btn_ShowBarChart.setText(_translate("PieChart", "Show Pie Chart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PieChart = QtWidgets.QDialog()
    ui = Ui_PieChart()
    ui.setupUi(PieChart)
    PieChart.show()
    sys.exit(app.exec_())

