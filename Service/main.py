import sys

from Controller import Controller
from static.Frontend_main_ui_utf8 import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 实例化cotroller,并调用show_main_window方法
    controller = Controller()
    #controller.show_main_window()
    controller.mainProcess()
    # 退出程序，关闭数据库

    sys.exit(app.exec_())


