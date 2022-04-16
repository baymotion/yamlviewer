# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yamlviewer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        self.actionE_xit = QAction(MainWindow)
        self.actionE_xit.setObjectName(u"actionE_xit")
        self.action_Reload = QAction(MainWindow)
        self.action_Reload.setObjectName(u"action_Reload")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yaml = QTreeWidget(self.centralwidget)
        self.yaml.setObjectName(u"yaml")
        self.yaml.setColumnCount(2)
        self.yaml.header().setDefaultSectionSize(300)

        self.horizontalLayout.addWidget(self.yaml)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Reload)
        self.menu_File.addAction(self.actionE_xit)

        self.retranslateUi(MainWindow)
        self.actionE_xit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"yamlviewer", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open", None))
        self.actionE_xit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.action_Reload.setText(QCoreApplication.translate("MainWindow", u"&Reload (F5)", None))
        ___qtreewidgetitem = self.yaml.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

