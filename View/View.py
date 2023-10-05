from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QTableView, QTableWidget)
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from Controller import Controller
from UI.mainwindowsui import Ui_MainWindow
import sys


class View(QMainWindow):
    controller = Controller.Controller()
    timer_update = QTimer()
    def __init__(self, controller = None):
        super(View, self).__init__()
        self.controller = controller

    def initMainUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.setToolTip('This is a <b>QWidget</b> widget')

        #btn = QPushButton('Add +1', self)
        #btn.setToolTip('This is a <b>QPushButton</b> widget')
        #btn.resize(btn.sizeHint())
        #btn.move(50, 50)
        #btn.clicked.connect(self.controller.the_button_was_clicked)

        self.ui.UpdatePushButton.clicked.connect(self.controller.handle_update_list_button)
        self.timer_update.timeout.connect(self.controller.handle_timer_update)
        self.timer_update.start(self.controller.update_time_endpoints)
        self.ui.OpenMapPushButton.clicked.connect(self.controller.handle_show_on_map)


        self.statusBar().showMessage(str(self.controller.model.num))
        #self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

    def initMapUI(self):
        self.setGeometry(500,500,500,500)
        self.move(300, 300)
        self.setWindowTitle('Simple')
        self.show()




