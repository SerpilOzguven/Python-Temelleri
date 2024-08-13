from PyQt6 import QtWidgets
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    
app()