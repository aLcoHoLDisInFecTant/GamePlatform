# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_background = QtWidgets.QWidget(self.centralwidget)
        self.login_background.setGeometry(QtCore.QRect(20, 10, 1500, 1200))
        self.login_background.setAutoFillBackground(False)
        self.login_background.setStyleSheet("#login_background{\n"
"        background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(194, 231, 255), stop:1 rgb(175, 255, 182))\n"
"}")
        self.login_background.setObjectName("login_background")
        self.Login_Register = QtWidgets.QStackedWidget(self.login_background)
        self.Login_Register.setGeometry(QtCore.QRect(80, 80, 1000, 800))
        self.Login_Register.setObjectName("Login_Register")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.widget_login = QtWidgets.QWidget(self.page)
        self.widget_login.setGeometry(QtCore.QRect(0, 0, 1001, 731))
        self.widget_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_login.setAutoFillBackground(False)
        self.widget_login.setStyleSheet("#widget_login {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px; \n"
"}")
        self.widget_login.setObjectName("widget_login")
        self.label_background = QtWidgets.QLabel(self.widget_login)
        self.label_background.setGeometry(QtCore.QRect(0, -10, 701, 741))
        self.label_background.setStyleSheet("#label_background {\n"
"    border-radius:20px; \n"
"}")
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("graphs/login.png"))
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")
        self.label = QtWidgets.QLabel(self.widget_login)
        self.label.setGeometry(QtCore.QRect(640, 70, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_login)
        self.label_2.setGeometry(QtCore.QRect(560, 130, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_login)
        self.label_3.setGeometry(QtCore.QRect(760, 160, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_login)
        self.label_4.setGeometry(QtCore.QRect(590, 240, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_login)
        self.label_5.setGeometry(QtCore.QRect(590, 340, 54, 12))
        self.label_5.setObjectName("label_5")
        self.login_pushButton = QtWidgets.QPushButton(self.widget_login)
        self.login_pushButton.setGeometry(QtCore.QRect(850, 500, 75, 23))
        self.login_pushButton.setObjectName("login_pushButton")
        self.user_id = QtWidgets.QLineEdit(self.widget_login)
        self.user_id.setGeometry(QtCore.QRect(590, 280, 321, 20))
        self.user_id.setObjectName("user_id")
        self.password = QtWidgets.QLineEdit(self.widget_login)
        self.password.setGeometry(QtCore.QRect(590, 380, 321, 20))
        self.password.setObjectName("password")
        self.register_button = QtWidgets.QPushButton(self.widget_login)
        self.register_button.setGeometry(QtCore.QRect(760, 500, 75, 24))
        self.register_button.setObjectName("register_button")
        self.Login_Register.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.register_widget = QtWidgets.QWidget(self.page_2)
        self.register_widget.setGeometry(QtCore.QRect(140, 20, 721, 761))
        self.register_widget.setStyleSheet("#register_widget {\n"
"    background: rgb(255, 255, 255);\n"
"    border-radius: 20px; \n"
"\n"
"}")
        self.register_widget.setObjectName("register_widget")
        self.label_6 = QtWidgets.QLabel(self.register_widget)
        self.label_6.setGeometry(QtCore.QRect(30, 40, 54, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.register_widget)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 54, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.register_widget)
        self.label_8.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.label_8.setObjectName("label_8")
        self.register_name = QtWidgets.QLineEdit(self.register_widget)
        self.register_name.setGeometry(QtCore.QRect(220, 40, 113, 20))
        self.register_name.setObjectName("register_name")
        self.register_introduction = QtWidgets.QLineEdit(self.register_widget)
        self.register_introduction.setGeometry(QtCore.QRect(220, 120, 241, 71))
        self.register_introduction.setObjectName("register_introduction")
        self.register_phonecode = QtWidgets.QLineEdit(self.register_widget)
        self.register_phonecode.setGeometry(QtCore.QRect(220, 240, 161, 20))
        self.register_phonecode.setObjectName("register_phonecode")
        self.register_username = QtWidgets.QLineEdit(self.register_widget)
        self.register_username.setGeometry(QtCore.QRect(220, 320, 161, 20))
        self.register_username.setObjectName("register_username")
        self.register_password = QtWidgets.QLineEdit(self.register_widget)
        self.register_password.setGeometry(QtCore.QRect(220, 390, 161, 20))
        self.register_password.setObjectName("register_password")
        self.label_9 = QtWidgets.QLabel(self.register_widget)
        self.label_9.setGeometry(QtCore.QRect(30, 320, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.register_widget)
        self.label_10.setGeometry(QtCore.QRect(30, 390, 81, 16))
        self.label_10.setObjectName("label_10")
        self.register_confirm = QtWidgets.QPushButton(self.register_widget)
        self.register_confirm.setGeometry(QtCore.QRect(600, 690, 75, 24))
        self.register_confirm.setObjectName("register_confirm")
        self.register_cancel = QtWidgets.QPushButton(self.register_widget)
        self.register_cancel.setGeometry(QtCore.QRect(490, 690, 75, 24))
        self.register_cancel.setObjectName("register_cancel")
        self.Login_Register.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Login_Register.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "UserLogin"))
        self.label_2.setText(_translate("MainWindow", "欢迎登录"))
        self.label_3.setText(_translate("MainWindow", "康复训练&管理系统"))
        self.label_4.setText(_translate("MainWindow", "用户名"))
        self.label_5.setText(_translate("MainWindow", "密码"))
        self.login_pushButton.setText(_translate("MainWindow", "登录"))
        self.register_button.setText(_translate("MainWindow", "注册"))
        self.label_6.setText(_translate("MainWindow", "姓名"))
        self.label_7.setText(_translate("MainWindow", "介绍"))
        self.label_8.setText(_translate("MainWindow", "绑定电话号码"))
        self.label_9.setText(_translate("MainWindow", "再次输入用户名"))
        self.label_10.setText(_translate("MainWindow", "再次输入密码"))
        self.register_confirm.setText(_translate("MainWindow", "确定"))
        self.register_cancel.setText(_translate("MainWindow", "取消"))
