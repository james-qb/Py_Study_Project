# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_From(object):
    def setupUi(self, From):
        From.setObjectName("From")
        From.resize(662, 434)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        From.setFont(font)
        self.label = QtWidgets.QLabel(From)
        self.label.setGeometry(QtCore.QRect(130, 100, 55, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(From)
        self.lineEdit.setGeometry(QtCore.QRect(220, 100, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(From)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(From)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 250, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(From)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 55, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(From)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 150, 201, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(From)
        QtCore.QMetaObject.connectSlotsByName(From)

    def retranslateUi(self, From):
        _translate = QtCore.QCoreApplication.translate
        From.setWindowTitle(_translate("From", "登录"))
        self.label.setText(_translate("From", "用户名"))
        self.pushButton.setText(_translate("From", "登录"))
        self.pushButton_2.setText(_translate("From", "取消"))
        self.label_3.setText(_translate("From", "密码"))
