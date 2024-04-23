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
    QScrollBar, QSizePolicy, QSlider, QStackedWidget,
    QVBoxLayout, QWidget)

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
"	background: qlineargradient(x1:0.7, y1:0.5, x2:1, y2:1,\n"
"                                stop:0 rgb(134, 142, 255), \n"
"                                stop:1 rgb(233, 206, 255));\n"
"	border-top-left-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-bottom-left-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0b\u89d2\u5706\u89d2 */\n"
"}")
        self.site_frame_1.setFrameShape(QFrame.StyledPanel)
        self.site_frame_1.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.site_frame_1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 10, 141, 51))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 41, 41))
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 10, 91, 16))
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 30, 71, 20))
        self.label_2 = QLabel(self.site_frame_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 121, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 9pt \"Microsoft YaHei UI\";\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.label_3 = QLabel(self.site_frame_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 121, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 9pt \"Microsoft YaHei UI\";\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.label_4 = QLabel(self.site_frame_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 180, 121, 31))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 9pt \"Microsoft YaHei UI\";\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.label_8 = QLabel(self.site_frame_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 610, 54, 16))
        self.label_8.setStyleSheet(u"QLabel {\n"
"	font: 9pt \"Microsoft YaHei UI\";\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.label_18 = QLabel(self.site_frame_1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 580, 54, 16))
        self.label_18.setStyleSheet(u"QLabel {\n"
"	font: 9pt \"Microsoft YaHei UI\";\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.pushButton = QPushButton(self.site_frame_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 230, 75, 24))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    /* \u8bbe\u7f6e\u6309\u94ae\u80cc\u666f\u8272\u548c\u900f\u660e\u5ea6 */\n"
"    background-color: rgba(100, 100, 255, 150); /* \u8fd9\u91cc\u4f7f\u7528\u4e86\u534a\u900f\u660e\u7684\u84dd\u8272 */\n"
"    \n"
"    /* \u8bbe\u7f6e\u8fb9\u6846\u6837\u5f0f */\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: #555555;\n"
"    \n"
"    /* \u8bbe\u7f6e\u5706\u89d2 */\n"
"    border-radius: 15px; /* \u589e\u5927\u8fd9\u4e2a\u503c\u4f1a\u4f7f\u6309\u94ae\u8fb9\u7f18\u66f4\u5706 */\n"
"    \n"
"    /* \u6587\u5b57\u989c\u8272 */\n"
"    color: white;\n"
"    \n"
"    /* \u6309\u94ae\u5728\u60ac\u6d6e\u65f6\u7684\u6837\u5f0f */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 100, 255, 200); /* \u60ac\u6d6e\u65f6\u66f4\u5c11\u7684\u900f\u660e\u5ea6 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(100, 100, 255, 255); /* \u6309\u4e0b\u65f6\u4e0d\u900f\u660e */\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(self.site_frame_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 270, 75, 24))
        self.pushButton_3 = QPushButton(self.site_frame_1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 310, 75, 24))
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(170, 10, 741, 671))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.main_frame_2 = QFrame(self.page)
        self.main_frame_2.setObjectName(u"main_frame_2")
        self.main_frame_2.setGeometry(QRect(0, 0, 741, 671))
        self.main_frame_2.setStyleSheet(u"#main_frame_2 {\n"
"	background: qlineargradient(spread:pad, x1:0.4, y1:0.3, x2:1, y2:1, stop:0 rgb(255, 255, 255), stop:1 rgb(240, 228, 255));\n"
"	border-top-right-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-bottom-right-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0b\u89d2\u5706\u89d2 */\n"
"}")
        self.main_frame_2.setFrameShape(QFrame.StyledPanel)
        self.main_frame_2.setFrameShadow(QFrame.Raised)
        self.Game_Frame = QFrame(self.main_frame_2)
        self.Game_Frame.setObjectName(u"Game_Frame")
        self.Game_Frame.setEnabled(True)
        self.Game_Frame.setGeometry(QRect(10, 60, 721, 591))
        self.Game_Frame.setStyleSheet(u"#Game_Frame {\n"
"    	border-radius: 10px; /* \u8bbe\u7f6e\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    background: qlineargradient(x1:0.3, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgb(179, 202, 255), \n"
"                                stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.Game_Frame.setFrameShape(QFrame.StyledPanel)
        self.Game_Frame.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.Game_Frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(30, 20, 651, 331))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 70, 181, 161))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 181, 131))
        self.label_13.setStyleSheet(u"QFrame {\n"
"	    background: qlineargradient(x1:0.3, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgb(140, 125, 255), \n"
"                                stop:1 rgb(238, 196, 255));\n"
"	border-radius: 15px; /* \u8bbe\u7f6e\u5706\u89d2\u5927\u5c0f */\n"
"}")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 140, 91, 16))
        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(220, 70, 181, 161))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 0, 181, 131))
        self.label_14.setStyleSheet(u"QFrame {\n"
"	    background: qlineargradient(x1:0.3, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgb(255, 116, 69), \n"
"                                stop:1 rgb(255, 219, 198));\n"
"	border-radius: 15px; /* \u8bbe\u7f6e\u5706\u89d2\u5927\u5c0f */\n"
"}")
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 140, 91, 16))
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(420, 70, 181, 161))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 181, 131))
        self.label_15.setStyleSheet(u"QFrame {\n"
"		    background: qlineargradient(x1:0.3, y1:0, x2:1, y2:1,\n"
"                                stop:0 rgb(141, 255, 123), \n"
"                                stop:1 rgb(223, 255, 222));\n"
"	border-radius: 15px; /* \u8bbe\u7f6e\u5706\u89d2\u5927\u5c0f */\n"
"}")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 140, 91, 16))
        self.horizontalScrollBar = QScrollBar(self.frame_6)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(10, 310, 631, 16))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 171, 20))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.frame_7 = QFrame(self.Game_Frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 360, 321, 221))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_7)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 70, 281, 131))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setEnabled(True)
        self.label_17.setGeometry(QRect(10, 10, 111, 21))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_17.setFont(font1)
        self.widget_3 = QWidget(self.Game_Frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(349, 359, 331, 221))
        self.label_22 = QLabel(self.widget_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(True)
        self.label_22.setGeometry(QRect(0, 10, 111, 21))
        self.label_22.setFont(font1)
        self.frame_8 = QFrame(self.widget_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(40, 70, 281, 131))
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.main_frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 30, 321, 16))
        self.stackedWidget.addWidget(self.page)
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
        self.label.setText(QCoreApplication.translate("Form", u"\u5934\u50cf", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Your profile", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Add account", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Your workspace", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Sign out", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8bc4\u4f30", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u62a5\u544a", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"game_cover", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"game1_name", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"game_cover", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"game2_name", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"game_cover", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"game3_name", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Games", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3\u76ee\u6807", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3\u76ee\u6807", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"search", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3\u62a5\u544a", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u8bc4\u4f30\u62a5\u544a", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
    # retranslateUi

