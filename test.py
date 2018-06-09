from netdisco.discovery import NetworkDiscovery
import netdisco
netdis = NetworkDiscovery()

netdis.scan()
print (netdis.discover())
for dev in netdis.discover():
    print(dev, netdis.get_info(dev))

netdis.stop()