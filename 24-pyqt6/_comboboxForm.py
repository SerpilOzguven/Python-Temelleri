# Form implementation generated from reading ui file '_comboboxForm.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 339)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(20, 20, 271, 111))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lblResult = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(320, 20, 271, 111))
        self.lblResult.setObjectName("lblResult")
        self.btnGetItem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGetItem.setGeometry(QtCore.QRect(20, 150, 271, 61))
        self.btnGetItem.setObjectName("btnGetItem")
        self.btnLoadItems = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLoadItems.setGeometry(QtCore.QRect(310, 150, 271, 61))
        self.btnLoadItems.setObjectName("btnLoadItems")
        self.btnClearItems = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClearItems.setGeometry(QtCore.QRect(20, 230, 271, 61))
        self.btnClearItems.setObjectName("btnClearItems")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblResult.setText(_translate("MainWindow", "TextLabel"))
        self.btnGetItem.setText(_translate("MainWindow", "Get Item"))
        self.btnLoadItems.setText(_translate("MainWindow", "Load Items"))
        self.btnClearItems.setText(_translate("MainWindow", "ClearItems"))
