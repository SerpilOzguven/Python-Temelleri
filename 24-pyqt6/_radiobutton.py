from PyQt6 import QtWidgets
import sys
from _radiobuttonForm import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self) :
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioLise.setChecked(True)
        
        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbeycan.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)
        
        self.ui.radioIlkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)
        
        self.ui.btnUlke.clicked.connect(self.getselectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getselectedEgitim)
        
    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print('seçilen ülke: '+ rb.text())
            
    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print('seçilen eğitim: '+ rb.text())
            
            
    def getselectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton) 
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText('seçilen ülke: ' + rb.text())
        
    def getselectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton) 
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText('seçilen eğitim: ' + rb.text())
        
        
        
app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())