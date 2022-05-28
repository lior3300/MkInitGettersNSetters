import re
import mainWindow as mnwin
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def __init__(self,MainWindow,varNums,clipboard) -> None:
        self.varNums=varNums
        self.vars=set()
        self.clipBoard=clipboard
        self.MainWindow=MainWindow
        self.strRes=""

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(505, 280)
        self.MainWindow.setMinimumSize(QtCore.QSize(505, 280))
        self.MainWindow.setMaximumSize(QtCore.QSize(505, 280))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
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
        self.pushButton_create.setGeometry(QtCore.QRect(260, 190, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(120, 190, 113, 32))
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_create.clicked.connect(lambda:self.checkLineEdits())
        self.pushButton_back.clicked.connect(lambda:mnwin.Ui_MainWindow(self.MainWindow).startMain())

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

        #region OG components

        # self.horizontalLayout_varNames = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_varNames.setObjectName("horizontalLayout_varNames")

        # self.label_varName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_varName.setFont(font)
        # self.label_varName.setObjectName("label_varName")
        # self.label_varName.setText(_translate("MainWindow", "variable name:"))
        # self.horizontalLayout_varNames.addWidget(self.label_varName)

        # self.lineEdit_varName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.lineEdit_varName.setFont(font)
        # self.lineEdit_varName.setObjectName("lineEdit_varName")
        # self.horizontalLayout_varNames.addWidget(self.lineEdit_varName)

        # self.checkBox_valPrivete = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.checkBox_valPrivete.setFont(font)
        # self.checkBox_valPrivete.setObjectName("checkBox_valPrivete")
        # self.checkBox_valPrivete.setText(_translate("MainWindow", "private"))
        # self.horizontalLayout_varNames.addWidget(self.checkBox_valPrivete)

        #endregion

        #region activly creating the components
        for i in range(1,self.varNums+1):
            #create new horizontal layout
            self.horizontalLayout_varNames = QtWidgets.QHBoxLayout()
            self.horizontalLayout_varNames.setObjectName(f"horizontalLayout_varNames{i}")

            #add to the horizontal layout the lable
            self.label_varName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_varName.setFont(font)
            self.label_varName.setObjectName(f"label_varName{i}")
            self.label_varName.setText(f"variable No.{i} name:")
            self.horizontalLayout_varNames.addWidget(self.label_varName)

            #add to the horizontal layout the lineEdit
            self.lineEdit_varName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.lineEdit_varName.setFont(font)
            self.lineEdit_varName.setObjectName(f"lineEdit_varName{i}")
            self.horizontalLayout_varNames.addWidget(self.lineEdit_varName)

            #to the horizontal layout the checkBox
            self.checkBox_valPrivete = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.checkBox_valPrivete.setFont(font)
            self.checkBox_valPrivete.setObjectName(f"checkBox_valPrivete{i}")
            self.checkBox_valPrivete.setText("private")
            self.horizontalLayout_varNames.addWidget(self.checkBox_valPrivete)

            #add the the horizontal layout the main verticalLayout of the scrollArea
            self.verticalLayout.addLayout(self.horizontalLayout_varNames)
        #endregion
        
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_errorVarName = QtWidgets.QLabel(self.centralwidget)
        self.label_errorVarName.setGeometry(QtCore.QRect(20, 220, 470, 20))
        self.label_errorVarName.setObjectName("label_errorVarName")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 37))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "makeInit"))
        self.checkBox_gettersNsetters.setText(_translate("MainWindow", " make getters/setters private"))
        self.pushButton_create.setText(_translate("MainWindow", "create"))
        self.pushButton_back.setText(_translate("MainWindow", "back"))
        # self.label_errorVarName.hide(True)

    #loading the window
    def startVarInput(self):
        self.setupUi()
        self.MainWindow.show()

    #checks if all the variable names that given are lagel
    def checkLineEdits(self):
        self.vars=set()
        erroredNames=[]
        for i in range(1,self.varNums+1):
            txt=self.MainWindow.findChild(QtWidgets.QLineEdit, f"lineEdit_varName{i}").text()
            
            #region ~~regex pattern explained~~~
            #           start(^)
            #           take 0 or 1 underscore (_{0,1})
            #           any from a-z and A-Z ([a-zA-Z])
            #           take 1 or more (+)
            #           any from underscore and a-z and A-Z ([_a-zA-Z])
            #           0 or more (*)
            #           ends with those in [] ($)
            #endregion
            #
            regex="^([a-zA-Z])+[_a-zA-Z]*$"
            # this is if i want to let the user choose to use 1 underscore
            # choose pattern by if private was chosen, let to use _ at the begining of var name if not private
            # if self.MainWindow.findChild(QtWidgets.QCheckBox, f"checkBox_valPrivete{i}").isChecked():
            #     regex="^([a-zA-Z])+[_a-zA-Z]*$"
            # else:
            #     regex="^(_{0,1}[a-zA-Z])+[_a-zA-Z]*$"

            if not bool(re.match(regex,txt)):
                erroredNames+=[f"No.{i}"]
            else:
                self.vars.add(txt)
        
        if len(erroredNames)==0:
            self.label_errorVarName.setText("created, was inserted to your clipboard.")
            self.createInit()
        else:
            self.label_errorVarName.setText(f"variables with illigal names are: "+",".join(erroredNames))


    #creates the __init__
    def createInit(self):
        self.strRes+=f"    def __init__(self,{','.join(self.vars)}):\n"
        for var in self.vars:
                self.strRes+=f"        self.{var}={var}\n"    
        self.createSetGet()
    
    def createSetGet(self):
        #check if getters/setters were set to private
        if self.MainWindow.findChild(QtWidgets.QCheckBox, "checkBox_gettersNsetters").isChecked():
            isPrivateMethods="__"
        else:
            isPrivateMethods=""

        for i in range(1,len(self.vars)+1):
            txt=self.MainWindow.findChild(QtWidgets.QLineEdit, f"lineEdit_varName{i}").text()

            #create the setter
            setName=f"{isPrivateMethods}set{txt.capitalize()}"
            self.strRes+=f"\n    def {setName}(self,{txt}):\n"
            if self.MainWindow.findChild(QtWidgets.QCheckBox, f"checkBox_valPrivete{i}").isChecked():
                self.strRes+=f"        self.__{txt}={txt}\n"
            else:
                self.strRes+=f"        self.{txt.capitalize()}={txt}\n"

            #create the getter
            getName=f"{isPrivateMethods}get{txt.capitalize()}"
            self.strRes+=f"\n    def {getName}(self):\n"

            if self.MainWindow.findChild(QtWidgets.QCheckBox, f"checkBox_valPrivete{i}").isChecked():
                self.strRes+=f"        return self.__{txt}\n"
            else:
                self.strRes+=f"        return self.{txt.capitalize()}\n"
            
            #create the property
            self.strRes+=f"    {txt}=property({getName},{setName})\n"
            
            self.clipBoard.setText(self.strRes) #add to clipboard
        
