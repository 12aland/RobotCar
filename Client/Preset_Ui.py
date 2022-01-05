# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\Qt\basic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setEnabled(True)
        self.addBtn.setGeometry(QtCore.QRect(10, 110, 120, 20))
        self.addBtn.setObjectName("addBtn")
        self.presetList = QtWidgets.QListWidget(self.centralwidget)
        self.presetList.setGeometry(QtCore.QRect(150, 80, 150, 350))
        self.presetList.setObjectName("presetList")
        self.presetBox = QtWidgets.QLineEdit(self.centralwidget)
        self.presetBox.setGeometry(QtCore.QRect(10, 80, 120, 20))
        self.presetBox.setObjectName("presetBox")
        self.loadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadBtn.setGeometry(QtCore.QRect(150, 440, 150, 50))
        self.loadBtn.setObjectName("loadBtn")
        self.YouHaveSelected = QtWidgets.QLabel(self.centralwidget)
        self.YouHaveSelected.setGeometry(QtCore.QRect(320, 30, 100, 30))
        self.YouHaveSelected.setObjectName("YouHaveSelected")
        self.presetLabel = QtWidgets.QLabel(self.centralwidget)
        self.presetLabel.setGeometry(QtCore.QRect(420, 30, 221, 31))
        self.presetLabel.setText("")
        self.presetLabel.setObjectName("presetLabel")
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(469, 440, 251, 50))
        self.runBtn.setObjectName("runBtn")
        self.presetStatus = QtWidgets.QLabel(self.centralwidget)
        self.presetStatus.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.presetStatus.setText("")
        self.presetStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.presetStatus.setObjectName("presetStatus")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(420, 440, 41, 50))
        self.saveBtn.setObjectName("saveBtn")
        self.actionsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.actionsTable.setGeometry(QtCore.QRect(420, 80, 300, 350))
        self.actionsTable.setObjectName("actionsTable")
        self.actionsTable.setColumnCount(2)
        self.actionsTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.actionsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.actionsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.actionsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.actionsTable.setItem(0, 1, item)
        self.newRowBtn = QtWidgets.QPushButton(self.centralwidget)
        self.newRowBtn.setGeometry(QtCore.QRect(662, 88, 54, 42))
        self.newRowBtn.setObjectName("newRowBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addBtn.setText(_translate("MainWindow", "Create Preset"))
        self.loadBtn.setText(_translate("MainWindow", "Load"))
        self.YouHaveSelected.setText(_translate("MainWindow", "You have selected:"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        item = self.actionsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Action"))
        item = self.actionsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        __sortingEnabled = self.actionsTable.isSortingEnabled()
        self.actionsTable.setSortingEnabled(False)
        item = self.actionsTable.item(0, 0)
        item.setText(_translate("MainWindow", "Forward"))
        item = self.actionsTable.item(0, 1)
        item.setText(_translate("MainWindow", "1.0"))
        self.actionsTable.setSortingEnabled(__sortingEnabled)
        self.newRowBtn.setText(_translate("MainWindow", "New Row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())