import sys
from PyQt5 import QtWidgets
import mainWindow as mnwin

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    clipboard=app.clipboard()
    ui = mnwin.Ui_MainWindow(QtWidgets.QMainWindow(),clipboard)
    ui.startMain()
    
    # ui.setupUi()
    # MainWindow.show()
    sys.exit(app.exec_())