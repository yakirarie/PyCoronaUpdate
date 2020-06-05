# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'corona.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(333, 504)
        Dialog.setStyleSheet("\n"
"QWidget {\n"
"    background-color:rgb(0, 0, 0);\n"
"    color: rgb(240, 240, 240);\n"
"    border-color: rgb(58, 58, 58);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color:rgb(0, 0, 0);\n"
"    color: rgb(200, 200, 200);\n"
"    selection-background-color: rgb(255, 153, 0);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"        border-top: 1px solid #000000;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"     background-color:rgb(0, 0, 0);\n"
"     border-style: outset;\n"
"    border-width: 1px;\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-top-width: 0px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 153, 0);\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"   color: rgb(255, 255, 255);\n"
"   background-color:rgb(0, 0, 0);\n"
"   border-color:rgb(42, 42, 42);\n"
"   margin-left: 0px;\n"
"   margin-right: 0px;\n"
"   border-bottom-right-radius:4px;\n"
"   border-bottom-left-radius:4px;\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"  background-color:rgb(0, 0, 0);\n"
"    border-color:rgb(42, 42, 42);\n"
"    margin-left: 0px;\n"
"      margin-right: 0px;\n"
"    border-bottom-right-radius:4px;\n"
"    border-bottom-left-radius:4px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"   margin-bottom: 4px;\n"
"   border-bottom-right-radius:4px;\n"
"   border-bottom-left-radius:4px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-bottom-color: rgb(115, 115, 115);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(0, 0, 0);\n"
"    padding: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: rgb(255, 255, 255);\n"
"    background:rgb(101, 101, 101);\n"
"    selection-background-color: rgb(187, 187, 187);\n"
"    selection-color: rgb(60, 63, 65);\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(0, 200, 0, 255), stop:1 rgba(30, 230, 30, 255));\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background:rgb(0, 0, 0);\n"
"    color: rgb(255, 153, 0);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"      spacing: 3px; \n"
"    padding: 1px 4px;\n"
"      background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected { \n"
"      background:rgb(115, 115, 115);\n"
"}\n"
"\n"
"QMenu {\n"
"    border-width: 2px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(255, 153, 0);\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    spacing: 3px; \n"
"    padding: 3px 15px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    spacing: 3px; \n"
"    padding: 3px 15px;\n"
"    background:rgb(115, 115, 115);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QLabel, QComboBox{\n"
"    font-size: 26px;\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QLCDNumber{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.total_confirmed_num = QtWidgets.QLCDNumber(Dialog)
        self.total_confirmed_num.setDigitCount(9)
        self.total_confirmed_num.setObjectName("total_confirmed_num")
        self.gridLayout.addWidget(self.total_confirmed_num, 0, 1, 1, 1)
        self.total_deaths_num = QtWidgets.QLCDNumber(Dialog)
        self.total_deaths_num.setDigitCount(9)
        self.total_deaths_num.setObjectName("total_deaths_num")
        self.gridLayout.addWidget(self.total_deaths_num, 1, 1, 1, 1)
        self.total_deaths = QtWidgets.QLabel(Dialog)
        self.total_deaths.setObjectName("total_deaths")
        self.gridLayout.addWidget(self.total_deaths, 1, 0, 1, 1)
        self.total_recovered = QtWidgets.QLabel(Dialog)
        self.total_recovered.setObjectName("total_recovered")
        self.gridLayout.addWidget(self.total_recovered, 3, 0, 1, 1)
        self.total_confirmed = QtWidgets.QLabel(Dialog)
        self.total_confirmed.setObjectName("total_confirmed")
        self.gridLayout.addWidget(self.total_confirmed, 0, 0, 1, 1)
        self.total_recovered_num = QtWidgets.QLCDNumber(Dialog)
        self.total_recovered_num.setDigitCount(9)
        self.total_recovered_num.setObjectName("total_recovered_num")
        self.gridLayout.addWidget(self.total_recovered_num, 3, 1, 1, 1)
        self.total_active = QtWidgets.QLabel(Dialog)
        self.total_active.setObjectName("total_active")
        self.gridLayout.addWidget(self.total_active, 4, 0, 1, 1)
        self.total_active_num = QtWidgets.QLCDNumber(Dialog)
        self.total_active_num.setDigitCount(9)
        self.total_active_num.setObjectName("total_active_num")
        self.gridLayout.addWidget(self.total_active_num, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.confirmed_button = QtWidgets.QPushButton(Dialog)
        self.confirmed_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.confirmed_button.setObjectName("confirmed_button")
        self.horizontalLayout_2.addWidget(self.confirmed_button)
        self.deaths_button = QtWidgets.QPushButton(Dialog)
        self.deaths_button.setObjectName("deaths_button")
        self.horizontalLayout_2.addWidget(self.deaths_button)
        self.recovered_button = QtWidgets.QPushButton(Dialog)
        self.recovered_button.setObjectName("recovered_button")
        self.horizontalLayout_2.addWidget(self.recovered_button)
        self.active_button = QtWidgets.QPushButton(Dialog)
        self.active_button.setObjectName("active_button")
        self.horizontalLayout_2.addWidget(self.active_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.graphicsView = QChartView(Dialog)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QtCorona"))
        self.title.setText(_translate("Dialog", "Global Corona Status"))
        self.total_deaths.setText(_translate("Dialog", "Total Deaths"))
        self.total_recovered.setText(_translate("Dialog", "Total Recovered"))
        self.total_confirmed.setText(_translate("Dialog", "Total Confirmed"))
        self.total_active.setText(_translate("Dialog", "Total Active"))
        self.confirmed_button.setText(_translate("Dialog", "Confirmed"))
        self.deaths_button.setText(_translate("Dialog", "Deaths"))
        self.recovered_button.setText(_translate("Dialog", "Recovered"))
        self.active_button.setText(_translate("Dialog", "Actives"))
from PyQt5.QtChart import QChartView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
