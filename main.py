import SocketServer
import socket
from proxy import UDPHandler
import proxy

def main():
    # Set port and IP address into variables
    port = 5000
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print 'Starting proxy server...'
    print 'Your IP address is: %s' % ipaddress
    print 'Use port %s to connect' % port
    # Set global variables inside lib
    proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, port)
    proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, port)
    # Start server and let it run forever
    server = SocketServer.UDPServer((ipaddress, port), UDPHandler)
    while 1:
        server.handle_request()


if __name__ == "__main__":
    main()
