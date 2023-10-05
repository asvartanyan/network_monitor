import folium

from Model import Model
from View import View, MapView
from PyQt5.QtWidgets import QTableWidgetItem
class Controller:
    model = Model.Model()
    view = None
    update_time_endpoints = 16000
    mapview = None
    def the_button_was_clicked(self):
        self.model.increment()
        self.view.statusBar().showMessage(str(self.model.num))
        self.view.ui.tableWidget.horizontalHeader().setVisible(False)

    def handle_update_list_button(self):
        net_list = self.model.getNetConnectionList()
        self.view.ui.listWidget.clear()
        while self.view.ui.tableWidget.rowCount() > 0:
            self.view.ui.tableWidget.removeRow(0)
        for net in net_list:
            self.view.ui.listWidget.addItem(str(net))
            rowPosition = self.view.ui.tableWidget.rowCount()
            self.view.ui.tableWidget.insertRow(rowPosition)
            self.view.ui.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(net["ip"])))
            self.view.ui.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(net["port"])))
            self.view.ui.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(net["country"])))
            self.view.ui.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(net["city"])))


    def handle_timer_update(self):
        self.handle_update_list_button()
        self.view.timer_update.start(self.update_time_endpoints)

    def handle_show_on_map(self):
        _map = self.model.getFoliumMapWithMarkers(self.model.getNetConnectionList())
        self.mapview = MapView.MapView(_map)
        self.mapview.close()
        self.mapview.show()










