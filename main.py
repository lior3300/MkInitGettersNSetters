# import pyperclip
# pyperclip.copy('The text to be copied to the clipboard.')
# spam = pyperclip.paste()

# from tkinter import Tk
# r = Tk()
# r.withdraw()
# r.clipboard_clear()
# r.clipboard_append('i can has clipboardz?')
# r.update() # now it stays on the clipboard after the window is closed
# r.destroy()

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