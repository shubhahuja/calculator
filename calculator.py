# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\shubham\Desktop\calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    text =""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.num1 = QtWidgets.QPushButton(self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(56, 95, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num1.setFont(font)
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QPushButton(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(156, 95, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num2.setFont(font)
        self.num2.setObjectName("num2")
        self.num8 = QtWidgets.QPushButton(self.centralwidget)
        self.num8.setGeometry(QtCore.QRect(156, 265, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num8.setFont(font)
        self.num8.setObjectName("num8")
        self.num4 = QtWidgets.QPushButton(self.centralwidget)
        self.num4.setGeometry(QtCore.QRect(56, 185, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num4.setFont(font)
        self.num4.setObjectName("num4")
        self.num9 = QtWidgets.QPushButton(self.centralwidget)
        self.num9.setGeometry(QtCore.QRect(256, 265, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num9.setFont(font)
        self.num9.setObjectName("num9")
        self.num5 = QtWidgets.QPushButton(self.centralwidget)
        self.num5.setGeometry(QtCore.QRect(156, 185, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num5.setFont(font)
        self.num5.setObjectName("num5")
        self.num6 = QtWidgets.QPushButton(self.centralwidget)
        self.num6.setGeometry(QtCore.QRect(256, 185, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num6.setFont(font)
        self.num6.setObjectName("num6")
        self.num3 = QtWidgets.QPushButton(self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(256, 95, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num3.setFont(font)
        self.num3.setObjectName("num3")
        self.num7 = QtWidgets.QPushButton(self.centralwidget)
        self.num7.setGeometry(QtCore.QRect(56, 265, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num7.setFont(font)
        self.num7.setObjectName("num7")
        self.num0 = QtWidgets.QPushButton(self.centralwidget)
        self.num0.setGeometry(QtCore.QRect(156, 345, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.num0.setFont(font)
        self.num0.setObjectName("num0")
        self.addop = QtWidgets.QPushButton(self.centralwidget)
        self.addop.setGeometry(QtCore.QRect(366, 95, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.addop.setFont(font)
        self.addop.setObjectName("addop")
        self.multop = QtWidgets.QPushButton(self.centralwidget)
        self.multop.setGeometry(QtCore.QRect(366, 265, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.multop.setFont(font)
        self.multop.setObjectName("multop")
        self.subop = QtWidgets.QPushButton(self.centralwidget)
        self.subop.setGeometry(QtCore.QRect(366, 185, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.subop.setFont(font)
        self.subop.setObjectName("subop")
        self.divop = QtWidgets.QPushButton(self.centralwidget)
        self.divop.setGeometry(QtCore.QRect(366, 345, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.divop.setFont(font)
        self.divop.setObjectName("divop")
        self.sqop = QtWidgets.QPushButton(self.centralwidget)
        self.sqop.setGeometry(QtCore.QRect(476, 185, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.sqop.setFont(font)
        self.sqop.setObjectName("sqop")
        self.powop = QtWidgets.QPushButton(self.centralwidget)
        self.powop.setGeometry(QtCore.QRect(476, 95, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.powop.setFont(font)
        self.powop.setObjectName("powop")
        self.eqop = QtWidgets.QPushButton(self.centralwidget)
        self.eqop.setGeometry(QtCore.QRect(476, 265, 81, 151))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.eqop.setFont(font)
        self.eqop.setObjectName("eqop")
        self.leftb = QtWidgets.QPushButton(self.centralwidget)
        self.leftb.setGeometry(QtCore.QRect(56, 345, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.leftb.setFont(font)
        self.leftb.setObjectName("leftb")
        self.rightb = QtWidgets.QPushButton(self.centralwidget)
        self.rightb.setGeometry(QtCore.QRect(256, 345, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.rightb.setFont(font)
        self.rightb.setObjectName("rightb")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 30, 20, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(570, 30, 20, 401))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(37, 20, 541, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(40, 420, 541, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.num1.clicked.connect(self.button1)
        self.num2.clicked.connect(self.button2)
        self.num3.clicked.connect(self.button3)
        self.num4.clicked.connect(self.button4)
        self.num5.clicked.connect(self.button5)
        self.num6.clicked.connect(self.button6)
        self.num7.clicked.connect(self.button7)
        self.num8.clicked.connect(self.button8)
        self.num9.clicked.connect(self.button9)
        self.num0.clicked.connect(self.button0)
        
        self.addop.clicked.connect(self.buttonadd)
        self.multop.clicked.connect(self.buttonmult)
        self.subop.clicked.connect(self.buttonsub)
        self.divop.clicked.connect(self.buttondiv)
        self.powop.clicked.connect(self.buttonpow)
        self.sqop.clicked.connect(self.buttonsq)
        self.rightb.clicked.connect(self.buttonrig)

        self.leftb.clicked.connect(self.buttonlef)


    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.num1.setText(_translate("MainWindow", "1"))
        self.num2.setText(_translate("MainWindow", "2"))
        self.num8.setText(_translate("MainWindow", "8"))
        self.num4.setText(_translate("MainWindow", "4"))
        self.num9.setText(_translate("MainWindow", "9"))
        self.num5.setText(_translate("MainWindow", "5"))
        self.num6.setText(_translate("MainWindow", "6"))
        self.num3.setText(_translate("MainWindow", "3"))
        self.num7.setText(_translate("MainWindow", "7"))
        self.num0.setText(_translate("MainWindow", "0"))
        self.addop.setText(_translate("MainWindow", "+"))
        self.multop.setText(_translate("MainWindow", "*"))
        self.subop.setText(_translate("MainWindow", "-"))
        self.divop.setText(_translate("MainWindow", "/"))
        self.sqop.setText(_translate("MainWindow", "sqrt"))
        self.powop.setText(_translate("MainWindow", "**"))
        self.eqop.setText(_translate("MainWindow", "="))
        self.leftb.setText(_translate("MainWindow", "("))
        self.rightb.setText(_translate("MainWindow", ")"))
        self.label.setText(_translate("MainWindow", "0"))


    def button1(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"1"
        self.label.setText(Ui_MainWindow.text)


    def button2(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"2"
        self.label.setText(Ui_MainWindow.text)

    def button3(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"3"
        self.label.setText(Ui_MainWindow.text)

    def button4(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"4"
        self.label.setText(Ui_MainWindow.text)

    def button5(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"5"
        self.label.setText(Ui_MainWindow.text)

    def button6(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"6"
        self.label.setText(Ui_MainWindow.text)

    def button7(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"7"
        self.label.setText(Ui_MainWindow.text)

    def button8(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"8"
        self.label.setText(Ui_MainWindow.text)

    def button9(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"9"
        self.label.setText(Ui_MainWindow.text)

    def button0(self):
        Ui_MainWindow.text=Ui_MainWindow.text+"0"
        self.label.setText(Ui_MainWindow.text)

    def buttonadd(self):
        Ui_MainWindow.text=Ui_MainWindow.text+" + "
        self.label.setText(Ui_MainWindow.text)

    def buttonsub(self):
        Ui_MainWindow.text=Ui_MainWindow.text+" - "
        self.label.setText(Ui_MainWindow.text)

    def buttonmult(self):
        Ui_MainWindow.text=Ui_MainWindow.text+" * "
        self.label.setText(Ui_MainWindow.text)

    def buttondiv(self):
        Ui_MainWindow.text=Ui_MainWindow.text+" / "
        self.label.setText(Ui_MainWindow.text)

    def buttonpow(self):
        Ui_MainWindow.text=Ui_MainWindow.text+" ** "
        self.label.setText(Ui_MainWindow.text)

    def buttonsq(self):
        Ui_MainWindow.text=Ui_MainWindow.text+" sqrt "
        self.label.setText(Ui_MainWindow.text)
        
    def buttonlef(self):
        Ui_MainWindow.text=Ui_MainWindow.text+" ( "
        self.label.setText(Ui_MainWindow.text)
    def buttonrig(self):
        Ui_MainWindow.text=Ui_MainWindow.text+" ) "
        self.label.setText(Ui_MainWindow.text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
