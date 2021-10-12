# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Population_Mean.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_PopulationMean(object):

    def check(self):
        size = self.Txt_Size.text()
        sd = self.Txt_Sd.text()
        Avg=self.Txt_Avg.text()
        ci=self.Txt_C_I.text()
        a = float("{0:.3f}".format((100 - int(ci)) / 200))
        workbook = xlrd.open_workbook("z_score_excel.xls")
        worksheet = workbook.sheet_by_name("Sheet2")
        total_row = worksheet.nrows
        total_col = worksheet.ncols
        for i in range(1, total_row):
            for x in range(1, total_col):
                excel_date3 = worksheet.cell(i, x).value
                if excel_date3 == a:
                    zx = abs(float("{0:.4f}".format(worksheet.cell(i, 0).value)))
                    zy = float("{0:.4f}".format(worksheet.cell(0, x).value))
                    z = zy + zx
                    m1 = Avg + z * sd / math.sqrt(size)
                    m2 = Avg - z * sd / math.sqrt(size)
                    self.Lbl_SD.setText(str(m1) + " < " + "Population Mean" +" < " + str(m2)  )
                    return 0

        for i in range(1, total_row):
            for x in range(1, total_col):
                excel_date3 = worksheet.cell(i, x).value
                if excel_date3 > a:
                    for y in range(x, total_col):
                        excel_date4 = worksheet.cell(i, y).value
                        if excel_date4 < a:
                            if (a - worksheet.cell(i, y).value) < (worksheet.cell(i, y - 1).value - a):
                                maxx = worksheet.cell(i, y).value
                            else:
                                maxx = worksheet.cell(i, y - 1).value
                                y = y - 1

                            zx = abs(float("{0:.4f}".format(worksheet.cell(i, 0).value)))
                            zy = float("{0:.4f}".format(worksheet.cell(0, y).value))
                            z = zy + zx
                            m1 = Avg + z * sd / math.sqrt(size)
                            m2 = Avg - z * sd / math.sqrt(size)
                            self.Lbl_SD.setText(str(m1) + " < " + "Population Mean" + " < " + str(m2))
                            return 0

    def setupUi(self, PopulationMean):
        PopulationMean.setObjectName("PopulationMean")
        PopulationMean.resize(570, 304)
        self.label_3 = QtWidgets.QLabel(PopulationMean)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(PopulationMean)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(PopulationMean)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(PopulationMean)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Btn_Calc = QtWidgets.QPushButton(PopulationMean)
        self.Btn_Calc.setGeometry(QtCore.QRect(340, 90, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Calc.setFont(font)
        self.Btn_Calc.setObjectName("Btn_Calc")
        self.Btn_Calc.clicked.connect(self.check)
        self.Txt_Size = QtWidgets.QLineEdit(PopulationMean)
        self.Txt_Size.setGeometry(QtCore.QRect(200, 40, 51, 21))
        self.Txt_Size.setObjectName("Txt_Size")
        self.Lbl_Average = QtWidgets.QLabel(PopulationMean)
        self.Lbl_Average.setGeometry(QtCore.QRect(190, 160, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Average.setFont(font)
        self.Lbl_Average.setText("")
        self.Lbl_Average.setObjectName("Lbl_Average")
        self.Lbl_C_I = QtWidgets.QLabel(PopulationMean)
        self.Lbl_C_I.setGeometry(QtCore.QRect(190, 190, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_C_I.setFont(font)
        self.Lbl_C_I.setText("")
        self.Lbl_C_I.setObjectName("Lbl_C_I")
        self.Lbl_Size = QtWidgets.QLabel(PopulationMean)
        self.Lbl_Size.setGeometry(QtCore.QRect(190, 130, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_Size.setFont(font)
        self.Lbl_Size.setText("")
        self.Lbl_Size.setObjectName("Lbl_Size")
        self.Lbl_SD = QtWidgets.QLabel(PopulationMean)
        self.Lbl_SD.setGeometry(QtCore.QRect(200, 210, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lbl_SD.setFont(font)
        self.Lbl_SD.setText("")
        self.Lbl_SD.setObjectName("Lbl_SD")
        self.Txt_Avg = QtWidgets.QLineEdit(PopulationMean)
        self.Txt_Avg.setGeometry(QtCore.QRect(200, 70, 51, 21))
        self.Txt_Avg.setObjectName("Txt_Avg")
        self.Txt_Sd = QtWidgets.QLineEdit(PopulationMean)
        self.Txt_Sd.setGeometry(QtCore.QRect(200, 100, 51, 21))
        self.Txt_Sd.setObjectName("Txt_Sd")
        self.Txt_C_I = QtWidgets.QLineEdit(PopulationMean)
        self.Txt_C_I.setGeometry(QtCore.QRect(200, 130, 51, 21))
        self.Txt_C_I.setObjectName("Txt_C_I")
        self.label_7 = QtWidgets.QLabel(PopulationMean)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(PopulationMean)
        QtCore.QMetaObject.connectSlotsByName(PopulationMean)

    def retranslateUi(self, PopulationMean):
        _translate = QtCore.QCoreApplication.translate
        PopulationMean.setWindowTitle(_translate("PopulationMean", "Population Mean"))
        self.label_3.setText(_translate("PopulationMean", "Size"))
        self.label_6.setText(_translate("PopulationMean", "Standard Deviation"))
        self.label_5.setText(_translate("PopulationMean", "Confidence Interval"))
        self.label_4.setText(_translate("PopulationMean", "Average "))
        self.Btn_Calc.setText(_translate("PopulationMean", "Calculate"))
        self.label_7.setText(_translate("PopulationMean", "Population Interval :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopulationMean = QtWidgets.QDialog()
    ui = Ui_PopulationMean()
    ui.setupUi(PopulationMean)
    PopulationMean.show()
    sys.exit(app.exec_())

