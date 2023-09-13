# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_window_login(object):
    def setupUi(self, window_login):
        if not window_login.objectName():
            window_login.setObjectName(u"window_login")
        window_login.resize(372, 522)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window_login.sizePolicy().hasHeightForWidth())
        window_login.setSizePolicy(sizePolicy)
        window_login.setMaximumSize(QSize(372, 522))
        window_login.setStyleSheet(u"background-color: rgb(234, 245, 255);")
        self.fr_fundo_login = QFrame(window_login)
        self.fr_fundo_login.setObjectName(u"fr_fundo_login")
        self.fr_fundo_login.setGeometry(QRect(10, 10, 351, 501))
        sizePolicy.setHeightForWidth(self.fr_fundo_login.sizePolicy().hasHeightForWidth())
        self.fr_fundo_login.setSizePolicy(sizePolicy)
        self.fr_fundo_login.setStyleSheet(u"background-color: rgb(222, 241, 255);\n"
"border-radius: 5px;")
        self.fr_fundo_login.setFrameShape(QFrame.StyledPanel)
        self.fr_fundo_login.setFrameShadow(QFrame.Raised)
        self.edt_user_login = QLineEdit(self.fr_fundo_login)
        self.edt_user_login.setObjectName(u"edt_user_login")
        self.edt_user_login.setGeometry(QRect(20, 260, 311, 41))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(11)
        font.setBold(True)
        self.edt_user_login.setFont(font)
        self.edt_user_login.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(138, 185, 214);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"color: rgb(138, 185, 214);")
        self.edt_senha_login = QLineEdit(self.fr_fundo_login)
        self.edt_senha_login.setObjectName(u"edt_senha_login")
        self.edt_senha_login.setGeometry(QRect(20, 360, 311, 41))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(7)
        self.edt_senha_login.setFont(font1)
        self.edt_senha_login.setCursor(QCursor(Qt.IBeamCursor))
        self.edt_senha_login.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(138, 185, 214);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.edt_senha_login.setEchoMode(QLineEdit.Password)
        self.bt_entrar_login = QPushButton(self.fr_fundo_login)
        self.bt_entrar_login.setObjectName(u"bt_entrar_login")
        self.bt_entrar_login.setGeometry(QRect(230, 430, 101, 41))
        self.bt_entrar_login.setFont(font)
        self.bt_entrar_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_entrar_login.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.img_logo_login = QLabel(self.fr_fundo_login)
        self.img_logo_login.setObjectName(u"img_logo_login")
        self.img_logo_login.setGeometry(QRect(100, 20, 161, 181))
        self.img_logo_login.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(222, 241, 255);")
        self.img_logo_login.setPixmap(QPixmap(u"img/logoP.png"))
        self.lb_user_login = QLabel(window_login)
        self.lb_user_login.setObjectName(u"lb_user_login")
        self.lb_user_login.setGeometry(QRect(30, 230, 91, 31))
        self.lb_user_login.setFont(font)
        self.lb_user_login.setStyleSheet(u"background-color: rgb(222, 241, 255);")
        self.lb_senha_login = QLabel(window_login)
        self.lb_senha_login.setObjectName(u"lb_senha_login")
        self.lb_senha_login.setGeometry(QRect(30, 330, 91, 31))
        self.lb_senha_login.setFont(font)
        self.lb_senha_login.setStyleSheet(u"background-color: rgb(222, 241, 255);")
        QWidget.setTabOrder(self.edt_user_login, self.edt_senha_login)
        QWidget.setTabOrder(self.edt_senha_login, self.bt_entrar_login)

        self.retranslateUi(window_login)

        QMetaObject.connectSlotsByName(window_login)
    # setupUi

    def retranslateUi(self, window_login):
        window_login.setWindowTitle(QCoreApplication.translate("window_login", u"Sistema de Cadastro - Quatro Patas Hotel", None))
        self.bt_entrar_login.setText(QCoreApplication.translate("window_login", u"ENTRAR", None))
        self.img_logo_login.setText("")
        self.lb_user_login.setText(QCoreApplication.translate("window_login", u"USU\u00c1RIO:", None))
        self.lb_senha_login.setText(QCoreApplication.translate("window_login", u"SENHA:", None))
    # retranslateUi

