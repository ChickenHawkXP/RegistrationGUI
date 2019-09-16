# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jayma\OneDrive\Documents\GitHub\RegistrationGUI\BADui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import json
import mysql.connector
import mysql.connector.errors as ErrorOut
table = "information"
with open('config.json', 'r') as files:
    data = json.load(files)
    try:
         database = mysql.connector.connect(host = data['host'],
                                       user = data['user'],
                                       password = data['password'],
                                       database = data['database'],
                                       auth_plugin = data['auth_plugin'])
    except:
         print('Could not make connection with database!')
cursor = database.cursor(buffered = True)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 210, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 100, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 210, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 100, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 210, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(410,100, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.fname = QtWidgets.QLineEdit(self.centralwidget)
        self.fname.setGeometry(QtCore.QRect(0, 80, 131, 20))
        self.fname.setObjectName("fname")
        self.lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lname.setGeometry(QtCore.QRect(0, 160, 131, 20))
        self.lname.setObjectName("lname")
        self.birthday = QtWidgets.QLineEdit(self.centralwidget)
        self.birthday.setGeometry(QtCore.QRect(0, 270, 131, 20))
        self.birthday.setObjectName("birthday")
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(230, 70, 131, 20))
        self.address.setObjectName("address")
        self.phone = QtWidgets.QLineEdit(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(230, 170, 131, 20))
        self.phone.setObjectName("phone")
        self.sex = QtWidgets.QLineEdit(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(230, 270, 131, 20))
        self.sex.setObjectName("sex")
        self.major = QtWidgets.QLineEdit(self.centralwidget)
        self.major.setGeometry(QtCore.QRect(410, 70, 131, 20))
        self.major.setObjectName("major")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(410, 170, 131, 20))
        self.email.setObjectName("email")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(220, 320, 161, 16))
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        self.menuRegistration_Form = QtWidgets.QMenu(self.menubar)
        self.menuRegistration_Form.setObjectName("menuRegistration_Form")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuRegistration_Form.menuAction())
        
        def add_to_db():
            fname = self.fname.text()
            lname = self.lname.text()
            birthday = self.birthday.text()
            email = self.email.text()
            address = self.address.text()
            phone = self.phone.text()
            sex = self.sex.text()
            major = self.major.text()

            if(fname == "" or lname == "" or birthday == "" or email == "" or address == "" or phone == "" or sex == "" or major == ""):
                error = QMessageBox()
                error.setText("Please fill in all fields!")
                error.exec()
                return
            #print("First Name: %s\nLast Name: %s\nBirthday: %s\nEmail: %s\nAddress: %s\nPhone: %s\nSex: %s\nMajor: %s\nPets: %d\nHeight: %d" %(fname,lname,birthday,email,address,phone,sex,major,pets,height))
            try:
                cursor.execute("""INSERT INTO %s
                                    VALUES 
                                    ('%s','%s','%s','%s','%s','%s','%s','%s');""" %(table,fname,lname,birthday,email,address,phone,sex,major))
            except:
                error = QMessageBox()
                error.setText("Invalid Character found, please rer-enter data")
                error.exec()
                return
            database.commit()
            self.fname.clear()
            self.lname.clear()
            self.birthday.clear()
            self.email.clear()
            self.address.clear()
            self.phone.clear()
            self.address.clear()
            self.sex.clear()
            self.major.clear()
            
            print("User has been added!")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(add_to_db)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "First Name"))
        self.label_2.setText(_translate("MainWindow", "Last Name"))
        self.label_3.setText(_translate("MainWindow", "Date of Birth"))
        self.label_4.setText(_translate("MainWindow", "Address"))
        self.label_5.setText(_translate("MainWindow", "Phone Number"))
        self.label_6.setText(_translate("MainWindow", "Sex"))
        self.label_7.setText(_translate("MainWindow", "Major"))
        self.label_10.setText(_translate("MainWindow", "Email"))
        self.label_11.setText(_translate("MainWindow", "*ALL FIELDS ARE REQUIRED!*"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.menuRegistration_Form.setTitle(_translate("MainWindow", "Registration Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
