# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manager_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Manager_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 325)
        Form.setMinimumSize(QtCore.QSize(420, 325))
        Form.setMaximumSize(QtCore.QSize(420, 325))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 25))
        self.pushButton_3.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 25))
        self.pushButton_2.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setPlaceholderText("Student ID")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(70, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_5.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_4.setMinimumSize(QtCore.QSize(0, 25))
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setPlaceholderText("SSID")
        self.horizontalLayout_5.addWidget(self.textEdit_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_5.setMinimumSize(QtCore.QSize(0, 25))
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setPlaceholderText("PASSWORD")
        self.horizontalLayout_5.addWidget(self.textEdit_5)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_2.addWidget(self.textEdit_3)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout.addWidget(self.frame_5)
        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "REFRESH"))
        self.pushButton_2.setText(_translate("Form", "CONNECT"))
        self.pushButton.setText(_translate("Form", "GENERATE"))
        self.pushButton_5.setText(_translate("Form", "CHECK"))
        self.pushButton_4.setText(_translate("Form", "UPDATE"))
        self.pushButton_6.setText(_translate("Form", "READ"))
import model.resource