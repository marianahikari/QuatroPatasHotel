# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1563, 867)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(234, 245, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.telas = QStackedWidget(self.centralwidget)
        self.telas.setObjectName(u"telas")
        sizePolicy.setHeightForWidth(self.telas.sizePolicy().hasHeightForWidth())
        self.telas.setSizePolicy(sizePolicy)
        self.win_home = QWidget()
        self.win_home.setObjectName(u"win_home")
        self.gridLayout = QGridLayout(self.win_home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fr_gMenu_home = QHBoxLayout()
        self.fr_gMenu_home.setObjectName(u"fr_gMenu_home")
        self.fr_menu_home = QFrame(self.win_home)
        self.fr_menu_home.setObjectName(u"fr_menu_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_menu_home.sizePolicy().hasHeightForWidth())
        self.fr_menu_home.setSizePolicy(sizePolicy1)
        self.fr_menu_home.setMinimumSize(QSize(128, 201))
        self.fr_menu_home.setMaximumSize(QSize(128, 201))
        self.fr_menu_home.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.fr_menu_home.setFrameShape(QFrame.StyledPanel)
        self.fr_menu_home.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.fr_menu_home)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.bt_pets_home = QPushButton(self.fr_menu_home)
        self.bt_pets_home.setObjectName(u"bt_pets_home")
        sizePolicy1.setHeightForWidth(self.bt_pets_home.sizePolicy().hasHeightForWidth())
        self.bt_pets_home.setSizePolicy(sizePolicy1)
        self.bt_pets_home.setMinimumSize(QSize(110, 28))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.bt_pets_home.setFont(font)
        self.bt_pets_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pets_home.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_3.addWidget(self.bt_pets_home, 3, 0, 1, 1)

        self.bt_sair_home = QPushButton(self.fr_menu_home)
        self.bt_sair_home.setObjectName(u"bt_sair_home")
        self.bt_sair_home.setMinimumSize(QSize(80, 28))
        self.bt_sair_home.setFont(font)
        self.bt_sair_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_sair_home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"}")
        icon = QIcon()
        icon.addFile(u"img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_sair_home.setIcon(icon)
        self.bt_sair_home.setIconSize(QSize(15, 15))

        self.gridLayout_3.addWidget(self.bt_sair_home, 7, 0, 1, 1)

        self.bt_home_home = QPushButton(self.fr_menu_home)
        self.bt_home_home.setObjectName(u"bt_home_home")
        sizePolicy1.setHeightForWidth(self.bt_home_home.sizePolicy().hasHeightForWidth())
        self.bt_home_home.setSizePolicy(sizePolicy1)
        self.bt_home_home.setMinimumSize(QSize(110, 28))
        self.bt_home_home.setFont(font)
        self.bt_home_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_home_home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.bt_home_home, 2, 0, 1, 1)

        self.sp_menu_home = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.sp_menu_home, 6, 0, 1, 1)

        self.lb_menu_home = QLabel(self.fr_menu_home)
        self.lb_menu_home.setObjectName(u"lb_menu_home")
        sizePolicy1.setHeightForWidth(self.lb_menu_home.sizePolicy().hasHeightForWidth())
        self.lb_menu_home.setSizePolicy(sizePolicy1)
        self.lb_menu_home.setMinimumSize(QSize(110, 35))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.lb_menu_home.setFont(font1)
        self.lb_menu_home.setStyleSheet(u"")
        self.lb_menu_home.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_menu_home, 1, 0, 1, 1)

        self.bt_usuarios_home = QPushButton(self.fr_menu_home)
        self.bt_usuarios_home.setObjectName(u"bt_usuarios_home")
        sizePolicy1.setHeightForWidth(self.bt_usuarios_home.sizePolicy().hasHeightForWidth())
        self.bt_usuarios_home.setSizePolicy(sizePolicy1)
        self.bt_usuarios_home.setMinimumSize(QSize(110, 28))
        self.bt_usuarios_home.setFont(font)
        self.bt_usuarios_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_usuarios_home.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_3.addWidget(self.bt_usuarios_home, 5, 0, 1, 1)


        self.fr_gMenu_home.addWidget(self.fr_menu_home)

        self.fr_sp_menu_home = QFrame(self.win_home)
        self.fr_sp_menu_home.setObjectName(u"fr_sp_menu_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fr_sp_menu_home.sizePolicy().hasHeightForWidth())
        self.fr_sp_menu_home.setSizePolicy(sizePolicy2)
        self.fr_sp_menu_home.setFrameShape(QFrame.StyledPanel)
        self.fr_sp_menu_home.setFrameShadow(QFrame.Raised)

        self.fr_gMenu_home.addWidget(self.fr_sp_menu_home)


        self.gridLayout.addLayout(self.fr_gMenu_home, 1, 0, 1, 1)

        self.sp_supDir_home = QSpacerItem(20, 79, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.sp_supDir_home, 1, 3, 1, 1)

        self.sp_esq_home = QSpacerItem(310, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.sp_esq_home, 3, 0, 1, 1)

        self.fr_titulo_home = QWidget(self.win_home)
        self.fr_titulo_home.setObjectName(u"fr_titulo_home")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fr_titulo_home.sizePolicy().hasHeightForWidth())
        self.fr_titulo_home.setSizePolicy(sizePolicy3)
        self.fr_titulo_home.setMinimumSize(QSize(0, 70))
        self.fr_titulo_home.setMaximumSize(QSize(16777215, 70))
        self.fr_titulo_home.setStyleSheet(u"background-color: rgb(213, 213, 213);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.fr_titulo_home)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.img_titulo_home = QLabel(self.fr_titulo_home)
        self.img_titulo_home.setObjectName(u"img_titulo_home")
        sizePolicy1.setHeightForWidth(self.img_titulo_home.sizePolicy().hasHeightForWidth())
        self.img_titulo_home.setSizePolicy(sizePolicy1)
        self.img_titulo_home.setPixmap(QPixmap(u"img/home.png"))

        self.horizontalLayout_11.addWidget(self.img_titulo_home)

        self.lb_titulo_home = QLabel(self.fr_titulo_home)
        self.lb_titulo_home.setObjectName(u"lb_titulo_home")
        self.lb_titulo_home.setMinimumSize(QSize(0, 50))
        self.lb_titulo_home.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setPointSize(28)
        font2.setBold(True)
        self.lb_titulo_home.setFont(font2)

        self.horizontalLayout_11.addWidget(self.lb_titulo_home)

        self.sp_titulo_home = QSpacerItem(1274, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.sp_titulo_home)


        self.gridLayout.addWidget(self.fr_titulo_home, 0, 0, 1, 4)

        self.sp_esqMenu_home = QSpacerItem(309, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.sp_esqMenu_home, 3, 3, 1, 1)

        self.sp_infEsq_home = QSpacerItem(20, 79, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.sp_infEsq_home, 4, 0, 1, 1)

        self.bt_sobre_home = QPushButton(self.win_home)
        self.bt_sobre_home.setObjectName(u"bt_sobre_home")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bt_sobre_home.sizePolicy().hasHeightForWidth())
        self.bt_sobre_home.setSizePolicy(sizePolicy4)
        self.bt_sobre_home.setMinimumSize(QSize(65, 23))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.bt_sobre_home.setFont(font3)
        self.bt_sobre_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_sobre_home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.bt_sobre_home, 5, 0, 1, 4)

        self.sp_infMeio_home = QSpacerItem(20, 79, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.sp_infMeio_home, 4, 1, 1, 1)

        self.img_logo_menu = QLabel(self.win_home)
        self.img_logo_menu.setObjectName(u"img_logo_menu")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.img_logo_menu.sizePolicy().hasHeightForWidth())
        self.img_logo_menu.setSizePolicy(sizePolicy5)
        self.img_logo_menu.setMinimumSize(QSize(900, 0))
        self.img_logo_menu.setMaximumSize(QSize(900, 16777215))
        self.img_logo_menu.setPixmap(QPixmap(u"img/logoG.png"))
        self.img_logo_menu.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.img_logo_menu, 3, 1, 1, 2)

        self.sp_supMeio_home = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.sp_supMeio_home, 1, 2, 1, 1)

        self.sp_infDir_home = QSpacerItem(20, 79, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.sp_infDir_home, 4, 3, 1, 1)

        self.telas.addWidget(self.win_home)
        self.win_cadPet = QWidget()
        self.win_cadPet.setObjectName(u"win_cadPet")
        self.gridLayout_6 = QGridLayout(self.win_cadPet)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.fr_titulo_cadPet = QFrame(self.win_cadPet)
        self.fr_titulo_cadPet.setObjectName(u"fr_titulo_cadPet")
        self.fr_titulo_cadPet.setMinimumSize(QSize(0, 70))
        self.fr_titulo_cadPet.setMaximumSize(QSize(16777215, 70))
        self.fr_titulo_cadPet.setStyleSheet(u"background-color: rgb(213, 213, 213);\n"
"border-radius:5px;\n"
"")
        self.fr_titulo_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_titulo_cadPet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.fr_titulo_cadPet)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.img_titulo_cadPet = QLabel(self.fr_titulo_cadPet)
        self.img_titulo_cadPet.setObjectName(u"img_titulo_cadPet")
        sizePolicy1.setHeightForWidth(self.img_titulo_cadPet.sizePolicy().hasHeightForWidth())
        self.img_titulo_cadPet.setSizePolicy(sizePolicy1)
        self.img_titulo_cadPet.setPixmap(QPixmap(u"img/pata.png"))

        self.horizontalLayout_9.addWidget(self.img_titulo_cadPet)

        self.lb_titulo_cadPet = QLabel(self.fr_titulo_cadPet)
        self.lb_titulo_cadPet.setObjectName(u"lb_titulo_cadPet")
        self.lb_titulo_cadPet.setMinimumSize(QSize(0, 50))
        self.lb_titulo_cadPet.setMaximumSize(QSize(16777215, 50))
        self.lb_titulo_cadPet.setFont(font2)

        self.horizontalLayout_9.addWidget(self.lb_titulo_cadPet)


        self.gridLayout_6.addWidget(self.fr_titulo_cadPet, 0, 0, 1, 2)

        self.div_meio_cadPet = QFrame(self.win_cadPet)
        self.div_meio_cadPet.setObjectName(u"div_meio_cadPet")
        self.div_meio_cadPet.setStyleSheet(u"")
        self.div_meio_cadPet.setFrameShape(QFrame.HLine)
        self.div_meio_cadPet.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.div_meio_cadPet, 7, 0, 1, 2)

        self.fr_botoes_cadPet = QFrame(self.win_cadPet)
        self.fr_botoes_cadPet.setObjectName(u"fr_botoes_cadPet")
        sizePolicy4.setHeightForWidth(self.fr_botoes_cadPet.sizePolicy().hasHeightForWidth())
        self.fr_botoes_cadPet.setSizePolicy(sizePolicy4)
        self.fr_botoes_cadPet.setMinimumSize(QSize(0, 60))
        self.fr_botoes_cadPet.setMaximumSize(QSize(16777215, 60))
        self.fr_botoes_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_botoes_cadPet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_botoes_cadPet)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_aviso_cadPet = QLabel(self.fr_botoes_cadPet)
        self.lb_aviso_cadPet.setObjectName(u"lb_aviso_cadPet")
        self.lb_aviso_cadPet.setStyleSheet(u"color: rgb(138, 185, 214);")

        self.horizontalLayout_2.addWidget(self.lb_aviso_cadPet)

        self.sp_supBt_cadPet = QSpacerItem(1097, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.sp_supBt_cadPet)

        self.bt_salvar_cadPet = QPushButton(self.fr_botoes_cadPet)
        self.bt_salvar_cadPet.setObjectName(u"bt_salvar_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_salvar_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_salvar_cadPet.setSizePolicy(sizePolicy1)
        self.bt_salvar_cadPet.setMinimumSize(QSize(130, 28))
        self.bt_salvar_cadPet.setFont(font)
        self.bt_salvar_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_salvar_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"img/salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_salvar_cadPet.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.bt_salvar_cadPet)

        self.bt_cancelar_cadPet = QPushButton(self.fr_botoes_cadPet)
        self.bt_cancelar_cadPet.setObjectName(u"bt_cancelar_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_cancelar_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_cancelar_cadPet.setSizePolicy(sizePolicy1)
        self.bt_cancelar_cadPet.setMinimumSize(QSize(130, 28))
        self.bt_cancelar_cadPet.setFont(font)
        self.bt_cancelar_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cancelar_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"img/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cancelar_cadPet.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.bt_cancelar_cadPet)

        self.bt_cad_cadPet = QPushButton(self.fr_botoes_cadPet)
        self.bt_cad_cadPet.setObjectName(u"bt_cad_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_cad_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_cad_cadPet.setSizePolicy(sizePolicy1)
        self.bt_cad_cadPet.setMinimumSize(QSize(130, 28))
        self.bt_cad_cadPet.setFont(font)
        self.bt_cad_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cad_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"img/cadastrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cad_cadPet.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.bt_cad_cadPet)


        self.gridLayout_6.addWidget(self.fr_botoes_cadPet, 6, 0, 1, 2)

        self.fr_cad2_cadPet = QFrame(self.win_cadPet)
        self.fr_cad2_cadPet.setObjectName(u"fr_cad2_cadPet")
        sizePolicy3.setHeightForWidth(self.fr_cad2_cadPet.sizePolicy().hasHeightForWidth())
        self.fr_cad2_cadPet.setSizePolicy(sizePolicy3)
        self.fr_cad2_cadPet.setMinimumSize(QSize(0, 60))
        self.fr_cad2_cadPet.setMaximumSize(QSize(16777215, 60))
        self.fr_cad2_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_cad2_cadPet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.fr_cad2_cadPet)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lb_peso_cadPet = QLabel(self.fr_cad2_cadPet)
        self.lb_peso_cadPet.setObjectName(u"lb_peso_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_peso_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_peso_cadPet.setSizePolicy(sizePolicy1)
        self.lb_peso_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_peso_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_peso_cadPet.setFont(font)

        self.horizontalLayout_17.addWidget(self.lb_peso_cadPet)

        self.box_peso_cadPet = QComboBox(self.fr_cad2_cadPet)
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.addItem("")
        self.box_peso_cadPet.setObjectName(u"box_peso_cadPet")
        sizePolicy4.setHeightForWidth(self.box_peso_cadPet.sizePolicy().hasHeightForWidth())
        self.box_peso_cadPet.setSizePolicy(sizePolicy4)
        self.box_peso_cadPet.setMinimumSize(QSize(0, 31))
        self.box_peso_cadPet.setMaximumSize(QSize(16777215, 31))
        self.box_peso_cadPet.setFont(font)
        self.box_peso_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_17.addWidget(self.box_peso_cadPet)

        self.sp2_cad2_cadPet_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.sp2_cad2_cadPet_2)

        self.lb_sexo_cadPet = QLabel(self.fr_cad2_cadPet)
        self.lb_sexo_cadPet.setObjectName(u"lb_sexo_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_sexo_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_sexo_cadPet.setSizePolicy(sizePolicy1)
        self.lb_sexo_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_sexo_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_sexo_cadPet.setFont(font)

        self.horizontalLayout_17.addWidget(self.lb_sexo_cadPet)

        self.box_sexo_cadPet = QComboBox(self.fr_cad2_cadPet)
        self.box_sexo_cadPet.addItem("")
        self.box_sexo_cadPet.addItem("")
        self.box_sexo_cadPet.setObjectName(u"box_sexo_cadPet")
        sizePolicy4.setHeightForWidth(self.box_sexo_cadPet.sizePolicy().hasHeightForWidth())
        self.box_sexo_cadPet.setSizePolicy(sizePolicy4)
        self.box_sexo_cadPet.setMinimumSize(QSize(0, 31))
        self.box_sexo_cadPet.setMaximumSize(QSize(16777215, 31))
        self.box_sexo_cadPet.setFont(font)
        self.box_sexo_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_17.addWidget(self.box_sexo_cadPet)

        self.sp1_cad2_cadPet = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.sp1_cad2_cadPet)

        self.lb_idade_cadPet = QLabel(self.fr_cad2_cadPet)
        self.lb_idade_cadPet.setObjectName(u"lb_idade_cadPet")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(25)
        sizePolicy6.setHeightForWidth(self.lb_idade_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_idade_cadPet.setSizePolicy(sizePolicy6)
        self.lb_idade_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_idade_cadPet.setFont(font)

        self.horizontalLayout_17.addWidget(self.lb_idade_cadPet)

        self.box_idade_cadPet = QComboBox(self.fr_cad2_cadPet)
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.addItem("")
        self.box_idade_cadPet.setObjectName(u"box_idade_cadPet")
        sizePolicy4.setHeightForWidth(self.box_idade_cadPet.sizePolicy().hasHeightForWidth())
        self.box_idade_cadPet.setSizePolicy(sizePolicy4)
        self.box_idade_cadPet.setMinimumSize(QSize(0, 31))
        self.box_idade_cadPet.setMaximumSize(QSize(16777215, 31))
        self.box_idade_cadPet.setFont(font)
        self.box_idade_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_17.addWidget(self.box_idade_cadPet)


        self.gridLayout_6.addWidget(self.fr_cad2_cadPet, 2, 1, 1, 1)

        self.fr_cad5_cadPet = QFrame(self.win_cadPet)
        self.fr_cad5_cadPet.setObjectName(u"fr_cad5_cadPet")
        self.fr_cad5_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_cad5_cadPet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.fr_cad5_cadPet)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_nomeEmerg_cadPet = QLabel(self.fr_cad5_cadPet)
        self.lb_nomeEmerg_cadPet.setObjectName(u"lb_nomeEmerg_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_nomeEmerg_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_nomeEmerg_cadPet.setSizePolicy(sizePolicy1)
        self.lb_nomeEmerg_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_nomeEmerg_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_nomeEmerg_cadPet.setFont(font)

        self.horizontalLayout_14.addWidget(self.lb_nomeEmerg_cadPet)

        self.edt_nomeEmerg_cadPet = QLineEdit(self.fr_cad5_cadPet)
        self.edt_nomeEmerg_cadPet.setObjectName(u"edt_nomeEmerg_cadPet")
        self.edt_nomeEmerg_cadPet.setMinimumSize(QSize(0, 31))
        self.edt_nomeEmerg_cadPet.setMaximumSize(QSize(16777215, 31))
        self.edt_nomeEmerg_cadPet.setFont(font)
        self.edt_nomeEmerg_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_14.addWidget(self.edt_nomeEmerg_cadPet)

        self.sp_cad5_cadPet = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.sp_cad5_cadPet)

        self.lb_telEmerg_cadPet = QLabel(self.fr_cad5_cadPet)
        self.lb_telEmerg_cadPet.setObjectName(u"lb_telEmerg_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_telEmerg_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_telEmerg_cadPet.setSizePolicy(sizePolicy1)
        self.lb_telEmerg_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_telEmerg_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_telEmerg_cadPet.setFont(font)

        self.horizontalLayout_14.addWidget(self.lb_telEmerg_cadPet)

        self.edt_telEmerg_cadPet = QLineEdit(self.fr_cad5_cadPet)
        self.edt_telEmerg_cadPet.setObjectName(u"edt_telEmerg_cadPet")
        self.edt_telEmerg_cadPet.setMinimumSize(QSize(0, 31))
        self.edt_telEmerg_cadPet.setMaximumSize(QSize(16777215, 31))
        self.edt_telEmerg_cadPet.setFont(font)
        self.edt_telEmerg_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_14.addWidget(self.edt_telEmerg_cadPet)


        self.gridLayout_6.addWidget(self.fr_cad5_cadPet, 5, 0, 1, 2)

        self.fr_cad3_cadPet = QFrame(self.win_cadPet)
        self.fr_cad3_cadPet.setObjectName(u"fr_cad3_cadPet")
        self.fr_cad3_cadPet.setMinimumSize(QSize(0, 57))
        self.fr_cad3_cadPet.setMaximumSize(QSize(16777215, 57))
        self.fr_cad3_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_cad3_cadPet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.fr_cad3_cadPet)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lb_obs_CadPet = QLabel(self.fr_cad3_cadPet)
        self.lb_obs_CadPet.setObjectName(u"lb_obs_CadPet")
        sizePolicy6.setHeightForWidth(self.lb_obs_CadPet.sizePolicy().hasHeightForWidth())
        self.lb_obs_CadPet.setSizePolicy(sizePolicy6)
        self.lb_obs_CadPet.setMinimumSize(QSize(0, 25))
        self.lb_obs_CadPet.setFont(font)

        self.horizontalLayout_13.addWidget(self.lb_obs_CadPet)

        self.edt_obs_cadPet = QTextEdit(self.fr_cad3_cadPet)
        self.edt_obs_cadPet.setObjectName(u"edt_obs_cadPet")
        self.edt_obs_cadPet.setMinimumSize(QSize(0, 31))
        self.edt_obs_cadPet.setMaximumSize(QSize(16777215, 31))
        self.edt_obs_cadPet.setFont(font)
        self.edt_obs_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_13.addWidget(self.edt_obs_cadPet)

        self.sp2_cad2_cadPet = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.sp2_cad2_cadPet)

        self.lb_end_cadPet = QLabel(self.fr_cad3_cadPet)
        self.lb_end_cadPet.setObjectName(u"lb_end_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_end_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_end_cadPet.setSizePolicy(sizePolicy1)
        self.lb_end_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_end_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_end_cadPet.setFont(font)

        self.horizontalLayout_13.addWidget(self.lb_end_cadPet)

        self.edt_end_cadPet = QLineEdit(self.fr_cad3_cadPet)
        self.edt_end_cadPet.setObjectName(u"edt_end_cadPet")
        self.edt_end_cadPet.setMinimumSize(QSize(0, 31))
        self.edt_end_cadPet.setMaximumSize(QSize(16777215, 31))
        self.edt_end_cadPet.setFont(font)
        self.edt_end_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_13.addWidget(self.edt_end_cadPet)


        self.gridLayout_6.addWidget(self.fr_cad3_cadPet, 3, 1, 1, 1)

        self.fr_cad4_cadPet = QFrame(self.win_cadPet)
        self.fr_cad4_cadPet.setObjectName(u"fr_cad4_cadPet")
        self.fr_cad4_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_cad4_cadPet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_cad4_cadPet)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_nomeTutor_cadPet = QLabel(self.fr_cad4_cadPet)
        self.lb_nomeTutor_cadPet.setObjectName(u"lb_nomeTutor_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_nomeTutor_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_nomeTutor_cadPet.setSizePolicy(sizePolicy1)
        self.lb_nomeTutor_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_nomeTutor_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_nomeTutor_cadPet.setFont(font)

        self.horizontalLayout.addWidget(self.lb_nomeTutor_cadPet)

        self.edt_nomeTutor_cadPet = QLineEdit(self.fr_cad4_cadPet)
        self.edt_nomeTutor_cadPet.setObjectName(u"edt_nomeTutor_cadPet")
        self.edt_nomeTutor_cadPet.setMinimumSize(QSize(0, 31))
        self.edt_nomeTutor_cadPet.setMaximumSize(QSize(16777215, 31))
        self.edt_nomeTutor_cadPet.setFont(font)
        self.edt_nomeTutor_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout.addWidget(self.edt_nomeTutor_cadPet)

        self.sp1_cad4_cadPet = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.sp1_cad4_cadPet)

        self.lb_tel_cadPet = QLabel(self.fr_cad4_cadPet)
        self.lb_tel_cadPet.setObjectName(u"lb_tel_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_tel_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_tel_cadPet.setSizePolicy(sizePolicy1)
        self.lb_tel_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_tel_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_tel_cadPet.setFont(font)

        self.horizontalLayout.addWidget(self.lb_tel_cadPet)

        self.edt_telTutor_cadPet = QLineEdit(self.fr_cad4_cadPet)
        self.edt_telTutor_cadPet.setObjectName(u"edt_telTutor_cadPet")
        self.edt_telTutor_cadPet.setMinimumSize(QSize(0, 31))
        self.edt_telTutor_cadPet.setMaximumSize(QSize(16777215, 31))
        self.edt_telTutor_cadPet.setFont(font)
        self.edt_telTutor_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout.addWidget(self.edt_telTutor_cadPet)

        self.sp2_cad4_cadPet = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.sp2_cad4_cadPet)

        self.lb_email_cadPet = QLabel(self.fr_cad4_cadPet)
        self.lb_email_cadPet.setObjectName(u"lb_email_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_email_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_email_cadPet.setSizePolicy(sizePolicy1)
        self.lb_email_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_email_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_email_cadPet.setFont(font)

        self.horizontalLayout.addWidget(self.lb_email_cadPet)

        self.edt_email_cadPet = QLineEdit(self.fr_cad4_cadPet)
        self.edt_email_cadPet.setObjectName(u"edt_email_cadPet")
        self.edt_email_cadPet.setMinimumSize(QSize(0, 31))
        self.edt_email_cadPet.setMaximumSize(QSize(16777215, 31))
        self.edt_email_cadPet.setFont(font)
        self.edt_email_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout.addWidget(self.edt_email_cadPet)


        self.gridLayout_6.addWidget(self.fr_cad4_cadPet, 4, 0, 1, 2)

        self.fr_cad1_cadPet = QFrame(self.win_cadPet)
        self.fr_cad1_cadPet.setObjectName(u"fr_cad1_cadPet")
        self.fr_cad1_cadPet.setMinimumSize(QSize(0, 57))
        self.fr_cad1_cadPet.setMaximumSize(QSize(16777215, 57))
        self.fr_cad1_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_cad1_cadPet.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.fr_cad1_cadPet)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lb_nomePet_cadPet = QLabel(self.fr_cad1_cadPet)
        self.lb_nomePet_cadPet.setObjectName(u"lb_nomePet_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_nomePet_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_nomePet_cadPet.setSizePolicy(sizePolicy1)
        self.lb_nomePet_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_nomePet_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_nomePet_cadPet.setFont(font)

        self.gridLayout_8.addWidget(self.lb_nomePet_cadPet, 0, 0, 1, 1)

        self.edt_nomePet_cadPet = QLineEdit(self.fr_cad1_cadPet)
        self.edt_nomePet_cadPet.setObjectName(u"edt_nomePet_cadPet")
        self.edt_nomePet_cadPet.setMinimumSize(QSize(0, 31))
        self.edt_nomePet_cadPet.setMaximumSize(QSize(16777215, 31))
        self.edt_nomePet_cadPet.setFont(font)
        self.edt_nomePet_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.gridLayout_8.addWidget(self.edt_nomePet_cadPet, 0, 1, 1, 1)

        self.sp1_cad1_cadPet = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.sp1_cad1_cadPet, 0, 2, 1, 1)

        self.lb_raca_cadPet = QLabel(self.fr_cad1_cadPet)
        self.lb_raca_cadPet.setObjectName(u"lb_raca_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_raca_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_raca_cadPet.setSizePolicy(sizePolicy1)
        self.lb_raca_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_raca_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_raca_cadPet.setFont(font)

        self.gridLayout_8.addWidget(self.lb_raca_cadPet, 0, 3, 1, 1)

        self.box_raca_cadPet = QComboBox(self.fr_cad1_cadPet)
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.addItem("")
        self.box_raca_cadPet.setObjectName(u"box_raca_cadPet")
        sizePolicy4.setHeightForWidth(self.box_raca_cadPet.sizePolicy().hasHeightForWidth())
        self.box_raca_cadPet.setSizePolicy(sizePolicy4)
        self.box_raca_cadPet.setMinimumSize(QSize(50, 31))
        self.box_raca_cadPet.setMaximumSize(QSize(16777215, 31))
        self.box_raca_cadPet.setFont(font)
        self.box_raca_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.gridLayout_8.addWidget(self.box_raca_cadPet, 0, 4, 1, 1)

        self.sp2_cad1_cadPet = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.sp2_cad1_cadPet, 0, 5, 1, 1)

        self.lb_Cor_cadPet = QLabel(self.fr_cad1_cadPet)
        self.lb_Cor_cadPet.setObjectName(u"lb_Cor_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_Cor_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_Cor_cadPet.setSizePolicy(sizePolicy1)
        self.lb_Cor_cadPet.setMinimumSize(QSize(0, 25))
        self.lb_Cor_cadPet.setMaximumSize(QSize(16777215, 25))
        self.lb_Cor_cadPet.setFont(font)

        self.gridLayout_8.addWidget(self.lb_Cor_cadPet, 0, 6, 1, 1)

        self.box_cor_cadPet = QComboBox(self.fr_cad1_cadPet)
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.addItem("")
        self.box_cor_cadPet.setObjectName(u"box_cor_cadPet")
        sizePolicy4.setHeightForWidth(self.box_cor_cadPet.sizePolicy().hasHeightForWidth())
        self.box_cor_cadPet.setSizePolicy(sizePolicy4)
        self.box_cor_cadPet.setMinimumSize(QSize(50, 31))
        self.box_cor_cadPet.setMaximumSize(QSize(16777215, 31))
        self.box_cor_cadPet.setFont(font)
        self.box_cor_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.gridLayout_8.addWidget(self.box_cor_cadPet, 0, 7, 1, 1)


        self.gridLayout_6.addWidget(self.fr_cad1_cadPet, 1, 1, 1, 1)

        self.fr_menu_cadPet = QFrame(self.win_cadPet)
        self.fr_menu_cadPet.setObjectName(u"fr_menu_cadPet")
        sizePolicy1.setHeightForWidth(self.fr_menu_cadPet.sizePolicy().hasHeightForWidth())
        self.fr_menu_cadPet.setSizePolicy(sizePolicy1)
        self.fr_menu_cadPet.setMinimumSize(QSize(128, 201))
        self.fr_menu_cadPet.setMaximumSize(QSize(128, 201))
        self.fr_menu_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.fr_menu_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_menu_cadPet.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.fr_menu_cadPet)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.bt_home_cadPet = QPushButton(self.fr_menu_cadPet)
        self.bt_home_cadPet.setObjectName(u"bt_home_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_home_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_home_cadPet.setSizePolicy(sizePolicy1)
        self.bt_home_cadPet.setMinimumSize(QSize(110, 28))
        self.bt_home_cadPet.setFont(font)
        self.bt_home_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_home_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_16.addWidget(self.bt_home_cadPet, 2, 0, 1, 1)

        self.bt_pets_cadPet = QPushButton(self.fr_menu_cadPet)
        self.bt_pets_cadPet.setObjectName(u"bt_pets_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_pets_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_pets_cadPet.setSizePolicy(sizePolicy1)
        self.bt_pets_cadPet.setMinimumSize(QSize(110, 28))
        self.bt_pets_cadPet.setFont(font)
        self.bt_pets_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pets_cadPet.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_16.addWidget(self.bt_pets_cadPet, 3, 0, 1, 1)

        self.bt_sair_cadPet = QPushButton(self.fr_menu_cadPet)
        self.bt_sair_cadPet.setObjectName(u"bt_sair_cadPet")
        self.bt_sair_cadPet.setMinimumSize(QSize(80, 28))
        self.bt_sair_cadPet.setFont(font)
        self.bt_sair_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_sair_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"}")
        self.bt_sair_cadPet.setIcon(icon)
        self.bt_sair_cadPet.setIconSize(QSize(15, 15))

        self.gridLayout_16.addWidget(self.bt_sair_cadPet, 7, 0, 1, 1)

        self.lb_menu_cadPet = QLabel(self.fr_menu_cadPet)
        self.lb_menu_cadPet.setObjectName(u"lb_menu_cadPet")
        sizePolicy1.setHeightForWidth(self.lb_menu_cadPet.sizePolicy().hasHeightForWidth())
        self.lb_menu_cadPet.setSizePolicy(sizePolicy1)
        self.lb_menu_cadPet.setMinimumSize(QSize(110, 35))
        self.lb_menu_cadPet.setFont(font1)
        self.lb_menu_cadPet.setStyleSheet(u"")
        self.lb_menu_cadPet.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.lb_menu_cadPet, 1, 0, 1, 1)

        self.sp_menu_cadPet = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.sp_menu_cadPet, 5, 0, 1, 1)

        self.bt_usuarios_cadPet = QPushButton(self.fr_menu_cadPet)
        self.bt_usuarios_cadPet.setObjectName(u"bt_usuarios_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_usuarios_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_usuarios_cadPet.setSizePolicy(sizePolicy1)
        self.bt_usuarios_cadPet.setMinimumSize(QSize(110, 28))
        self.bt_usuarios_cadPet.setFont(font)
        self.bt_usuarios_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_usuarios_cadPet.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_16.addWidget(self.bt_usuarios_cadPet, 4, 0, 1, 1)


        self.gridLayout_6.addWidget(self.fr_menu_cadPet, 1, 0, 3, 1)

        self.fr_tabCad_cadPet = QFrame(self.win_cadPet)
        self.fr_tabCad_cadPet.setObjectName(u"fr_tabCad_cadPet")
        self.fr_tabCad_cadPet.setFrameShape(QFrame.StyledPanel)
        self.fr_tabCad_cadPet.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.fr_tabCad_cadPet)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.img_lupa_cadPet = QLabel(self.fr_tabCad_cadPet)
        self.img_lupa_cadPet.setObjectName(u"img_lupa_cadPet")
        sizePolicy1.setHeightForWidth(self.img_lupa_cadPet.sizePolicy().hasHeightForWidth())
        self.img_lupa_cadPet.setSizePolicy(sizePolicy1)
        self.img_lupa_cadPet.setMinimumSize(QSize(0, 25))
        self.img_lupa_cadPet.setMaximumSize(QSize(16777215, 25))
        self.img_lupa_cadPet.setFont(font)
        self.img_lupa_cadPet.setPixmap(QPixmap(u"img/lupa.png"))

        self.gridLayout_4.addWidget(self.img_lupa_cadPet, 0, 2, 1, 1)

        self.edt_filtro_cadPet = QLineEdit(self.fr_tabCad_cadPet)
        self.edt_filtro_cadPet.setObjectName(u"edt_filtro_cadPet")
        sizePolicy1.setHeightForWidth(self.edt_filtro_cadPet.sizePolicy().hasHeightForWidth())
        self.edt_filtro_cadPet.setSizePolicy(sizePolicy1)
        self.edt_filtro_cadPet.setMinimumSize(QSize(405, 28))
        self.edt_filtro_cadPet.setMaximumSize(QSize(16777215, 28))
        self.edt_filtro_cadPet.setFont(font)
        self.edt_filtro_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.gridLayout_4.addWidget(self.edt_filtro_cadPet, 0, 3, 1, 3)

        self.bt_excel_cadPet = QPushButton(self.fr_tabCad_cadPet)
        self.bt_excel_cadPet.setObjectName(u"bt_excel_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_excel_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_excel_cadPet.setSizePolicy(sizePolicy1)
        self.bt_excel_cadPet.setMinimumSize(QSize(130, 28))
        self.bt_excel_cadPet.setMaximumSize(QSize(130, 16777215))
        self.bt_excel_cadPet.setFont(font)
        self.bt_excel_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_excel_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"img/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_excel_cadPet.setIcon(icon4)

        self.gridLayout_4.addWidget(self.bt_excel_cadPet, 2, 0, 1, 1)

        self.bt_pdf_cadPet = QPushButton(self.fr_tabCad_cadPet)
        self.bt_pdf_cadPet.setObjectName(u"bt_pdf_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_pdf_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_pdf_cadPet.setSizePolicy(sizePolicy1)
        self.bt_pdf_cadPet.setMinimumSize(QSize(130, 28))
        self.bt_pdf_cadPet.setMaximumSize(QSize(30, 16777215))
        self.bt_pdf_cadPet.setFont(font)
        self.bt_pdf_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pdf_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"img/iconPDF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_pdf_cadPet.setIcon(icon5)
        self.bt_pdf_cadPet.setIconSize(QSize(50, 20))

        self.gridLayout_4.addWidget(self.bt_pdf_cadPet, 2, 3, 1, 1)

        self.sp_infTab_cadPet = QSpacerItem(1333, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.sp_infTab_cadPet, 2, 1, 1, 2)

        self.bt_remover_cadPet = QPushButton(self.fr_tabCad_cadPet)
        self.bt_remover_cadPet.setObjectName(u"bt_remover_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_remover_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_remover_cadPet.setSizePolicy(sizePolicy1)
        self.bt_remover_cadPet.setMinimumSize(QSize(130, 28))
        self.bt_remover_cadPet.setFont(font)
        self.bt_remover_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_remover_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"img/remover.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_remover_cadPet.setIcon(icon6)

        self.gridLayout_4.addWidget(self.bt_remover_cadPet, 2, 5, 1, 1)

        self.sp_supTab_cadPet = QSpacerItem(1248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.sp_supTab_cadPet, 0, 1, 1, 1)

        self.lb_tituloTab_cadPet = QLabel(self.fr_tabCad_cadPet)
        self.lb_tituloTab_cadPet.setObjectName(u"lb_tituloTab_cadPet")
        self.lb_tituloTab_cadPet.setFont(font1)

        self.gridLayout_4.addWidget(self.lb_tituloTab_cadPet, 0, 0, 1, 1)

        self.tab_cadPet = QTableView(self.fr_tabCad_cadPet)
        self.tab_cadPet.setObjectName(u"tab_cadPet")
        self.tab_cadPet.setFont(font)
        self.tab_cadPet.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"QTableView::item:selected {\n"
"   \n"
"	background-color: rgb(192, 226, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.tab_cadPet, 1, 0, 1, 6)

        self.bt_edit_cadPet = QPushButton(self.fr_tabCad_cadPet)
        self.bt_edit_cadPet.setObjectName(u"bt_edit_cadPet")
        sizePolicy1.setHeightForWidth(self.bt_edit_cadPet.sizePolicy().hasHeightForWidth())
        self.bt_edit_cadPet.setSizePolicy(sizePolicy1)
        self.bt_edit_cadPet.setMinimumSize(QSize(130, 28))
        self.bt_edit_cadPet.setFont(font)
        self.bt_edit_cadPet.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_edit_cadPet.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"img/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_edit_cadPet.setIcon(icon7)

        self.gridLayout_4.addWidget(self.bt_edit_cadPet, 2, 4, 1, 1)


        self.gridLayout_6.addWidget(self.fr_tabCad_cadPet, 8, 0, 1, 2)

        self.telas.addWidget(self.win_cadPet)
        self.win_sobre = QWidget()
        self.win_sobre.setObjectName(u"win_sobre")
        self.verticalLayout = QVBoxLayout(self.win_sobre)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_titulo_sobre = QWidget(self.win_sobre)
        self.fr_titulo_sobre.setObjectName(u"fr_titulo_sobre")
        self.fr_titulo_sobre.setMinimumSize(QSize(0, 70))
        self.fr_titulo_sobre.setMaximumSize(QSize(16777215, 70))
        self.fr_titulo_sobre.setStyleSheet(u"background-color: rgb(213, 213, 213);\n"
"border-radius:5px;\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.fr_titulo_sobre)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.img_titulo_sobre = QLabel(self.fr_titulo_sobre)
        self.img_titulo_sobre.setObjectName(u"img_titulo_sobre")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.img_titulo_sobre.sizePolicy().hasHeightForWidth())
        self.img_titulo_sobre.setSizePolicy(sizePolicy7)
        self.img_titulo_sobre.setMinimumSize(QSize(30, 30))
        self.img_titulo_sobre.setMaximumSize(QSize(34, 50))
        self.img_titulo_sobre.setPixmap(QPixmap(u"img/comp.png"))

        self.horizontalLayout_4.addWidget(self.img_titulo_sobre)

        self.lb_titulo_sobre = QLabel(self.fr_titulo_sobre)
        self.lb_titulo_sobre.setObjectName(u"lb_titulo_sobre")
        sizePolicy7.setHeightForWidth(self.lb_titulo_sobre.sizePolicy().hasHeightForWidth())
        self.lb_titulo_sobre.setSizePolicy(sizePolicy7)
        self.lb_titulo_sobre.setMinimumSize(QSize(30, 30))
        self.lb_titulo_sobre.setMaximumSize(QSize(16777215, 50))
        self.lb_titulo_sobre.setFont(font2)

        self.horizontalLayout_4.addWidget(self.lb_titulo_sobre)


        self.verticalLayout.addWidget(self.fr_titulo_sobre)

        self.fr_geral_sobre = QFormLayout()
        self.fr_geral_sobre.setObjectName(u"fr_geral_sobre")
        self.fr_menu_sobre = QFrame(self.win_sobre)
        self.fr_menu_sobre.setObjectName(u"fr_menu_sobre")
        sizePolicy1.setHeightForWidth(self.fr_menu_sobre.sizePolicy().hasHeightForWidth())
        self.fr_menu_sobre.setSizePolicy(sizePolicy1)
        self.fr_menu_sobre.setMinimumSize(QSize(128, 201))
        self.fr_menu_sobre.setMaximumSize(QSize(128, 201))
        self.fr_menu_sobre.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.fr_menu_sobre.setFrameShape(QFrame.StyledPanel)
        self.fr_menu_sobre.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.fr_menu_sobre)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.sp_menu_sobre = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.sp_menu_sobre, 5, 0, 1, 1)

        self.bt_sair_sobre = QPushButton(self.fr_menu_sobre)
        self.bt_sair_sobre.setObjectName(u"bt_sair_sobre")
        self.bt_sair_sobre.setMinimumSize(QSize(80, 28))
        self.bt_sair_sobre.setFont(font)
        self.bt_sair_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_sair_sobre.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"}")
        self.bt_sair_sobre.setIcon(icon)
        self.bt_sair_sobre.setIconSize(QSize(15, 15))

        self.gridLayout_15.addWidget(self.bt_sair_sobre, 7, 0, 1, 1)

        self.lb_menu_sobre = QLabel(self.fr_menu_sobre)
        self.lb_menu_sobre.setObjectName(u"lb_menu_sobre")
        sizePolicy1.setHeightForWidth(self.lb_menu_sobre.sizePolicy().hasHeightForWidth())
        self.lb_menu_sobre.setSizePolicy(sizePolicy1)
        self.lb_menu_sobre.setMinimumSize(QSize(110, 35))
        self.lb_menu_sobre.setFont(font1)
        self.lb_menu_sobre.setStyleSheet(u"")
        self.lb_menu_sobre.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lb_menu_sobre, 1, 0, 1, 1)

        self.bt_home_sobre = QPushButton(self.fr_menu_sobre)
        self.bt_home_sobre.setObjectName(u"bt_home_sobre")
        sizePolicy1.setHeightForWidth(self.bt_home_sobre.sizePolicy().hasHeightForWidth())
        self.bt_home_sobre.setSizePolicy(sizePolicy1)
        self.bt_home_sobre.setMinimumSize(QSize(110, 28))
        self.bt_home_sobre.setFont(font)
        self.bt_home_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_home_sobre.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.bt_home_sobre, 2, 0, 1, 1)

        self.bt_pets_sobre = QPushButton(self.fr_menu_sobre)
        self.bt_pets_sobre.setObjectName(u"bt_pets_sobre")
        sizePolicy1.setHeightForWidth(self.bt_pets_sobre.sizePolicy().hasHeightForWidth())
        self.bt_pets_sobre.setSizePolicy(sizePolicy1)
        self.bt_pets_sobre.setMinimumSize(QSize(110, 28))
        self.bt_pets_sobre.setFont(font)
        self.bt_pets_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pets_sobre.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_15.addWidget(self.bt_pets_sobre, 3, 0, 1, 1)

        self.bt_usuarios_sobre = QPushButton(self.fr_menu_sobre)
        self.bt_usuarios_sobre.setObjectName(u"bt_usuarios_sobre")
        sizePolicy1.setHeightForWidth(self.bt_usuarios_sobre.sizePolicy().hasHeightForWidth())
        self.bt_usuarios_sobre.setSizePolicy(sizePolicy1)
        self.bt_usuarios_sobre.setMinimumSize(QSize(110, 28))
        self.bt_usuarios_sobre.setFont(font)
        self.bt_usuarios_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_usuarios_sobre.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_15.addWidget(self.bt_usuarios_sobre, 4, 0, 1, 1)


        self.fr_geral_sobre.setWidget(0, QFormLayout.LabelRole, self.fr_menu_sobre)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.fr_geral_sobre.setItem(0, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.lb_infos_sobre = QLabel(self.win_sobre)
        self.lb_infos_sobre.setObjectName(u"lb_infos_sobre")
        sizePolicy.setHeightForWidth(self.lb_infos_sobre.sizePolicy().hasHeightForWidth())
        self.lb_infos_sobre.setSizePolicy(sizePolicy)
        self.lb_infos_sobre.setFont(font)
        self.lb_infos_sobre.setAlignment(Qt.AlignCenter)

        self.fr_geral_sobre.setWidget(1, QFormLayout.FieldRole, self.lb_infos_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.fr_geral_sobre.setItem(7, QFormLayout.FieldRole, self.verticalSpacer)

        self.label_2 = QLabel(self.win_sobre)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.fr_geral_sobre.setWidget(4, QFormLayout.FieldRole, self.label_2)

        self.label = QLabel(self.win_sobre)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"img/ceub.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.fr_geral_sobre.setWidget(5, QFormLayout.FieldRole, self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.fr_geral_sobre.setItem(3, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.fr_geral_sobre.setItem(6, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.lb_infos_sobre_2 = QLabel(self.win_sobre)
        self.lb_infos_sobre_2.setObjectName(u"lb_infos_sobre_2")
        sizePolicy.setHeightForWidth(self.lb_infos_sobre_2.sizePolicy().hasHeightForWidth())
        self.lb_infos_sobre_2.setSizePolicy(sizePolicy)
        self.lb_infos_sobre_2.setFont(font)
        self.lb_infos_sobre_2.setAlignment(Qt.AlignCenter)

        self.fr_geral_sobre.setWidget(2, QFormLayout.FieldRole, self.lb_infos_sobre_2)


        self.verticalLayout.addLayout(self.fr_geral_sobre)

        self.telas.addWidget(self.win_sobre)
        self.win_cadUser = QWidget()
        self.win_cadUser.setObjectName(u"win_cadUser")
        self.gridLayout_5 = QGridLayout(self.win_cadUser)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.fr_botoes_cadUser = QFrame(self.win_cadUser)
        self.fr_botoes_cadUser.setObjectName(u"fr_botoes_cadUser")
        sizePolicy4.setHeightForWidth(self.fr_botoes_cadUser.sizePolicy().hasHeightForWidth())
        self.fr_botoes_cadUser.setSizePolicy(sizePolicy4)
        self.fr_botoes_cadUser.setMinimumSize(QSize(0, 60))
        self.fr_botoes_cadUser.setMaximumSize(QSize(16777215, 60))
        self.fr_botoes_cadUser.setFrameShape(QFrame.StyledPanel)
        self.fr_botoes_cadUser.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.fr_botoes_cadUser)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_aviso_cadUser = QLabel(self.fr_botoes_cadUser)
        self.lb_aviso_cadUser.setObjectName(u"lb_aviso_cadUser")
        self.lb_aviso_cadUser.setStyleSheet(u"color: rgb(138, 185, 214);")

        self.horizontalLayout_12.addWidget(self.lb_aviso_cadUser)

        self.sp_supBt_cadUser = QSpacerItem(1095, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.sp_supBt_cadUser)

        self.bt_cancelar_cadUser = QPushButton(self.fr_botoes_cadUser)
        self.bt_cancelar_cadUser.setObjectName(u"bt_cancelar_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_cancelar_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_cancelar_cadUser.setSizePolicy(sizePolicy1)
        self.bt_cancelar_cadUser.setMinimumSize(QSize(130, 28))
        self.bt_cancelar_cadUser.setFont(font)
        self.bt_cancelar_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cancelar_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.bt_cancelar_cadUser.setIcon(icon2)

        self.horizontalLayout_12.addWidget(self.bt_cancelar_cadUser)

        self.bt_salvar_cadUser = QPushButton(self.fr_botoes_cadUser)
        self.bt_salvar_cadUser.setObjectName(u"bt_salvar_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_salvar_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_salvar_cadUser.setSizePolicy(sizePolicy1)
        self.bt_salvar_cadUser.setMinimumSize(QSize(130, 28))
        self.bt_salvar_cadUser.setFont(font)
        self.bt_salvar_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_salvar_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.bt_salvar_cadUser.setIcon(icon1)

        self.horizontalLayout_12.addWidget(self.bt_salvar_cadUser)

        self.bt_cad_cadUser = QPushButton(self.fr_botoes_cadUser)
        self.bt_cad_cadUser.setObjectName(u"bt_cad_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_cad_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_cad_cadUser.setSizePolicy(sizePolicy1)
        self.bt_cad_cadUser.setMinimumSize(QSize(130, 28))
        self.bt_cad_cadUser.setFont(font)
        self.bt_cad_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cad_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.bt_cad_cadUser.setIcon(icon3)

        self.horizontalLayout_12.addWidget(self.bt_cad_cadUser)


        self.gridLayout_5.addWidget(self.fr_botoes_cadUser, 4, 0, 1, 2)

        self.fr_titulo_cadUser = QFrame(self.win_cadUser)
        self.fr_titulo_cadUser.setObjectName(u"fr_titulo_cadUser")
        self.fr_titulo_cadUser.setMinimumSize(QSize(0, 70))
        self.fr_titulo_cadUser.setMaximumSize(QSize(16777215, 70))
        self.fr_titulo_cadUser.setStyleSheet(u"background-color: rgb(213, 213, 213);\n"
"border-radius:5px;\n"
"")
        self.fr_titulo_cadUser.setFrameShape(QFrame.StyledPanel)
        self.fr_titulo_cadUser.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.fr_titulo_cadUser)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.img_titulo_CadUser = QLabel(self.fr_titulo_cadUser)
        self.img_titulo_CadUser.setObjectName(u"img_titulo_CadUser")
        sizePolicy1.setHeightForWidth(self.img_titulo_CadUser.sizePolicy().hasHeightForWidth())
        self.img_titulo_CadUser.setSizePolicy(sizePolicy1)
        self.img_titulo_CadUser.setPixmap(QPixmap(u"img/cadastro.png"))

        self.horizontalLayout_8.addWidget(self.img_titulo_CadUser)

        self.lb_titulo_cadUser = QLabel(self.fr_titulo_cadUser)
        self.lb_titulo_cadUser.setObjectName(u"lb_titulo_cadUser")
        self.lb_titulo_cadUser.setMinimumSize(QSize(0, 50))
        self.lb_titulo_cadUser.setMaximumSize(QSize(16777215, 50))
        self.lb_titulo_cadUser.setFont(font2)

        self.horizontalLayout_8.addWidget(self.lb_titulo_cadUser)


        self.gridLayout_5.addWidget(self.fr_titulo_cadUser, 0, 0, 1, 2)

        self.fr_cad3_cadUser = QFrame(self.win_cadUser)
        self.fr_cad3_cadUser.setObjectName(u"fr_cad3_cadUser")
        self.fr_cad3_cadUser.setMinimumSize(QSize(0, 60))
        self.fr_cad3_cadUser.setMaximumSize(QSize(16777215, 60))
        self.fr_cad3_cadUser.setFrameShape(QFrame.StyledPanel)
        self.fr_cad3_cadUser.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fr_cad3_cadUser)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_login_cadUser = QLabel(self.fr_cad3_cadUser)
        self.lb_login_cadUser.setObjectName(u"lb_login_cadUser")
        sizePolicy1.setHeightForWidth(self.lb_login_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_login_cadUser.setSizePolicy(sizePolicy1)
        self.lb_login_cadUser.setMinimumSize(QSize(0, 25))
        self.lb_login_cadUser.setMaximumSize(QSize(16777215, 25))
        self.lb_login_cadUser.setFont(font)

        self.horizontalLayout_6.addWidget(self.lb_login_cadUser)

        self.edt_login_cadUser = QLineEdit(self.fr_cad3_cadUser)
        self.edt_login_cadUser.setObjectName(u"edt_login_cadUser")
        self.edt_login_cadUser.setMinimumSize(QSize(0, 31))
        self.edt_login_cadUser.setMaximumSize(QSize(16777215, 31))
        self.edt_login_cadUser.setFont(font)
        self.edt_login_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_6.addWidget(self.edt_login_cadUser)

        self.sp_cad3_cadUser = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.sp_cad3_cadUser)

        self.lb_senha_cadUser = QLabel(self.fr_cad3_cadUser)
        self.lb_senha_cadUser.setObjectName(u"lb_senha_cadUser")
        sizePolicy1.setHeightForWidth(self.lb_senha_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_senha_cadUser.setSizePolicy(sizePolicy1)
        self.lb_senha_cadUser.setMinimumSize(QSize(0, 25))
        self.lb_senha_cadUser.setMaximumSize(QSize(16777215, 25))
        self.lb_senha_cadUser.setFont(font)

        self.horizontalLayout_6.addWidget(self.lb_senha_cadUser)

        self.edt_senha_cadUser = QLineEdit(self.fr_cad3_cadUser)
        self.edt_senha_cadUser.setObjectName(u"edt_senha_cadUser")
        self.edt_senha_cadUser.setMinimumSize(QSize(0, 31))
        self.edt_senha_cadUser.setMaximumSize(QSize(16777215, 31))
        font5 = QFont()
        font5.setFamilies([u"Yu Gothic UI"])
        font5.setPointSize(8)
        font5.setBold(False)
        self.edt_senha_cadUser.setFont(font5)
        self.edt_senha_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")
        self.edt_senha_cadUser.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.edt_senha_cadUser)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.lb_senhaConfirm_cadUser = QLabel(self.fr_cad3_cadUser)
        self.lb_senhaConfirm_cadUser.setObjectName(u"lb_senhaConfirm_cadUser")
        sizePolicy1.setHeightForWidth(self.lb_senhaConfirm_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_senhaConfirm_cadUser.setSizePolicy(sizePolicy1)
        self.lb_senhaConfirm_cadUser.setMinimumSize(QSize(0, 25))
        self.lb_senhaConfirm_cadUser.setMaximumSize(QSize(16777215, 25))
        self.lb_senhaConfirm_cadUser.setFont(font)

        self.horizontalLayout_6.addWidget(self.lb_senhaConfirm_cadUser)

        self.edt_senhaConfirm_cadUser = QLineEdit(self.fr_cad3_cadUser)
        self.edt_senhaConfirm_cadUser.setObjectName(u"edt_senhaConfirm_cadUser")
        self.edt_senhaConfirm_cadUser.setMinimumSize(QSize(0, 31))
        self.edt_senhaConfirm_cadUser.setMaximumSize(QSize(16777215, 31))
        self.edt_senhaConfirm_cadUser.setFont(font5)
        self.edt_senhaConfirm_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")
        self.edt_senhaConfirm_cadUser.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.edt_senhaConfirm_cadUser)


        self.gridLayout_5.addWidget(self.fr_cad3_cadUser, 3, 1, 1, 1)

        self.fr_cad2_cadUser = QFrame(self.win_cadUser)
        self.fr_cad2_cadUser.setObjectName(u"fr_cad2_cadUser")
        self.fr_cad2_cadUser.setMinimumSize(QSize(0, 63))
        self.fr_cad2_cadUser.setMaximumSize(QSize(16777215, 63))
        self.fr_cad2_cadUser.setFrameShape(QFrame.StyledPanel)
        self.fr_cad2_cadUser.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.fr_cad2_cadUser)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_email_cadUser = QLabel(self.fr_cad2_cadUser)
        self.lb_email_cadUser.setObjectName(u"lb_email_cadUser")
        sizePolicy1.setHeightForWidth(self.lb_email_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_email_cadUser.setSizePolicy(sizePolicy1)
        self.lb_email_cadUser.setMinimumSize(QSize(0, 25))
        self.lb_email_cadUser.setMaximumSize(QSize(16777215, 25))
        self.lb_email_cadUser.setFont(font)

        self.horizontalLayout_7.addWidget(self.lb_email_cadUser)

        self.edt_email_cadUser = QLineEdit(self.fr_cad2_cadUser)
        self.edt_email_cadUser.setObjectName(u"edt_email_cadUser")
        self.edt_email_cadUser.setMinimumSize(QSize(0, 31))
        self.edt_email_cadUser.setMaximumSize(QSize(16777215, 31))
        self.edt_email_cadUser.setFont(font)
        self.edt_email_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_7.addWidget(self.edt_email_cadUser)

        self.sp_cad2_cadUser = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.sp_cad2_cadUser)

        self.lb_tipoUser_cadUser = QLabel(self.fr_cad2_cadUser)
        self.lb_tipoUser_cadUser.setObjectName(u"lb_tipoUser_cadUser")
        sizePolicy6.setHeightForWidth(self.lb_tipoUser_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_tipoUser_cadUser.setSizePolicy(sizePolicy6)
        self.lb_tipoUser_cadUser.setMinimumSize(QSize(0, 25))
        self.lb_tipoUser_cadUser.setFont(font)

        self.horizontalLayout_7.addWidget(self.lb_tipoUser_cadUser)

        self.box_tipoUser_cadUser = QComboBox(self.fr_cad2_cadUser)
        self.box_tipoUser_cadUser.addItem("")
        self.box_tipoUser_cadUser.addItem("")
        self.box_tipoUser_cadUser.setObjectName(u"box_tipoUser_cadUser")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(31)
        sizePolicy8.setHeightForWidth(self.box_tipoUser_cadUser.sizePolicy().hasHeightForWidth())
        self.box_tipoUser_cadUser.setSizePolicy(sizePolicy8)
        self.box_tipoUser_cadUser.setMinimumSize(QSize(0, 31))
        self.box_tipoUser_cadUser.setFont(font)
        self.box_tipoUser_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_7.addWidget(self.box_tipoUser_cadUser)


        self.gridLayout_5.addWidget(self.fr_cad2_cadUser, 2, 1, 1, 1)

        self.fr_menu_cadUser = QFrame(self.win_cadUser)
        self.fr_menu_cadUser.setObjectName(u"fr_menu_cadUser")
        sizePolicy1.setHeightForWidth(self.fr_menu_cadUser.sizePolicy().hasHeightForWidth())
        self.fr_menu_cadUser.setSizePolicy(sizePolicy1)
        self.fr_menu_cadUser.setMinimumSize(QSize(128, 201))
        self.fr_menu_cadUser.setMaximumSize(QSize(128, 201))
        self.fr_menu_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.fr_menu_cadUser.setFrameShape(QFrame.StyledPanel)
        self.fr_menu_cadUser.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.fr_menu_cadUser)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.bt_home_cadUser = QPushButton(self.fr_menu_cadUser)
        self.bt_home_cadUser.setObjectName(u"bt_home_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_home_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_home_cadUser.setSizePolicy(sizePolicy1)
        self.bt_home_cadUser.setMinimumSize(QSize(110, 28))
        self.bt_home_cadUser.setFont(font)
        self.bt_home_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_home_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.gridLayout_14.addWidget(self.bt_home_cadUser, 2, 0, 1, 1)

        self.sp_menu_cadUser = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.sp_menu_cadUser, 5, 0, 1, 1)

        self.lb_menu_cadUser = QLabel(self.fr_menu_cadUser)
        self.lb_menu_cadUser.setObjectName(u"lb_menu_cadUser")
        sizePolicy1.setHeightForWidth(self.lb_menu_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_menu_cadUser.setSizePolicy(sizePolicy1)
        self.lb_menu_cadUser.setMinimumSize(QSize(110, 35))
        self.lb_menu_cadUser.setFont(font1)
        self.lb_menu_cadUser.setStyleSheet(u"")
        self.lb_menu_cadUser.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.lb_menu_cadUser, 1, 0, 1, 1)

        self.bt_sair_cadUser = QPushButton(self.fr_menu_cadUser)
        self.bt_sair_cadUser.setObjectName(u"bt_sair_cadUser")
        self.bt_sair_cadUser.setMinimumSize(QSize(80, 28))
        self.bt_sair_cadUser.setFont(font)
        self.bt_sair_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_sair_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"}")
        self.bt_sair_cadUser.setIcon(icon)
        self.bt_sair_cadUser.setIconSize(QSize(15, 15))

        self.gridLayout_14.addWidget(self.bt_sair_cadUser, 7, 0, 1, 1)

        self.bt_pets_cadUser = QPushButton(self.fr_menu_cadUser)
        self.bt_pets_cadUser.setObjectName(u"bt_pets_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_pets_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_pets_cadUser.setSizePolicy(sizePolicy1)
        self.bt_pets_cadUser.setMinimumSize(QSize(110, 28))
        self.bt_pets_cadUser.setFont(font)
        self.bt_pets_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pets_cadUser.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_14.addWidget(self.bt_pets_cadUser, 3, 0, 1, 1)

        self.bt_usuarios_cadUser = QPushButton(self.fr_menu_cadUser)
        self.bt_usuarios_cadUser.setObjectName(u"bt_usuarios_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_usuarios_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_usuarios_cadUser.setSizePolicy(sizePolicy1)
        self.bt_usuarios_cadUser.setMinimumSize(QSize(110, 28))
        self.bt_usuarios_cadUser.setFont(font)
        self.bt_usuarios_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_usuarios_cadUser.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_14.addWidget(self.bt_usuarios_cadUser, 4, 0, 1, 1)


        self.gridLayout_5.addWidget(self.fr_menu_cadUser, 1, 0, 3, 1)

        self.fr_cad1_cadUser = QFrame(self.win_cadUser)
        self.fr_cad1_cadUser.setObjectName(u"fr_cad1_cadUser")
        self.fr_cad1_cadUser.setMinimumSize(QSize(0, 60))
        self.fr_cad1_cadUser.setMaximumSize(QSize(16777215, 60))
        self.fr_cad1_cadUser.setFrameShape(QFrame.StyledPanel)
        self.fr_cad1_cadUser.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.fr_cad1_cadUser)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_nome_cadUser = QLabel(self.fr_cad1_cadUser)
        self.lb_nome_cadUser.setObjectName(u"lb_nome_cadUser")
        sizePolicy1.setHeightForWidth(self.lb_nome_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_nome_cadUser.setSizePolicy(sizePolicy1)
        self.lb_nome_cadUser.setMinimumSize(QSize(0, 25))
        self.lb_nome_cadUser.setMaximumSize(QSize(16777215, 25))
        self.lb_nome_cadUser.setFont(font)

        self.horizontalLayout_5.addWidget(self.lb_nome_cadUser)

        self.edt_nome_cadUser = QLineEdit(self.fr_cad1_cadUser)
        self.edt_nome_cadUser.setObjectName(u"edt_nome_cadUser")
        self.edt_nome_cadUser.setMinimumSize(QSize(0, 31))
        self.edt_nome_cadUser.setMaximumSize(QSize(16777215, 31))
        self.edt_nome_cadUser.setFont(font)
        self.edt_nome_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_5.addWidget(self.edt_nome_cadUser)

        self.sp1_cad1_cadUser = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.sp1_cad1_cadUser)

        self.lb_cpf_cadUser = QLabel(self.fr_cad1_cadUser)
        self.lb_cpf_cadUser.setObjectName(u"lb_cpf_cadUser")
        sizePolicy1.setHeightForWidth(self.lb_cpf_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_cpf_cadUser.setSizePolicy(sizePolicy1)
        self.lb_cpf_cadUser.setMinimumSize(QSize(0, 25))
        self.lb_cpf_cadUser.setMaximumSize(QSize(16777215, 25))
        self.lb_cpf_cadUser.setFont(font)

        self.horizontalLayout_5.addWidget(self.lb_cpf_cadUser)

        self.edt_cpf_cadUser = QLineEdit(self.fr_cad1_cadUser)
        self.edt_cpf_cadUser.setObjectName(u"edt_cpf_cadUser")
        self.edt_cpf_cadUser.setMinimumSize(QSize(0, 31))
        self.edt_cpf_cadUser.setMaximumSize(QSize(16777215, 31))
        self.edt_cpf_cadUser.setFont(font)
        self.edt_cpf_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_5.addWidget(self.edt_cpf_cadUser)

        self.sp2_cad1_cadUser = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.sp2_cad1_cadUser)

        self.lb_cargo_cadUser = QLabel(self.fr_cad1_cadUser)
        self.lb_cargo_cadUser.setObjectName(u"lb_cargo_cadUser")
        sizePolicy1.setHeightForWidth(self.lb_cargo_cadUser.sizePolicy().hasHeightForWidth())
        self.lb_cargo_cadUser.setSizePolicy(sizePolicy1)
        self.lb_cargo_cadUser.setMinimumSize(QSize(0, 25))
        self.lb_cargo_cadUser.setMaximumSize(QSize(16777215, 25))
        self.lb_cargo_cadUser.setFont(font)

        self.horizontalLayout_5.addWidget(self.lb_cargo_cadUser)

        self.box_cargo_cadUser = QComboBox(self.fr_cad1_cadUser)
        self.box_cargo_cadUser.addItem("")
        self.box_cargo_cadUser.addItem("")
        self.box_cargo_cadUser.addItem("")
        self.box_cargo_cadUser.addItem("")
        self.box_cargo_cadUser.addItem("")
        self.box_cargo_cadUser.addItem("")
        self.box_cargo_cadUser.setObjectName(u"box_cargo_cadUser")
        sizePolicy4.setHeightForWidth(self.box_cargo_cadUser.sizePolicy().hasHeightForWidth())
        self.box_cargo_cadUser.setSizePolicy(sizePolicy4)
        self.box_cargo_cadUser.setMinimumSize(QSize(0, 31))
        self.box_cargo_cadUser.setMaximumSize(QSize(16777215, 31))
        self.box_cargo_cadUser.setFont(font)
        self.box_cargo_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);")

        self.horizontalLayout_5.addWidget(self.box_cargo_cadUser)


        self.gridLayout_5.addWidget(self.fr_cad1_cadUser, 1, 1, 1, 1)

        self.line = QFrame(self.win_cadUser)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 6, 0, 1, 2)

        self.fr_tabCad_cadUser = QFrame(self.win_cadUser)
        self.fr_tabCad_cadUser.setObjectName(u"fr_tabCad_cadUser")
        self.fr_tabCad_cadUser.setFrameShape(QFrame.StyledPanel)
        self.fr_tabCad_cadUser.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.fr_tabCad_cadUser)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(1333, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 2)

        self.bt_exportarExcel_cadUser = QPushButton(self.fr_tabCad_cadUser)
        self.bt_exportarExcel_cadUser.setObjectName(u"bt_exportarExcel_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_exportarExcel_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_exportarExcel_cadUser.setSizePolicy(sizePolicy1)
        self.bt_exportarExcel_cadUser.setMinimumSize(QSize(130, 28))
        self.bt_exportarExcel_cadUser.setFont(font)
        self.bt_exportarExcel_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_exportarExcel_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.bt_exportarExcel_cadUser.setIcon(icon4)

        self.gridLayout_2.addWidget(self.bt_exportarExcel_cadUser, 2, 0, 1, 1)

        self.lb_tituloTab_cadUser = QLabel(self.fr_tabCad_cadUser)
        self.lb_tituloTab_cadUser.setObjectName(u"lb_tituloTab_cadUser")
        self.lb_tituloTab_cadUser.setFont(font1)

        self.gridLayout_2.addWidget(self.lb_tituloTab_cadUser, 0, 0, 1, 1)

        self.img_lupa_cadUser = QLabel(self.fr_tabCad_cadUser)
        self.img_lupa_cadUser.setObjectName(u"img_lupa_cadUser")
        self.img_lupa_cadUser.setPixmap(QPixmap(u"img/lupa.png"))

        self.gridLayout_2.addWidget(self.img_lupa_cadUser, 0, 2, 1, 1)

        self.bt_edit_cadUser = QPushButton(self.fr_tabCad_cadUser)
        self.bt_edit_cadUser.setObjectName(u"bt_edit_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_edit_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_edit_cadUser.setSizePolicy(sizePolicy1)
        self.bt_edit_cadUser.setMinimumSize(QSize(130, 28))
        self.bt_edit_cadUser.setFont(font)
        self.bt_edit_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_edit_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.bt_edit_cadUser.setIcon(icon7)

        self.gridLayout_2.addWidget(self.bt_edit_cadUser, 2, 4, 1, 1)

        self.bt_pdf_cadUser = QPushButton(self.fr_tabCad_cadUser)
        self.bt_pdf_cadUser.setObjectName(u"bt_pdf_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_pdf_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_pdf_cadUser.setSizePolicy(sizePolicy1)
        self.bt_pdf_cadUser.setMinimumSize(QSize(130, 28))
        self.bt_pdf_cadUser.setMaximumSize(QSize(30, 16777215))
        self.bt_pdf_cadUser.setFont(font)
        self.bt_pdf_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pdf_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.bt_pdf_cadUser.setIcon(icon5)
        self.bt_pdf_cadUser.setIconSize(QSize(50, 20))

        self.gridLayout_2.addWidget(self.bt_pdf_cadUser, 2, 3, 1, 1)

        self.bt_remover_cadUser = QPushButton(self.fr_tabCad_cadUser)
        self.bt_remover_cadUser.setObjectName(u"bt_remover_cadUser")
        sizePolicy1.setHeightForWidth(self.bt_remover_cadUser.sizePolicy().hasHeightForWidth())
        self.bt_remover_cadUser.setSizePolicy(sizePolicy1)
        self.bt_remover_cadUser.setMinimumSize(QSize(130, 28))
        self.bt_remover_cadUser.setFont(font)
        self.bt_remover_cadUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_remover_cadUser.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(213, 213, 213);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(190, 190, 190);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.bt_remover_cadUser.setIcon(icon6)

        self.gridLayout_2.addWidget(self.bt_remover_cadUser, 2, 5, 1, 1)

        self.sp_supTab_cadUser = QSpacerItem(1248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.sp_supTab_cadUser, 0, 1, 1, 1)

        self.edt_filtro_cadUser = QLineEdit(self.fr_tabCad_cadUser)
        self.edt_filtro_cadUser.setObjectName(u"edt_filtro_cadUser")
        sizePolicy1.setHeightForWidth(self.edt_filtro_cadUser.sizePolicy().hasHeightForWidth())
        self.edt_filtro_cadUser.setSizePolicy(sizePolicy1)
        self.edt_filtro_cadUser.setMinimumSize(QSize(405, 28))
        self.edt_filtro_cadUser.setMaximumSize(QSize(16777215, 28))
        self.edt_filtro_cadUser.setFont(font)
        self.edt_filtro_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"color: rgb(138, 185, 214);\n"
"")
        self.edt_filtro_cadUser.setEchoMode(QLineEdit.Normal)

        self.gridLayout_2.addWidget(self.edt_filtro_cadUser, 0, 3, 1, 3)

        self.tab_cadUser = QTableView(self.fr_tabCad_cadUser)
        self.tab_cadUser.setObjectName(u"tab_cadUser")
        self.tab_cadUser.setFont(font)
        self.tab_cadUser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"QTableView::item:selected {\n"
"   \n"
"	background-color: rgb(192, 226, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.tab_cadUser, 1, 0, 1, 6)


        self.gridLayout_5.addWidget(self.fr_tabCad_cadUser, 7, 0, 1, 2)

        self.telas.addWidget(self.win_cadUser)

        self.gridLayout_7.addWidget(self.telas, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.edt_nomePet_cadPet, self.box_raca_cadPet)
        QWidget.setTabOrder(self.box_raca_cadPet, self.box_cor_cadPet)
        QWidget.setTabOrder(self.box_cor_cadPet, self.box_peso_cadPet)
        QWidget.setTabOrder(self.box_peso_cadPet, self.box_sexo_cadPet)
        QWidget.setTabOrder(self.box_sexo_cadPet, self.box_idade_cadPet)
        QWidget.setTabOrder(self.box_idade_cadPet, self.edt_obs_cadPet)
        QWidget.setTabOrder(self.edt_obs_cadPet, self.edt_end_cadPet)
        QWidget.setTabOrder(self.edt_end_cadPet, self.edt_nomeTutor_cadPet)
        QWidget.setTabOrder(self.edt_nomeTutor_cadPet, self.edt_telTutor_cadPet)
        QWidget.setTabOrder(self.edt_telTutor_cadPet, self.edt_email_cadPet)
        QWidget.setTabOrder(self.edt_email_cadPet, self.edt_nomeEmerg_cadPet)
        QWidget.setTabOrder(self.edt_nomeEmerg_cadPet, self.edt_telEmerg_cadPet)
        QWidget.setTabOrder(self.edt_telEmerg_cadPet, self.bt_home_cadPet)
        QWidget.setTabOrder(self.bt_home_cadPet, self.bt_pets_cadPet)
        QWidget.setTabOrder(self.bt_pets_cadPet, self.bt_usuarios_cadPet)
        QWidget.setTabOrder(self.bt_usuarios_cadPet, self.bt_sair_cadPet)
        QWidget.setTabOrder(self.bt_sair_cadPet, self.bt_salvar_cadPet)
        QWidget.setTabOrder(self.bt_salvar_cadPet, self.bt_cancelar_cadPet)
        QWidget.setTabOrder(self.bt_cancelar_cadPet, self.bt_cad_cadPet)
        QWidget.setTabOrder(self.bt_cad_cadPet, self.tab_cadPet)
        QWidget.setTabOrder(self.tab_cadPet, self.edt_filtro_cadPet)
        QWidget.setTabOrder(self.edt_filtro_cadPet, self.bt_excel_cadPet)
        QWidget.setTabOrder(self.bt_excel_cadPet, self.bt_pdf_cadPet)
        QWidget.setTabOrder(self.bt_pdf_cadPet, self.bt_edit_cadPet)
        QWidget.setTabOrder(self.bt_edit_cadPet, self.bt_remover_cadPet)
        QWidget.setTabOrder(self.bt_remover_cadPet, self.edt_nome_cadUser)
        QWidget.setTabOrder(self.edt_nome_cadUser, self.edt_cpf_cadUser)
        QWidget.setTabOrder(self.edt_cpf_cadUser, self.box_cargo_cadUser)
        QWidget.setTabOrder(self.box_cargo_cadUser, self.edt_email_cadUser)
        QWidget.setTabOrder(self.edt_email_cadUser, self.box_tipoUser_cadUser)
        QWidget.setTabOrder(self.box_tipoUser_cadUser, self.edt_login_cadUser)
        QWidget.setTabOrder(self.edt_login_cadUser, self.edt_senha_cadUser)
        QWidget.setTabOrder(self.edt_senha_cadUser, self.edt_senhaConfirm_cadUser)
        QWidget.setTabOrder(self.edt_senhaConfirm_cadUser, self.bt_home_cadUser)
        QWidget.setTabOrder(self.bt_home_cadUser, self.bt_pets_cadUser)
        QWidget.setTabOrder(self.bt_pets_cadUser, self.bt_usuarios_cadUser)
        QWidget.setTabOrder(self.bt_usuarios_cadUser, self.bt_sair_cadUser)
        QWidget.setTabOrder(self.bt_sair_cadUser, self.bt_cancelar_cadUser)
        QWidget.setTabOrder(self.bt_cancelar_cadUser, self.bt_salvar_cadUser)
        QWidget.setTabOrder(self.bt_salvar_cadUser, self.bt_cad_cadUser)
        QWidget.setTabOrder(self.bt_cad_cadUser, self.edt_filtro_cadUser)
        QWidget.setTabOrder(self.edt_filtro_cadUser, self.tab_cadUser)
        QWidget.setTabOrder(self.tab_cadUser, self.bt_exportarExcel_cadUser)
        QWidget.setTabOrder(self.bt_exportarExcel_cadUser, self.bt_pdf_cadUser)
        QWidget.setTabOrder(self.bt_pdf_cadUser, self.bt_edit_cadUser)
        QWidget.setTabOrder(self.bt_edit_cadUser, self.bt_remover_cadUser)
        QWidget.setTabOrder(self.bt_remover_cadUser, self.bt_home_home)
        QWidget.setTabOrder(self.bt_home_home, self.bt_pets_home)
        QWidget.setTabOrder(self.bt_pets_home, self.bt_usuarios_home)
        QWidget.setTabOrder(self.bt_usuarios_home, self.bt_sair_home)
        QWidget.setTabOrder(self.bt_sair_home, self.bt_sobre_home)
        QWidget.setTabOrder(self.bt_sobre_home, self.bt_home_sobre)
        QWidget.setTabOrder(self.bt_home_sobre, self.bt_pets_sobre)
        QWidget.setTabOrder(self.bt_pets_sobre, self.bt_usuarios_sobre)
        QWidget.setTabOrder(self.bt_usuarios_sobre, self.bt_sair_sobre)

        self.retranslateUi(MainWindow)

        self.telas.setCurrentIndex(0)
        self.box_peso_cadPet.setCurrentIndex(-1)
        self.box_sexo_cadPet.setCurrentIndex(-1)
        self.box_idade_cadPet.setCurrentIndex(-1)
        self.box_raca_cadPet.setCurrentIndex(-1)
        self.box_cor_cadPet.setCurrentIndex(-1)
        self.box_tipoUser_cadUser.setCurrentIndex(-1)
        self.box_cargo_cadUser.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_pets_home.setText(QCoreApplication.translate("MainWindow", u"PETS", None))
        self.bt_sair_home.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.bt_home_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.lb_menu_home.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.bt_usuarios_home.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIOS", None))
        self.img_titulo_home.setText("")
        self.lb_titulo_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.bt_sobre_home.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro \u00a9 2023 Quatro Patas Hotel Ltda. Todos os direitos reservados.", None))
        self.img_logo_menu.setText("")
        self.img_titulo_cadPet.setText("")
        self.lb_titulo_cadPet.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE PETS", None))
        self.lb_aviso_cadPet.setText(QCoreApplication.translate("MainWindow", u"* Todos os campos s\u00e3o de preenchimento obrigat\u00f3rio.", None))
        self.bt_salvar_cadPet.setText(QCoreApplication.translate("MainWindow", u" SALVAR", None))
        self.bt_cancelar_cadPet.setText(QCoreApplication.translate("MainWindow", u" CANCELAR", None))
        self.bt_cad_cadPet.setText(QCoreApplication.translate("MainWindow", u" CADASTRAR", None))
        self.lb_peso_cadPet.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.box_peso_cadPet.setItemText(0, QCoreApplication.translate("MainWindow", u"0-1 kg", None))
        self.box_peso_cadPet.setItemText(1, QCoreApplication.translate("MainWindow", u"1-2 kg", None))
        self.box_peso_cadPet.setItemText(2, QCoreApplication.translate("MainWindow", u"2-3 kg", None))
        self.box_peso_cadPet.setItemText(3, QCoreApplication.translate("MainWindow", u"3-4 kg", None))
        self.box_peso_cadPet.setItemText(4, QCoreApplication.translate("MainWindow", u"4-5 kg", None))
        self.box_peso_cadPet.setItemText(5, QCoreApplication.translate("MainWindow", u"5-6 kg", None))
        self.box_peso_cadPet.setItemText(6, QCoreApplication.translate("MainWindow", u"6-7 kg", None))
        self.box_peso_cadPet.setItemText(7, QCoreApplication.translate("MainWindow", u"7-8 kg", None))
        self.box_peso_cadPet.setItemText(8, QCoreApplication.translate("MainWindow", u"8-9 kg", None))
        self.box_peso_cadPet.setItemText(9, QCoreApplication.translate("MainWindow", u"9-10 kg", None))
        self.box_peso_cadPet.setItemText(10, QCoreApplication.translate("MainWindow", u"10-11 kg", None))
        self.box_peso_cadPet.setItemText(11, QCoreApplication.translate("MainWindow", u"11-12 kg", None))
        self.box_peso_cadPet.setItemText(12, QCoreApplication.translate("MainWindow", u"12-13 kg", None))
        self.box_peso_cadPet.setItemText(13, QCoreApplication.translate("MainWindow", u"13-14 kg", None))
        self.box_peso_cadPet.setItemText(14, QCoreApplication.translate("MainWindow", u"14-15 kg", None))
        self.box_peso_cadPet.setItemText(15, QCoreApplication.translate("MainWindow", u"15-16 kg", None))
        self.box_peso_cadPet.setItemText(16, QCoreApplication.translate("MainWindow", u"16-17 kg", None))
        self.box_peso_cadPet.setItemText(17, QCoreApplication.translate("MainWindow", u"17-18 kg", None))
        self.box_peso_cadPet.setItemText(18, QCoreApplication.translate("MainWindow", u"18-19 kg", None))
        self.box_peso_cadPet.setItemText(19, QCoreApplication.translate("MainWindow", u"19-20 kg", None))
        self.box_peso_cadPet.setItemText(20, QCoreApplication.translate("MainWindow", u"20-21 kg", None))
        self.box_peso_cadPet.setItemText(21, QCoreApplication.translate("MainWindow", u"21-22 kg", None))
        self.box_peso_cadPet.setItemText(22, QCoreApplication.translate("MainWindow", u"22-23 kg", None))
        self.box_peso_cadPet.setItemText(23, QCoreApplication.translate("MainWindow", u"23-24 kg", None))
        self.box_peso_cadPet.setItemText(24, QCoreApplication.translate("MainWindow", u"24-25 kg", None))
        self.box_peso_cadPet.setItemText(25, QCoreApplication.translate("MainWindow", u"25-26 kg", None))
        self.box_peso_cadPet.setItemText(26, QCoreApplication.translate("MainWindow", u"26-27 kg", None))
        self.box_peso_cadPet.setItemText(27, QCoreApplication.translate("MainWindow", u"27-28 kg", None))
        self.box_peso_cadPet.setItemText(28, QCoreApplication.translate("MainWindow", u"28-29 kg", None))
        self.box_peso_cadPet.setItemText(29, QCoreApplication.translate("MainWindow", u"29-30 kg", None))
        self.box_peso_cadPet.setItemText(30, QCoreApplication.translate("MainWindow", u"30-31 kg", None))
        self.box_peso_cadPet.setItemText(31, QCoreApplication.translate("MainWindow", u"31-32 kg", None))
        self.box_peso_cadPet.setItemText(32, QCoreApplication.translate("MainWindow", u"32-33 kg", None))
        self.box_peso_cadPet.setItemText(33, QCoreApplication.translate("MainWindow", u"33-34 kg", None))
        self.box_peso_cadPet.setItemText(34, QCoreApplication.translate("MainWindow", u"34-35 kg", None))
        self.box_peso_cadPet.setItemText(35, QCoreApplication.translate("MainWindow", u"35-36 kg", None))
        self.box_peso_cadPet.setItemText(36, QCoreApplication.translate("MainWindow", u"36-37 kg", None))
        self.box_peso_cadPet.setItemText(37, QCoreApplication.translate("MainWindow", u"37-38 kg", None))
        self.box_peso_cadPet.setItemText(38, QCoreApplication.translate("MainWindow", u"38-39 kg", None))
        self.box_peso_cadPet.setItemText(39, QCoreApplication.translate("MainWindow", u"39-40 kg", None))
        self.box_peso_cadPet.setItemText(40, QCoreApplication.translate("MainWindow", u"40-41 kg", None))
        self.box_peso_cadPet.setItemText(41, QCoreApplication.translate("MainWindow", u"41-42 kg", None))
        self.box_peso_cadPet.setItemText(42, QCoreApplication.translate("MainWindow", u"42-43 kg", None))
        self.box_peso_cadPet.setItemText(43, QCoreApplication.translate("MainWindow", u"43-44 kg", None))
        self.box_peso_cadPet.setItemText(44, QCoreApplication.translate("MainWindow", u"44-45 kg", None))
        self.box_peso_cadPet.setItemText(45, QCoreApplication.translate("MainWindow", u"45-46 kg", None))
        self.box_peso_cadPet.setItemText(46, QCoreApplication.translate("MainWindow", u"46-47 kg", None))
        self.box_peso_cadPet.setItemText(47, QCoreApplication.translate("MainWindow", u"47-48 kg", None))
        self.box_peso_cadPet.setItemText(48, QCoreApplication.translate("MainWindow", u"48-49 kg", None))
        self.box_peso_cadPet.setItemText(49, QCoreApplication.translate("MainWindow", u"49-50 kg", None))
        self.box_peso_cadPet.setItemText(50, QCoreApplication.translate("MainWindow", u"Outro", None))

        self.box_peso_cadPet.setCurrentText("")
        self.lb_sexo_cadPet.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.box_sexo_cadPet.setItemText(0, QCoreApplication.translate("MainWindow", u"F\u00eamea", None))
        self.box_sexo_cadPet.setItemText(1, QCoreApplication.translate("MainWindow", u"Macho", None))

        self.lb_idade_cadPet.setText(QCoreApplication.translate("MainWindow", u"Idade:", None))
        self.box_idade_cadPet.setItemText(0, QCoreApplication.translate("MainWindow", u"0-1 ano", None))
        self.box_idade_cadPet.setItemText(1, QCoreApplication.translate("MainWindow", u"1-2 anos", None))
        self.box_idade_cadPet.setItemText(2, QCoreApplication.translate("MainWindow", u"2-3 anos", None))
        self.box_idade_cadPet.setItemText(3, QCoreApplication.translate("MainWindow", u"3-4 anos", None))
        self.box_idade_cadPet.setItemText(4, QCoreApplication.translate("MainWindow", u"4-5 anos", None))
        self.box_idade_cadPet.setItemText(5, QCoreApplication.translate("MainWindow", u"5-6 anos", None))
        self.box_idade_cadPet.setItemText(6, QCoreApplication.translate("MainWindow", u"6-7 anos", None))
        self.box_idade_cadPet.setItemText(7, QCoreApplication.translate("MainWindow", u"7-8 anos", None))
        self.box_idade_cadPet.setItemText(8, QCoreApplication.translate("MainWindow", u"8-9 anos", None))
        self.box_idade_cadPet.setItemText(9, QCoreApplication.translate("MainWindow", u"9-10 anos", None))
        self.box_idade_cadPet.setItemText(10, QCoreApplication.translate("MainWindow", u"10-11 anos", None))
        self.box_idade_cadPet.setItemText(11, QCoreApplication.translate("MainWindow", u"11-12 anos", None))
        self.box_idade_cadPet.setItemText(12, QCoreApplication.translate("MainWindow", u"12-13 anos", None))
        self.box_idade_cadPet.setItemText(13, QCoreApplication.translate("MainWindow", u"13-14 anos", None))
        self.box_idade_cadPet.setItemText(14, QCoreApplication.translate("MainWindow", u"14-15 anos", None))
        self.box_idade_cadPet.setItemText(15, QCoreApplication.translate("MainWindow", u"15-16 anos", None))
        self.box_idade_cadPet.setItemText(16, QCoreApplication.translate("MainWindow", u"16-17 anos", None))
        self.box_idade_cadPet.setItemText(17, QCoreApplication.translate("MainWindow", u"17-18 anos", None))
        self.box_idade_cadPet.setItemText(18, QCoreApplication.translate("MainWindow", u"18-19 anos", None))
        self.box_idade_cadPet.setItemText(19, QCoreApplication.translate("MainWindow", u"19-20 anos", None))
        self.box_idade_cadPet.setItemText(20, QCoreApplication.translate("MainWindow", u"20-21 anos", None))
        self.box_idade_cadPet.setItemText(21, QCoreApplication.translate("MainWindow", u"21-22 anos", None))
        self.box_idade_cadPet.setItemText(22, QCoreApplication.translate("MainWindow", u"22-23 anos", None))
        self.box_idade_cadPet.setItemText(23, QCoreApplication.translate("MainWindow", u"23-24 anos", None))
        self.box_idade_cadPet.setItemText(24, QCoreApplication.translate("MainWindow", u"24-25 anos", None))
        self.box_idade_cadPet.setItemText(25, "")

        self.lb_nomeEmerg_cadPet.setText(QCoreApplication.translate("MainWindow", u"Nome do Contato de Emerg\u00eancia:", None))
        self.lb_telEmerg_cadPet.setText(QCoreApplication.translate("MainWindow", u"Telefone do Contato de Emerg\u00eancia:", None))
        self.lb_obs_CadPet.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es:", None))
        self.lb_end_cadPet.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.lb_nomeTutor_cadPet.setText(QCoreApplication.translate("MainWindow", u"Nome do Tutor:", None))
        self.lb_tel_cadPet.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.lb_email_cadPet.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.lb_nomePet_cadPet.setText(QCoreApplication.translate("MainWindow", u"Nome do PET:", None))
        self.lb_raca_cadPet.setText(QCoreApplication.translate("MainWindow", u"Ra\u00e7a:", None))
        self.box_raca_cadPet.setItemText(0, QCoreApplication.translate("MainWindow", u"SRD", None))
        self.box_raca_cadPet.setItemText(1, QCoreApplication.translate("MainWindow", u"Outro", None))
        self.box_raca_cadPet.setItemText(2, QCoreApplication.translate("MainWindow", u"Akita", None))
        self.box_raca_cadPet.setItemText(3, QCoreApplication.translate("MainWindow", u"Beagle", None))
        self.box_raca_cadPet.setItemText(4, QCoreApplication.translate("MainWindow", u"Bernese Mountain Dog (C\u00e3o de Montanha dos Pirineus)", None))
        self.box_raca_cadPet.setItemText(5, QCoreApplication.translate("MainWindow", u"Border Collie", None))
        self.box_raca_cadPet.setItemText(6, QCoreApplication.translate("MainWindow", u"Boxer", None))
        self.box_raca_cadPet.setItemText(7, QCoreApplication.translate("MainWindow", u"Bulldog Franc\u00eas", None))
        self.box_raca_cadPet.setItemText(8, QCoreApplication.translate("MainWindow", u"Bulldog Ingl\u00eas", None))
        self.box_raca_cadPet.setItemText(9, QCoreApplication.translate("MainWindow", u"Bull Terrier", None))
        self.box_raca_cadPet.setItemText(10, QCoreApplication.translate("MainWindow", u"Cairn Terrier", None))
        self.box_raca_cadPet.setItemText(11, QCoreApplication.translate("MainWindow", u"Cane Corso", None))
        self.box_raca_cadPet.setItemText(12, QCoreApplication.translate("MainWindow", u"Cavalier King Charles Spaniel", None))
        self.box_raca_cadPet.setItemText(13, QCoreApplication.translate("MainWindow", u"Chihuahua", None))
        self.box_raca_cadPet.setItemText(14, QCoreApplication.translate("MainWindow", u"Cocker Spaniel Ingl\u00eas", None))
        self.box_raca_cadPet.setItemText(15, QCoreApplication.translate("MainWindow", u"Dachshund (Salsicha)", None))
        self.box_raca_cadPet.setItemText(16, QCoreApplication.translate("MainWindow", u"D\u00e1lmata", None))
        self.box_raca_cadPet.setItemText(17, QCoreApplication.translate("MainWindow", u"Doberman", None))
        self.box_raca_cadPet.setItemText(18, QCoreApplication.translate("MainWindow", u"Dogue Alem\u00e3o", None))
        self.box_raca_cadPet.setItemText(19, QCoreApplication.translate("MainWindow", u"Golden Retriever", None))
        self.box_raca_cadPet.setItemText(20, QCoreApplication.translate("MainWindow", u"Husky Siberiano", None))
        self.box_raca_cadPet.setItemText(21, QCoreApplication.translate("MainWindow", u"Labrador ", None))
        self.box_raca_cadPet.setItemText(22, QCoreApplication.translate("MainWindow", u"Lhasa Apso", None))
        self.box_raca_cadPet.setItemText(23, QCoreApplication.translate("MainWindow", u"Malt\u00eas", None))
        self.box_raca_cadPet.setItemText(24, QCoreApplication.translate("MainWindow", u"Pastor Alem\u00e3o", None))
        self.box_raca_cadPet.setItemText(25, QCoreApplication.translate("MainWindow", u"Pastor Belga Malinois", None))
        self.box_raca_cadPet.setItemText(26, QCoreApplication.translate("MainWindow", u"Pastor de Shetland", None))
        self.box_raca_cadPet.setItemText(27, QCoreApplication.translate("MainWindow", u"Pinscher", None))
        self.box_raca_cadPet.setItemText(28, QCoreApplication.translate("MainWindow", u"Pitbull", None))
        self.box_raca_cadPet.setItemText(29, QCoreApplication.translate("MainWindow", u"Poodle", None))
        self.box_raca_cadPet.setItemText(30, QCoreApplication.translate("MainWindow", u"Pug", None))
        self.box_raca_cadPet.setItemText(31, QCoreApplication.translate("MainWindow", u"Rottweiler", None))
        self.box_raca_cadPet.setItemText(32, QCoreApplication.translate("MainWindow", u"S\u00e3o Bernardo", None))
        self.box_raca_cadPet.setItemText(33, QCoreApplication.translate("MainWindow", u"Samoieda", None))
        self.box_raca_cadPet.setItemText(34, QCoreApplication.translate("MainWindow", u"Schnauzer", None))
        self.box_raca_cadPet.setItemText(35, QCoreApplication.translate("MainWindow", u"Setter Irland\u00eas", None))
        self.box_raca_cadPet.setItemText(36, QCoreApplication.translate("MainWindow", u"Shar Pei", None))
        self.box_raca_cadPet.setItemText(37, QCoreApplication.translate("MainWindow", u"Shiba Inu", None))
        self.box_raca_cadPet.setItemText(38, QCoreApplication.translate("MainWindow", u"Shih Tzu", None))
        self.box_raca_cadPet.setItemText(39, QCoreApplication.translate("MainWindow", u"Spitz Alem\u00e3o (Lulu da Pomer\u00e2nia)", None))
        self.box_raca_cadPet.setItemText(40, QCoreApplication.translate("MainWindow", u"Staffordshire Bull Terrier", None))
        self.box_raca_cadPet.setItemText(41, QCoreApplication.translate("MainWindow", u"Teckel (Dachshund)", None))
        self.box_raca_cadPet.setItemText(42, QCoreApplication.translate("MainWindow", u"Weimaraner", None))
        self.box_raca_cadPet.setItemText(43, QCoreApplication.translate("MainWindow", u"West Highland White Terrier", None))
        self.box_raca_cadPet.setItemText(44, QCoreApplication.translate("MainWindow", u"Yorkshire Terrier", None))

        self.box_raca_cadPet.setCurrentText("")
        self.lb_Cor_cadPet.setText(QCoreApplication.translate("MainWindow", u"Cor:", None))
        self.box_cor_cadPet.setItemText(0, QCoreApplication.translate("MainWindow", u"Outro", None))
        self.box_cor_cadPet.setItemText(1, QCoreApplication.translate("MainWindow", u"Albino (totalmente branco com olhos rosados)", None))
        self.box_cor_cadPet.setItemText(2, QCoreApplication.translate("MainWindow", u"Branco", None))
        self.box_cor_cadPet.setItemText(3, QCoreApplication.translate("MainWindow", u"Canela", None))
        self.box_cor_cadPet.setItemText(4, QCoreApplication.translate("MainWindow", u"Castanho", None))
        self.box_cor_cadPet.setItemText(5, QCoreApplication.translate("MainWindow", u"Cinza", None))
        self.box_cor_cadPet.setItemText(6, QCoreApplication.translate("MainWindow", u"Creme", None))
        self.box_cor_cadPet.setItemText(7, QCoreApplication.translate("MainWindow", u"Dourado", None))
        self.box_cor_cadPet.setItemText(8, QCoreApplication.translate("MainWindow", u"Marrom", None))
        self.box_cor_cadPet.setItemText(9, QCoreApplication.translate("MainWindow", u"Marrom e Branco", None))
        self.box_cor_cadPet.setItemText(10, QCoreApplication.translate("MainWindow", u"Merle (manchas em v\u00e1rias tonalidades)", None))
        self.box_cor_cadPet.setItemText(11, QCoreApplication.translate("MainWindow", u"Manto (manchas grandes e distintas em cor contrastante)", None))
        self.box_cor_cadPet.setItemText(12, QCoreApplication.translate("MainWindow", u"Preto", None))
        self.box_cor_cadPet.setItemText(13, QCoreApplication.translate("MainWindow", u"Preto e Branco", None))
        self.box_cor_cadPet.setItemText(14, QCoreApplication.translate("MainWindow", u"Ruivo", None))
        self.box_cor_cadPet.setItemText(15, QCoreApplication.translate("MainWindow", u"Sable (pelagem com pontas mais escuras)", None))
        self.box_cor_cadPet.setItemText(16, QCoreApplication.translate("MainWindow", u"Tricolor (preto, branco e marrom)", None))

        self.bt_home_cadPet.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.bt_pets_cadPet.setText(QCoreApplication.translate("MainWindow", u"PETS", None))
        self.bt_sair_cadPet.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.lb_menu_cadPet.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.bt_usuarios_cadPet.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIOS", None))
        self.img_lupa_cadPet.setText("")
        self.edt_filtro_cadPet.setInputMask("")
        self.edt_filtro_cadPet.setText("")
        self.bt_excel_cadPet.setText(QCoreApplication.translate("MainWindow", u" EXPORTAR", None))
        self.bt_pdf_cadPet.setText(QCoreApplication.translate("MainWindow", u"GERAR PDF", None))
        self.bt_remover_cadPet.setText(QCoreApplication.translate("MainWindow", u" REMOVER", None))
        self.lb_tituloTab_cadPet.setText(QCoreApplication.translate("MainWindow", u"CADASTROS", None))
        self.bt_edit_cadPet.setText(QCoreApplication.translate("MainWindow", u" EDITAR", None))
        self.img_titulo_sobre.setText("")
        self.lb_titulo_sobre.setText(QCoreApplication.translate("MainWindow", u"SISTEMA DE CADASTRO", None))
        self.bt_sair_sobre.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.lb_menu_sobre.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.bt_home_sobre.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.bt_pets_sobre.setText(QCoreApplication.translate("MainWindow", u"PETS", None))
        self.bt_usuarios_sobre.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIOS", None))
        self.lb_infos_sobre.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro desenvolvido nas disciplinas Projeto de TI I e Projeto de TI II pelos alunos:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Curso Superior de Tecnologia em An\u00e1lise e Desenvolvimento de Sistemas", None))
        self.label.setText("")
        self.lb_infos_sobre_2.setText(QCoreApplication.translate("MainWindow", u"Artur Alves Ara\u00fajo Nogueira, Mariana Hikari Daitoku e Tatiana Guedes Medeiro Evangelista.", None))
        self.lb_aviso_cadUser.setText(QCoreApplication.translate("MainWindow", u"* Todos os campos s\u00e3o de preenchimento obrigat\u00f3rio.", None))
        self.bt_cancelar_cadUser.setText(QCoreApplication.translate("MainWindow", u" CANCELAR", None))
        self.bt_salvar_cadUser.setText(QCoreApplication.translate("MainWindow", u" SALVAR", None))
        self.bt_cad_cadUser.setText(QCoreApplication.translate("MainWindow", u" CADASTRAR", None))
        self.img_titulo_CadUser.setText("")
        self.lb_titulo_cadUser.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE USU\u00c1RIOS", None))
        self.lb_login_cadUser.setText(QCoreApplication.translate("MainWindow", u"Login:", None))
        self.lb_senha_cadUser.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.edt_senha_cadUser.setInputMask("")
        self.lb_senhaConfirm_cadUser.setText(QCoreApplication.translate("MainWindow", u"Confirme a senha:", None))
        self.edt_senhaConfirm_cadUser.setInputMask("")
        self.lb_email_cadUser.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.lb_tipoUser_cadUser.setText(QCoreApplication.translate("MainWindow", u"Tipo de usu\u00e1rio:", None))
        self.box_tipoUser_cadUser.setItemText(0, QCoreApplication.translate("MainWindow", u"Comum", None))
        self.box_tipoUser_cadUser.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.bt_home_cadUser.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.lb_menu_cadUser.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.bt_sair_cadUser.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.bt_pets_cadUser.setText(QCoreApplication.translate("MainWindow", u"PETS", None))
        self.bt_usuarios_cadUser.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIOS", None))
        self.lb_nome_cadUser.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.edt_nome_cadUser.setInputMask("")
        self.edt_nome_cadUser.setText("")
        self.lb_cpf_cadUser.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.lb_cargo_cadUser.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.box_cargo_cadUser.setItemText(0, QCoreApplication.translate("MainWindow", u"Cuidador", None))
        self.box_cargo_cadUser.setItemText(1, QCoreApplication.translate("MainWindow", u"Diretor", None))
        self.box_cargo_cadUser.setItemText(2, QCoreApplication.translate("MainWindow", u"Gerente", None))
        self.box_cargo_cadUser.setItemText(3, QCoreApplication.translate("MainWindow", u"Recepcionista", None))
        self.box_cargo_cadUser.setItemText(4, QCoreApplication.translate("MainWindow", u"Veterin\u00e1rio", None))
        self.box_cargo_cadUser.setItemText(5, QCoreApplication.translate("MainWindow", u"Zelador", None))

        self.bt_exportarExcel_cadUser.setText(QCoreApplication.translate("MainWindow", u" EXPORTAR", None))
        self.lb_tituloTab_cadUser.setText(QCoreApplication.translate("MainWindow", u"CADASTROS", None))
        self.img_lupa_cadUser.setText("")
        self.bt_edit_cadUser.setText(QCoreApplication.translate("MainWindow", u" EDITAR", None))
        self.bt_pdf_cadUser.setText(QCoreApplication.translate("MainWindow", u"GERAR PDF", None))
        self.bt_remover_cadUser.setText(QCoreApplication.translate("MainWindow", u" REMOVER", None))
        self.edt_filtro_cadUser.setInputMask("")
    # retranslateUi

