# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Frontend_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QSlider, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1009, 832)
        self.main_frame = QFrame(Form)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(9, 19, 921, 701))
        self.main_frame.setStyleSheet(u"#main_frame {\n"
"	background-color: rgb(239, 228, 255)\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.site_frame_1 = QFrame(self.main_frame)
        self.site_frame_1.setObjectName(u"site_frame_1")
        self.site_frame_1.setGeometry(QRect(10, 10, 161, 671))
        self.site_frame_1.setStyleSheet(u"#site_frame_1 {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-left-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-bottom-left-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0b\u89d2\u5706\u89d2 */\n"
"}")
        self.site_frame_1.setFrameShape(QFrame.StyledPanel)
        self.site_frame_1.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.site_frame_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 54, 16))
        self.user_info = QPushButton(self.site_frame_1)
        self.user_info.setObjectName(u"user_info")
        self.user_info.setGeometry(QRect(20, 70, 121, 24))
        self.user_info.setStyleSheet(u"#user_info{\n"
"	border-radius: 12px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(143, 143, 143);\n"
"}")
        self.settings = QPushButton(self.site_frame_1)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(20, 620, 121, 24))
        self.settings.setStyleSheet(u"#settings {\n"
"	border-radius: 12px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(143, 143, 143);\n"
"}")
        self.training_statistic = QPushButton(self.site_frame_1)
        self.training_statistic.setObjectName(u"training_statistic")
        self.training_statistic.setGeometry(QRect(20, 580, 121, 24))
        self.training_statistic.setStyleSheet(u"#training_statistic {\n"
"		border-radius: 12px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(143, 143, 143);\n"
"}")
        self.rehabilition_training_button = QPushButton(self.site_frame_1)
        self.rehabilition_training_button.setObjectName(u"rehabilition_training_button")
        self.rehabilition_training_button.setGeometry(QRect(20, 540, 121, 24))
        self.rehabilition_training_button.setStyleSheet(u"#rehabilition_training_button {\n"
"		border-radius: 12px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(143, 143, 143);\n"
"}")
        self.patients_manage = QPushButton(self.site_frame_1)
        self.patients_manage.setObjectName(u"patients_manage")
        self.patients_manage.setGeometry(QRect(20, 500, 121, 24))
        self.patients_manage.setStyleSheet(u"#patients_manage {\n"
"		border-radius: 12px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(143, 143, 143);\n"
"}")
        self.label_2 = QLabel(self.site_frame_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 500, 21, 16))
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(170, 10, 741, 671))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.main_frame_2 = QFrame(self.page)
        self.main_frame_2.setObjectName(u"main_frame_2")
        self.main_frame_2.setGeometry(QRect(0, 0, 741, 671))
        self.main_frame_2.setStyleSheet(u"#main_frame_2 {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(194, 231, 255), stop:1 rgb(175, 255, 182));\n"
"	border-top-right-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-bottom-right-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0b\u89d2\u5706\u89d2 */\n"
"}")
        self.main_frame_2.setFrameShape(QFrame.StyledPanel)
        self.main_frame_2.setFrameShadow(QFrame.Raised)
        self.re_targets = QWidget(self.main_frame_2)
        self.re_targets.setObjectName(u"re_targets")
        self.re_targets.setGeometry(QRect(20, 70, 301, 251))
        self.re_targets.setStyleSheet(u"#re_targets {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px; \n"
"}")
        self.re_targets_title = QLabel(self.re_targets)
        self.re_targets_title.setObjectName(u"re_targets_title")
        self.re_targets_title.setGeometry(QRect(0, 0, 301, 31))
        self.re_targets_title.setStyleSheet(u"#re_targets_title {\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	\n"
"}")
        self.motor_coordination = QPushButton(self.re_targets)
        self.motor_coordination.setObjectName(u"motor_coordination")
        self.motor_coordination.setGeometry(QRect(10, 50, 281, 51))
        self.motor_coordination.setStyleSheet(u"#motor_coordination {\n"
"	background-color: rgb(238, 238, 238);\n"
"		border-radius: 12px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n""	border-color: rgb(143, 143, 143);\n"
"}")
        self.mind_training = QPushButton(self.re_targets)
        self.mind_training.setObjectName(u"mind_training")
        self.mind_training.setGeometry(QRect(10, 110, 281, 51))
        self.mind_training.setStyleSheet(u"#mind_training {\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 12px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(143, 143, 143);\n"
"}")
        self.static_strength = QPushButton(self.re_targets)
        self.static_strength.setObjectName(u"static_strength")
        self.static_strength.setGeometry(QRect(10, 170, 281, 51))
        self.static_strength.setStyleSheet(u"#static_strength {\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 12px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(143, 143, 143);\n"
"}")
        self.training_settings = QWidget(self.main_frame_2)
        self.training_settings.setObjectName(u"training_settings")
        self.training_settings.setGeometry(QRect(340, 70, 381, 251))
        self.training_settings.setStyleSheet(u"#training_settings {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.training_settings_title = QLabel(self.training_settings)
        self.training_settings_title.setObjectName(u"training_settings_title")
        self.training_settings_title.setGeometry(QRect(0, 0, 381, 31))
        self.training_settings_title.setStyleSheet(u"#training_settings_title {\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	\n"
"}")
        self.widget_4 = QWidget(self.training_settings)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(210, 40, 161, 201))
        self.widget_5 = QWidget(self.training_settings)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(20, 40, 171, 201))
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 141, 24))
        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 50, 141, 24))
        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 100, 141, 24))
        self.pushButton_8 = QPushButton(self.widget_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 150, 131, 24))
        self.label_3 = QLabel(self.main_frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 20, 71, 31))
        self.widget_3 = QWidget(self.main_frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(70, 380, 631, 221))
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.patients_management = QWidget(self.page_3)
        self.patients_management.setObjectName(u"patients_management")
        self.patients_management.setGeometry(QRect(-1, -1, 741, 671))
        self.patients_management.setStyleSheet(u"#patients_management {\n"
"		background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(194, 231, 255), stop:1 rgb(175, 255, 182))\n"
"}")
        self.widget_6 = QWidget(self.patients_management)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(50, 50, 641, 491))
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"#training_frame {\n"
"	background: qlineargradient(spread:pad, x1:0.4, y1:0.3, x2:1, y2:1, stop:0 rgb(255, 255, 255), stop:1 rgb(240, 228, 255));\n"
"	border-top-right-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-bottom-right-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0b\u89d2\u5706\u89d2 */\n"
"}")
        self.training_frame = QFrame(self.page_2)
        self.training_frame.setObjectName(u"training_frame")
        self.training_frame.setGeometry(QRect(-1, -1, 741, 671))
        self.training_frame.setStyleSheet(u"#training_frame {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(194, 231, 255), stop:1 rgb(175, 255, 182))\n"
"}")
        self.training_frame.setFrameShape(QFrame.StyledPanel)
        self.training_frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.training_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(19, 29, 711, 631))
        self.verticalSlider = QSlider(self.widget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(690, 0, 20, 631))
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 160, 681, 471))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-1, 10, 681, 151))
        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 70, 75, 24))
        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(120, 70, 75, 24))
        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(450, 70, 75, 24))
        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(570, 70, 75, 24))
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5bfc\u822a", None))
        self.user_info.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.settings.setText(QCoreApplication.translate("Form", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.training_statistic.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3\u7edf\u8ba1", None))
        self.rehabilition_training_button.setText(QCoreApplication.translate("Form", u"\u5eb7\u590d\u8bad\u7ec3", None))
        self.patients_manage.setText(QCoreApplication.translate("Form", u"\u60a3\u8005\u7ba1\u7406", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.re_targets_title.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3\u76ee\u6807", None))
        self.motor_coordination.setText(QCoreApplication.translate("Form", u"\u8fd0\u52a8\u534f\u8c03", None))
        self.mind_training.setText(QCoreApplication.translate("Form", u"\u601d\u7ef4\u8bad\u7ec3", None))
        self.static_strength.setText(QCoreApplication.translate("Form", u"\u9759\u6001\u529b\u91cf", None))
        self.training_settings_title.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3\u53c2\u6570", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3\u8bbe\u7f6e", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3\u62a5\u544a", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u8bc4\u4f30\u62a5\u544a", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
    # retranslateUi

