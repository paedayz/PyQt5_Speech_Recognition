# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 330, 171, 71))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: black;\n"
"    border: 2px solid white;\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: gray;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 150, 631, 161))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.backgroud = QtWidgets.QLabel(self.centralwidget)
        self.backgroud.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.backgroud.setText("")
        self.backgroud.setPixmap(QtGui.QPixmap("assets/space_dust.jpg"))
        self.backgroud.setScaledContents(True)
        self.backgroud.setObjectName("backgroud")
        self.logo_1 = QtWidgets.QLabel(self.centralwidget)
        self.logo_1.setGeometry(QtCore.QRect(550, 30, 81, 31))
        self.logo_1.setText("")
        self.logo_1.setPixmap(QtGui.QPixmap("assets/AIAT-W.png"))
        self.logo_1.setScaledContents(True)
        self.logo_1.setObjectName("logo_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 10, 71, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets/logoSuperAI.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.backgroud.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.logo_1.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Click Me"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
