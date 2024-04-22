from PyQt5.QtWidgets import QMainWindow
from static.Frontend_main_ui_qt5 import Ui_Form  # 导入由pyuic5生成的类
from static.Login_ui_qt5 import Ui_MainWindow
# from Service.RepoController.repo import Repo
# from Service.WebController.PageController import PageController
import requests


def get_csrf_token():
    url = 'http://localhost:8000/medic_platform/get_token/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # 解析 JSON 数据
        if data.get('res') == "0":
            csrftoken = data.get('token')
            print("Token received:", csrftoken)
            # 在 Python 中，通常不需要设置 cookie，因为 session 会自动处理。
            # 但如果需要，可以这样做:
            session = requests.Session()
            session.cookies.set('csrftoken', csrftoken)
            return csrftoken
        else:
            print("获取 token 失败")
    else:
        print("请求失败，状态码：", response.status_code)


# 调用函数
token = get_csrf_token()


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化UI
        # self.pushButton.clicked.connect(self.on_button_clicked)  # 连接信号


class Login_Register_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.session = requests.Session()
        self.login_pushButton.clicked.connect(self.on_Login_button_clicked)
        self.register_confirm.clicked.connect(self.on_Register_button_clicked)
        self.register_button.clicked.connect(self.register_jump)
        self.register_cancel.clicked.connect(self.register_back_login)

    def on_Login_button_clicked(self):
        # 槽函数：定义按钮点击时的行为
        # 从输入框获取文本

        username = self.user_id.text()
        password = self.password.text()
        url = 'http://localhost:8000/medic_platform/login/'
        new_token = get_csrf_token()
        headers = {'X-CSRFToken': new_token}
        data = {'username': username, 'password': password}
        # 发送请求
        response = self.session.post(url, headers=headers, json=data)
        # 获取响应
        if response.status_code == 200:
            self.label.setText("登录成功")
            # 保存CSRF令牌
            self.session.cookies.update(response.cookies)
            # 打开主窗口
            self.show_main_window()

        else:
            self.label.setText("登录失败")
            # 清空输入框
            self.user_id.clear()
            self.password.clear()
            # 返回false
            self.Login_Register.setCurrentIndex(1)

    def on_Register_button_clicked(self):

        # 槽函数：定义按钮点击时的行为
        # 从输入框获取文本
        actual_name = self.register_name.text()
        introduction = self.register_introduction.text()
        phonecode = self.register_phonecode.text()
        username = self.register_username.text()
        password = self.register_password.text()
        # 发送请求
        url = 'http://localhost:8000/medic_platform/register/'
        new_token = get_csrf_token()
        headers = {'X-CSRFToken': new_token}
        data = {'actual_name': actual_name, 'introduction': introduction, 'phonecode': phonecode, 'username': username,
                'password': password}
        response = self.session.post(url, headers=headers, json=data)
        # 获取响应
        if response.status_code == 200:
            self.label_6.setText("注册成功")
            # 保存CSRF令牌
            # self.session.cookies = response.cookies['csrftoken']
            self.session.cookies.update(response.cookies)
            # 打开主窗口
            self.show_main_window()

        else:
            self.label_6.setText("注册失败")
            # 清空输入框
            self.register_name.clear()
            self.register_introduction.clear()
            self.register_phonecode.clear()
            self.register_username.clear()
            self.register_password.clear()

    def register_jump(self):
        self.Login_Register.setCurrentIndex(1)

    def register_back_login(self):
        self.Login_Register.setCurrentIndex(0)


class Controller:
    def __init__(self):
        self.main_window = MainWindow()
        self.login_window = Login_Register_Window()
        # self.csrf_token = get_csrf_token()

    '''
    def post_data(self):
        url = 'http://localhost:8000/medic_platform/some_post_action/'
        headers = {'X-CSRFToken': self.session.cookies.get('csrftoken')}
        data = {'some_data': 'value'}
        response = self.session.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print("Data posted successfully")
        else:
            print("Failed to post data")
    
    def get_CSRF_token(self):
        url = 'http://localhost:8000/medic_platform/login/'
        response = requests.get(url)
        return response.cookies.get('csrftoken')
    '''

    def login(self):
        self.login_window.show()
        # # 进入登录循环
        # # 登录成功后关闭登录窗口
        # # 根据登录窗口的返回值判断是否登录成功
        # if self.login_window.on_Login_button_clicked():
        #     self.login_close()
        #     # 登录成功后打开主窗口
        #     self.show_main_window()
        # else:
        #     # 跳转到注册页面
        #     # 切换到注册页面
        #     self.login_window.Login_Register.setCurrentIndex(1)
        #     if self.login_window.on_Register_button_clicked():
        #         self.login_close()
        #         # 登录成功后打开主窗口
        #         self.show_main_window()

    def show_main_window(self):
        self.main_window.show()

    def mainProcess(self):
        self.login()
        # 调用函数
