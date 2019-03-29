from mininet.net import Mininet
from mininet.util import createLink

net = Mininet()

#creating nodes in a network
c0 = net.addController()
h0 = net.addHost('h0')
s0 = net.addSwitch('s0')
h1 = net.addHost('h1')

#creating links between nodes in anetowrk(2-ways)
net.addLink(h0,s0)
net.addLink(h1,s1)

#setip
h0.setIP('192.168.1.1',24)
h1.setIP('192.168.1.2',24)

net.start()
net.pingAll()
net.stop()
