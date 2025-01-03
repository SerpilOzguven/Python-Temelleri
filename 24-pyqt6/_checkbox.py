import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from  _checkboxForm import Ui_MainWindow


class myApp (QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitapOkumak.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)
        
        self.ui.btnHobilerSecilenleriAl.clicked.connect(self.getAllHobiler)
        self.ui.btnDerslerSecilenleriAl.clicked.connect(self.getAllDersler)
        
    def getAllHobiler(self):
        result = ''
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
               result += cb.text() + '\n'
               
        self.ui.lblResultHobiler.setText(result)
        
    def getAllDersler(self):
        result = ''
        items = self.ui.groupDersler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
               result += cb.text() + '\n'
               
        self.ui.lblResultDersler.setText(result)
        
        
        
    def show_state(self,value):
        cb = self.sender()
        print(cb.text())
        print(cb.isChecked())
        
        
        # print(value)
        # print(self.ui.cbSinema.isChecked())
        # print(self.ui.cbSinema.text())
        
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    
    sys.exit(app.exec())
    
   
    
app()