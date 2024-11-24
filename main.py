from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import sys
import ui_manager as UIM
"""
Requirement
-----------
1) install python 
2) install pip
3) install intel hex lib 
"""

def ConnectUiWithEvent(ui):
    UIM.button_interface(ui)
    pass
  
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # Store the ui reference

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = MyMainWindow(ui)
    ui.setupUi(MainWindow)
    ConnectUiWithEvent(ui)
    #page.list_com_ports()
    MainWindow.show()
    sys.exit(app.exec_())
