import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Preset_Ui import Ui_MainWindow
import sys
from pathlib import Path
import time



class application(QMainWindow, Ui_MainWindow):

    def __init__(self,TCP):
        super(application, self).__init__()
        self.TCP = TCP
        print(self.TCP)
        self.Key_W = False
        self.Key_A = False
        self.Key_S = False
        self.Key_D = False
        self.Key_Space = False
        self.setupUi(self)
        self.addBtn.clicked.connect(self.createpreset)
        self.loadBtn.clicked.connect(self.load)
        self.newRowBtn.clicked.connect(self.newrow)
        self.saveBtn.clicked.connect(self.save)
        self.runBtn.clicked.connect(self.run)
        if not os.path.exists('Presets'):
            os.makedirs('Presets')
        self.path = os.path.join(os.getcwd(),'Presets')
        files = os.listdir(self.path)
        for f in files:
            print(f[:-4])
            self.presetList.addItem(f[:-4])

    def createpreset(self):
        value = self.presetBox.text()  # Get the value of the lineEdit
        if value != '':
            if os.path.exists(os.path.join(self.path,value+'.txt')):
                self.presetStatus.setText('Already Created A Preset')
            else:
                with open(os.path.join(self.path,value+'.txt'), 'w') as fp:
                    print('Added:', value)
                    self.presetBox.clear()  # Clear the text
                    self.presetList.addItem(value)  # Add the value we got to the list
        else:
            self.presetStatus.setText('Preset is blank!')

    def load(self):
        print('loading preset:',self.presetList.currentItem().text())
        fileName = self.presetList.currentItem().text()
        self.presetLabel.setText(fileName)
        self.file = open(os.path.join(self.path,fileName+'.txt'), 'r')
        self.actionsTable.setRowCount(0)
        #self.actionsTable.clear()
        for entry in self.file:
            actions = entry.strip().split(',')
            self.addTableRow(self.actionsTable,actions)
            print(actions)
        self.file.close()

    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

    def newrow(self):
        self.actionsTable.insertRow(self.actionsTable.rowCount())

    '''
    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            pass
        else:
            if event.key() == Qt.Key_W:
                self.on_btn_ForWard()
                self.Key_W=True
            elif event.key() == Qt.Key_S:
                self.on_btn_BackWard()
                self.Key_S=True
            elif event.key() == Qt.Key_A:
                self.on_btn_Turn_Left()
                self.Key_A=True
            elif event.key() == Qt.Key_D:
                self.on_btn_Turn_Right()
                self.Key_D=True
            elif event.key() == Qt.Key_Space:
                self.on_btn_Buzzer()
                self.Key_Space=True
    '''

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W:
            if not(event.isAutoRepeat()) and self.Key_W==True:
                self.on_btn_Stop()
                self.Key_W=False
        elif event.key() == Qt.Key_A:
            if not(event.isAutoRepeat()) and self.Key_A==True:
                self.on_btn_Stop()
                self.Key_A=False
        elif event.key() == Qt.Key_S:
            if not(event.isAutoRepeat()) and self.Key_S==True:
                self.on_btn_Stop()
                self.Key_S=False
        elif event.key() == Qt.Key_D:
            if not(event.isAutoRepeat()) and self.Key_D==True:
                self.on_btn_Stop()
                self.Key_D=False

    def on_btn_ForWard(self):
        ForWard=self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.endChar
        #self.TCP.sendData(cmd.CMD_MOTOR+ForWard)

    def on_btn_Turn_Left(self):
        Turn_Left=self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.endChar
        #.TCP.sendData(cmd.CMD_MOTOR+ Turn_Left)

    def on_btn_BackWard(self):
        BackWard=self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.endChar
        #self.TCP.sendData(cmd.CMD_MOTOR+BackWard)

    def on_btn_Turn_Right(self):
        Turn_Right=self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.endChar
        #self.TCP.sendData(cmd.CMD_MOTOR+Turn_Right)

    def on_btn_Stop(self):
        Stop=self.intervalChar+str(0)+self.intervalChar+str(0)+self.intervalChar+str(0)+self.intervalChar+str(0)+self.endChar
        #self.TCP.sendData(cmd.CMD_MOTOR+Stop)

    def save(self):
        fileName = self.presetList.currentItem().text()
        self.file = open(os.path.join(self.path,fileName+'.txt'), 'w')
        for row in range(self.actionsTable.rowCount()):
            print(row)
            self.file.write(str(self.actionsTable.item(row,0).text())+','+self.actionsTable.item(row,1).text()+'\n')
        self.file.close()
        print('saved')

    def run(self):
        print('run')
        for row in range(self.actionsTable.rowCount()):
            print(self.actionsTable.item(row,0).text(),self.actionsTable.item(row,1).text())
            self.decoder(self.actionsTable.item(row,0).text(), float(self.actionsTable.item(row,1).text()))


    def decoder(self,action,duration):
        if action == 'Forward':
            self.TCP.sendData('CMD_MOTOR#1500#1500#1500#1500\n')
            time.sleep(duration)
            self.TCP.sendData('CMD_MOTOR#0#0#0#0\n')
        elif action == 'Left':
            self.TCP.sendData('CMD_MOTOR#-1500#-1500#1500#1500\n')
            time.sleep(duration)
            self.TCP.sendData('CMD_MOTOR#0#0#0#0\n')
        elif action == 'Right':
            self.TCP.sendData('CMD_MOTOR#1500#1500#-1500#-1500\n')
            time.sleep(duration)
            self.TCP.sendData('CMD_MOTOR#0#0#0#0\n')
        elif action == 'Backward':
            self.TCP.sendData('CMD_MOTOR#-1500#-1500#-1500#-1500\n')
            time.sleep(duration)
            self.TCP.sendData('CMD_MOTOR#0#0#0#0\n')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) #*
    MainWindow = application()
    MainWindow.show()
    sys.exit(app.exec_()) #*