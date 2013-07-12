######################################################################
####### CAN'T NAME THIS FILE ssl.py BECAUSE SSL IS IMPORTED!!! #######
######################################################################
import socket, ssl
from config import *

class SSL_server(object):
    def __init__(self, host, port=443):
        self.host = host
        self.port = port
        self.socket = socket.socket()
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)

    def accept_connection(self):
        print 'columbus http server, listening at %s on port %d' \
                   % (self.host, self.port)
        self.sc, sockname = self.socket.accept()
        print 'connected from', sockname
        print 'socket connects', self.sc.getsockname(), 'and', self.sc.getpeername()
        self.ssl_sc = ssl.wrap_socket(self.sc,
                                      server_side=True,
                                      certfile=ssl_certfile,
                                      keyfile=ssl_keyfile,
                                      ssl_version=ssl.PROTOCOL_TLSv1)          


    def listen(self):
        header = ''

        while True:
            header += self.ssl_sc.read()
            if '\r\n\r\n' in header:
                return header

    def respond(self, header_obj):
        http_method = header_obj.http_method()
        page = header_obj.page()
        response_header = header_obj.response_header()

        self.ssl_sc.sendall(response_header)

        if http_method == 'GET':
            self.ssl_sc.sendall(page)
        elif http_method != 'POST':
            self.ssl_sc.sendall("[COLUMBUS] sorry, currently http method %s\
 is not supported" % http_method)
        self.ssl_sc.shutdown(socket.SHUT_RDWR)
        self.ssl_sc.close()
        return