from PyQt5.QtWidgets import QMainWindow
#from static.Frontend_main_ui_qt5 import Ui_Form # 导入由pyuic5生成的类
from static.Login_ui_qt5 import Ui_MainWindow
from static.app_Li import Ui_app_main_window
# from Service.RepoController.repo import Repo
# from Service.WebController.PageController import PageController
import requests




class MainWindow(QMainWindow, Ui_app_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化UI
        self.pushButton.clicked.connect(self.on_button_clicked)  # 连接信号
        self.homeButton.clicked.connect(self.jump_to_main)
        self.trainButton.clicked.connect(self.jump_to_game)
        self.statButton.clicked.connect(self.jump_to_statistic)
        self.settingButton.clicked.connect(self.jump_to_setting)


    def jump_to_main(self):
        self.stackedWidget.setCurrentIndex(1)

    def jump_to_game(self):
        self.stackedWidget.setCurrentIndex(2)

    def jump_to_statistic(self):
        self.stackedWidget.setCurrentIndex(3)

    def jump_to_setting(self):
        self.stackedWidget.setCurrentIndex(4)

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        # 槽函数：定义按钮点击时的行为
        # 从输入框获取文本
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # 发送请求
        response = requests.post('http://localhost:8000/login', json={'username': username, 'password': password})
        # 获取响应
        if response.status_code == 200:
            self.label.setText("登录成功")
            # 登录成功后关闭登录窗口
            self.close()
            # 返回true
            return True
        else:
            self.label.setText("登录失败")
            # 清空输入框
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            # 返回false
            return False


class Controller:
    def __init__(self):
        self.main_window = MainWindow()
        self.login_window = LoginWindow()

    def login(self):
        self.login_window.show()
        # 进入登录循环
        self.login_window.exec_()
        # 登录成功后关闭登录窗口
        # 根据登录窗口的返回值判断是否登录成功
        if self.login_window.on_button_clicked():
            self.login_close()
            # 登录成功后打开主窗口
            self.show_main_window()





    def show_main_window(self):
        self.main_window.show()

    def login_close(self):
        self.login_window.close()
        self.show_main_window()

    def main_close(self):
        self.main_window.close()

    def mainProcess(self):
        self.login()

