# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\mainwindowsui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 781, 411))
        self.tableWidget.setToolTip("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 440, 341, 261))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.UpdatePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdatePushButton.setGeometry(QtCore.QRect(800, 10, 111, 23))
        self.UpdatePushButton.setObjectName("UpdatePushButton")
        self.OpenMapPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenMapPushButton.setGeometry(QtCore.QRect(800, 40, 111, 23))
        self.OpenMapPushButton.setObjectName("OpenMapPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Port"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Country"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "City"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Новый элемент"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.UpdatePushButton.setText(_translate("MainWindow", "Update"))
        self.OpenMapPushButton.setText(_translate("MainWindow", "Show on map"))
