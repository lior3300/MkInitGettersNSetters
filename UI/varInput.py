# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'varInput.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 300)
        MainWindow.setMinimumSize(QtCore.QSize(505, 300))
        MainWindow.setMaximumSize(QtCore.QSize(505, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox_gettersNsetters = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_gettersNsetters.setGeometry(QtCore.QRect(70, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_gettersNsetters.setFont(font)
        self.checkBox_gettersNsetters.setObjectName("checkBox_gettersNsetters")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(200, 190, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 501, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_varNames = QtWidgets.QHBoxLayout()
        self.horizontalLayout_varNames.setObjectName("horizontalLayout_varNames")
        self.label_varName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_varName.setFont(font)
        self.label_varName.setObjectName("label_varName")
        self.horizontalLayout_varNames.addWidget(self.label_varName)
        self.lineEdit_varName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_varName.setFont(font)
        self.lineEdit_varName.setObjectName("lineEdit_varName")
        self.horizontalLayout_varNames.addWidget(self.lineEdit_varName)
        self.checkBox_valPrivete = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_valPrivete.setFont(font)
        self.checkBox_valPrivete.setObjectName("checkBox_valPrivete")
        self.horizontalLayout_varNames.addWidget(self.checkBox_valPrivete)
        self.verticalLayout.addLayout(self.horizontalLayout_varNames)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_errorVarName = QtWidgets.QLabel(self.centralwidget)
        self.label_errorVarName.setGeometry(QtCore.QRect(110, 220, 291, 20))
        self.label_errorVarName.setObjectName("label_errorVarName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "makeInit"))
        self.checkBox_gettersNsetters.setText(_translate("MainWindow", " make getters/setters private"))
        self.pushButton_create.setText(_translate("MainWindow", "create"))
        self.label_varName.setText(_translate("MainWindow", "variable name:"))
        self.checkBox_valPrivete.setText(_translate("MainWindow", "private"))
        self.label_errorVarName.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
