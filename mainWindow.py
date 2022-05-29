from PyQt5 import QtCore, QtGui, QtWidgets
import varInput as vrnpt


class Ui_MainWindow(object):

    def __init__(self,MainWindow,clipboard) -> None:
        self.clipBoard=clipboard
        self.MainWindow=MainWindow

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(450, 250)
        self.MainWindow.setMinimumSize(QtCore.QSize(450, 250))
        self.MainWindow.setMaximumSize(QtCore.QSize(450, 250))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        self.MainWindow.setMinimumSize(QtCore.QSize(450, 250))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.checkBox_Inheritance = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Inheritance.setGeometry(QtCore.QRect(40, 50, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Inheritance.setFont(font)
        self.checkBox_Inheritance.setObjectName("checkBox_Inheritance")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(180, 160, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start.setObjectName("pushButton_start")

        self.pushButton_start.clicked.connect(lambda:self.openVarInputWindow())

        self.lineEdit_varNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_varNum.setGeometry(QtCore.QRect(310, 100, 50, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_varNum.setFont(font)
        self.lineEdit_varNum.setObjectName("lineEdit_varNum")
        self.label_valNum = QtWidgets.QLabel(self.centralwidget)
        self.label_valNum.setGeometry(QtCore.QRect(30, 110, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_valNum.setFont(font)
        self.label_valNum.setObjectName("label_valNum")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(60, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 37))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "initMaker"))
        self.pushButton_start.setText(_translate("MainWindow", "start"))
        self.label_valNum.setText(_translate("MainWindow", "how many variables?"))
        self.checkBox_Inheritance.setText(_translate("MainWindow", " does the class inherent from other class?"))
        self.lineEdit_varNum.setText("1")
        self.label_info.setText(_translate("MainWindow", "This program creates an __init__ function and\n"
                                "properties for the variables."))
        

    def openVarInputWindow(self):
        if self.lineEdit_varNum.text().isdigit() and int(self.lineEdit_varNum.text())>0:
            ui=vrnpt.Ui_MainWindow(self.MainWindow,
            int(self.lineEdit_varNum.text()),
            self.clipBoard,
            self.checkBox_Inheritance.isChecked())
            ui.startVarInput()
        else:
            self.label_info.setStyleSheet("background-color: #ff4a57")
            self.label_info.setText("variable number must be an int\nand bigger then 0")

    def startMain(self):
        self.setupUi()
        self.MainWindow.show()