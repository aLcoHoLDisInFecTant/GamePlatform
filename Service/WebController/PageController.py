import sys
from PyQt5.QtWidgets import QApplication, QWidget
from static.Frontend_main_ui_qt5 import *  # 导入自动生成的UI类
from static.Login_ui_qt5 import *  # 导入自动生成的UI类
import pymysql

class PageController(QWidget) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.login = Ui_MainWindow()
        self.ui.setupUi(self)
        self.login.setupUi(self)


    def register(self):
        # 读取用户名和密码输入框的内容，放入数据库
        username = self.login.widget_login.lineEdit.text()
        password = self.password.lineEdit_2.text()

        return username, password



    def Login(self):
        self.login.show()
