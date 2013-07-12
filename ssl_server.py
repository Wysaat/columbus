######################################################################
####### CAN'T NAME THIS FILE ssl.py BECAUSE SSL IS IMPORTED!!! #######
######################################################################
import socket, ssl
from config import *

bindsocket = socket.socket()
bindsocket.bind((inet_addr, ssl_port))
bindsocket.listen(5)
print 'socket is listening...'

while True:
    newsocket, fromaddr = bindsocket.accept()
    print 'newsocket is:', newsocket
    print 'fromaddr  is:', fromaddr

    connstream = ssl.wrap_socket(newsocket,
                                 server_side = True,
                                 certfile = ssl_certfile,
                                 keyfile = ssl_keyfile,
                                 ssl_version = ssl.PROTOCOL_TLSv1)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()

def deal_with_client(connstream):
    data = connstream.read()

    while data:
        print data

        # if not do_something(connstream, data):
        #    break
        data = connstream.read()
    return data