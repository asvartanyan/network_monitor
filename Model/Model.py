import random
import psutil
import requests
import json
import folium

class Model:
    endpoints_nets = None

    def __init__(self,num=0):
        self.num = num

        ips = ["173.194.222.100","93.186.255.194"]

        #print(ans)

    def increment(self):
        self.num += 1

    def getNetConnectionList(self):
        net_conn_list = []
        ips_list = []
        ps = psutil.net_connections(kind="inet")
        nets = []
        for p in ps:
            if len(p.raddr) == 2:
                net = {'ip': str(p.raddr.ip), 'port': str(p.raddr.port), 'country': "", 'city': "",'lat': 0, 'lon': 0}
                net_conn_list.append(net)
                ips_list.append(str(p.raddr.ip))

        url = 'http://ip-api.com/batch'
        response = requests.post(url, data=json.dumps(ips_list)).json()
        #ans = response[1].get("country")
        for ans in response:
            ip = str(ans.get("query"))
            country = str(ans.get("country"))
            city = str(ans.get("city"))
            lat = ans.get("lat")
            lon = ans.get("lon")
            for net in net_conn_list:
                if ip == net["ip"]:
                    net["country"] = country
                    net["city"] = city
                    net["lat"] = lat
                    net["lon"] = lon

        self.endpoints_nets = net_conn_list
        return net_conn_list

    def getFoliumMapWithMarkers(self,net_conn_list):
        _map = folium.Map()
        nets = net_conn_list
        rnd = (random.random()/10000)
        for net in nets:
            lat = net["lat"]
            lon = net["lon"]
            if ((lat != None) and (lon != None)):
                coord = [lat+rnd,lon+rnd]
                folium.Marker(location=coord).add_to(_map)
        return _map






