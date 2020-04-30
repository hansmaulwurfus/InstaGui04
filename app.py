from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog

import sys
import design
import scrModule
import selenScrape
import instaloader

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):

        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.actionQuit.triggered.connect(self.lol)
        self.toolButton.clicked.connect(self.browseSlot)
        self.pushButton_1.clicked.connect(self.btn_clicked_followers)
        self.pushButton_2.clicked.connect(self.btn_clicked_likes)
        self.radioButton_1.clicked.connect(self.getRadio_1)  # self.getRadio_1)
        self.radioButton_2.clicked.connect(self.getRadio_2)
        self.lineEdit_1.setText("vling9898")
        self.lineEdit_2.setText("gaBWwkvpV6YukQwWhgFy")
        self.lineEdit_3.setText("dercoolstenebenjob")
        #QtCore.QMetaObject.connectSlotsByName(QtWidgets.QMainWindow)

    def getRadio_1(self):
        self.radioVal=1
        print("radioVal " + str(self.radioVal))

    def getRadio_2(self):
        self.radioVal=2
        print("radioVal " + str(self.radioVal))

    def browseSlot(self):
            global directory
            self.directory = QFileDialog.getExistingDirectory()
            self.labelDirectory.setText(self.directory)

    def btn_clicked_likes(self):
       # try:
        tmp=scrModule.scrapeClass(self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.directory)
        print("02 get all likes")
        print("spinbox:")
        print(self.spinBox_2.text())
        tmp.get_all_likes(self.spinBox_2.text())
        #except AttributeError:
        #        print("Attribute Error")

    def btn_clicked_followers(self):
        print("btn_clicked1")
        self.login = self.lineEdit_1.text()
        self.password = self.lineEdit_2.text()
        self.follow = self.lineEdit_3.text()
        self.maxFoll=self.spinBox_1.text()
        print(self.follow)
        print()
        #try:
        directory=self.directory
        print("directory " + directory)
        print(self.login + " " + self.password + " " + self.follow)
        print("Radioval " + str(self.radioVal))
        if self.radioVal==1:
                self.temp = scrModule.scrapeClass(self.login, self.password, self.follow, self.directory)
                self.temp.getFollowers()
        elif self.radioVal==2:
                self.filepath=r"C:\downloads"
                print("maxfoll " + str(self.maxFoll))
                self.temp = selenScrape.scrapeFunc([self.login, self.password, self.follow,self.maxFoll,self.directory])
                #self.temp.getFollowers()
            # else:
            #     print("variable not defined")
            #     self.w1 = QtWidgets.QMessageBox()
            #     self.w1.setText("Check method 1 or method 2!")
            #     print(self.radioVal)
            #     self.w1.show()
        #except AttributeError:
        #    print("AttributeError")
        #    print("variable not defined")
        #    self.w1 = QtWidgets.QMessageBox()
        #    self.w1.setText("Variable not defined")
        #    self.w1.show(
        #    raise



    def lol(self):
        print("lol")

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    sys._excepthook = sys.excepthook
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    sys.excepthook = exception_hook
    main()