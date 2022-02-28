import SocketServer
import socket
from proxy import UDPHandler
import proxy



if __name__ == "__main__":
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    proxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, proxy.PORT)
    proxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, proxy.PORT)
    server = SocketServer.UDPServer((proxy.HOST, proxy.PORT), UDPHandler)
    server.serve_forever()