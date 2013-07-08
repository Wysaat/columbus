import socket
from config import *
from header import *

class TCP_server(object):
    def __init__(self, host, port=80):
        self.host = host
        self.port = port
        self.socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)

    def accept_connection(self):
        print 'Columbus http server, listening at %s on port %d' \
                   % (self.host, self.port)
        self.sc, sockname = self.socket.accept()
        print 'connected from', sockname
        print 'socket connects', self.sc.getsockname(), 'and', self.sc.getpeername()

    def listen(self, size=16):
        header = ''
        while True:
            message = self.sc.recv(size)
            header += message

            if '\r\n\r\n' in header:
                return header

    def respond(self, header_obj):
        http_method = header_obj.http_method()
        page = header_obj.page()
        response_header = header_obj.response_header()

        self.sc.sendall(response_header)

        if http_method == 'GET':
            self.sc.sendall(page)
        elif http_method != 'POST':
            self.sc.sendall("[COLUMBUS] sorry, currently http method %s\
 is not supported" % http_method)
        self.sc.close()
        return
