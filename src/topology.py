#!/usr/bin/python                                                                                                                                                            
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel 
from mininet.cli import CLI

'''
Single switch connected to one host.
'''
class SingleSwitchTopo(Topo):
    def build(self):
        # Add all switches to a topology
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        # Add all hosts to a topology
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        self.addLink(
			s2,
			s1,
			bw = 30,
	        delay = '87us',
	        loss = 3)
        self.addLink(
	        s3,
	        s1,
	        bw = 35,
	        delay = '48us',
	        loss = 6)
        self.addLink(
	        s4,
	        s1,
	        bw = 38,
	        delay = '76us',
	        loss = 4)
        self.addLink(
	        s5,
	        s1,
	        bw = 40,
	        delay = '52us',
	        loss = 2)
        self.addLink(
	        h1,
	        s2,
	        bw = 14,
	        delay = '5ms',
	        loss = 13)
        self.addLink(
	        h2,
	        s2,
	        bw = 12,
	        delay = '4ms',
	        loss = 15)
        self.addLink(
	        h3,
	        s3,
	        bw = 15,
	        delay = '3ms',
	        loss = 8)
        self.addLink(
	        h4,
	        s3,
	        bw = 11,
	        delay = '2ms',
	        loss = 9)
        self.addLink(
	        h5,
	        s1,
	        bw = 22,
	        delay = '3ms',
	        loss = 9)
        self.addLink(
	        h6,
	        s1,
	        bw = 25,
	        delay = '1ms',
	        loss = 7)
        self.addLink(
	        h7,
	        s1,
	        bw = 18,
	        delay = '4ms',
	        loss = 6)
        self.addLink(
	        h8,
	        s1,
	        bw = 20,
	        delay = '2ms',
	        loss = 8)
        self.addLink(
	        h9,
	        s4,
	        bw = 30,
	        delay = '7ms',
	        loss = 12)
        self.addLink(
	        h10,
	        s5,
	        bw = 25,
	        delay = '5ms',
	        loss = 10)

'''
Create and test a simple network
'''
def simpleTest():
    # Create a topology with 2 hosts and 1 switch
    topo = SingleSwitchTopo()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")
    net.pingAll()
    # Dump every hosts'and switches'connection
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
	# Add the following code and do NOT use net.stop()
    CLI(net)

'''
Main (entry point)
'''
# Remember to import the following module first! 
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
