import folium
import libpcap
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from View import View, MapView
from Model import Model
from Controller import Controller


if __name__ == '__main__':

      app = QApplication(sys.argv)
      controller = Controller.Controller()
      view = View.View(controller)
      controller.view = view
      controller.mapview = MapView.MapView()

      view.initMainUI()




      sys.exit((app.exec_()))

