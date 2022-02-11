# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.tabHSK = QTabWidget(self.centralwidget)
        self.tabHSK.setObjectName(u"tabHSK")
        self.tabHSK.setMouseTracking(True)
        self.tabHSK.setAutoFillBackground(True)
        self.tabHSK.setLocale(QLocale(QLocale.English, QLocale.Europe))
        self.tabHSK.setTabShape(QTabWidget.Triangular)
        self.tabHSK.setElideMode(Qt.ElideNone)
        self.tabHSK.setDocumentMode(False)
        self.HSK1 = QWidget()
        self.HSK1.setObjectName(u"HSK1")
        self.HSK1.setEnabled(True)
        self.tabHSK.addTab(self.HSK1, "")
        self.HSK2 = QWidget()
        self.HSK2.setObjectName(u"HSK2")
        self.tabHSK.addTab(self.HSK2, "")
        self.HSK3 = QWidget()
        self.HSK3.setObjectName(u"HSK3")
        self.tabHSK.addTab(self.HSK3, "")
        self.HSK4 = QWidget()
        self.HSK4.setObjectName(u"HSK4")
        self.tabHSK.addTab(self.HSK4, "")
        self.HSK5 = QWidget()
        self.HSK5.setObjectName(u"HSK5")
        self.tabHSK.addTab(self.HSK5, "")
        self.HSK6 = QWidget()
        self.HSK6.setObjectName(u"HSK6")
        self.tabHSK.addTab(self.HSK6, "")
        self.HSK7 = QWidget()
        self.HSK7.setObjectName(u"HSK7")
        self.tabHSK.addTab(self.HSK7, "")
        self.HSK8 = QWidget()
        self.HSK8.setObjectName(u"HSK8")
        self.tabHSK.addTab(self.HSK8, "")
        self.HSK9 = QWidget()
        self.HSK9.setObjectName(u"HSK9")
        self.tabHSK.addTab(self.HSK9, "")

        self.verticalLayout.addWidget(self.tabHSK)

        self.BtnLayout = QHBoxLayout()
        self.BtnLayout.setSpacing(10)
        self.BtnLayout.setObjectName(u"BtnLayout")
        self.BtnLayout.setContentsMargins(10, 10, 10, 10)
        self.Save = QPushButton(self.centralwidget)
        self.Save.setObjectName(u"Save")
        self.Save.setStyleSheet(u"")
        self.Save.setCheckable(False)
        self.Save.setChecked(False)

        self.BtnLayout.addWidget(self.Save)

        self.Print = QPushButton(self.centralwidget)
        self.Print.setObjectName(u"Print")
        self.Print.setCheckable(False)

        self.BtnLayout.addWidget(self.Print)


        self.verticalLayout.addLayout(self.BtnLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabHSK.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK1), QCoreApplication.translate("MainWindow", u"HSK 1", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK2), QCoreApplication.translate("MainWindow", u"HSK 2", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK3), QCoreApplication.translate("MainWindow", u"HSK 3", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK4), QCoreApplication.translate("MainWindow", u"HSK 4", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK5), QCoreApplication.translate("MainWindow", u"HSK 5", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK6), QCoreApplication.translate("MainWindow", u"HSK 6", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK7), QCoreApplication.translate("MainWindow", u"HSK 7", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK8), QCoreApplication.translate("MainWindow", u"HSK 8", None))
        self.tabHSK.setTabText(self.tabHSK.indexOf(self.HSK9), QCoreApplication.translate("MainWindow", u"HSK 9", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
    # retranslateUi

