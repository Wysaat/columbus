import sys, socket, time
from config import *
from header import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = inet_addr
PORT = 80

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

def main():
    header = ''
    while True:
        print 'Columbus http server, started at %s on port %d' % (HOST, PORT)
        sc, sockname = s.accept()
        print 'connected from', sockname
        print 'soket connects', sc.getsockname(), 'and', sc.getpeername()
        header_time_s = time.time()
        while True:
            header_time = time.time()
            t_time = header_time - header_time_s
            if t_time > 10:
                break
            message = sc.recv(16)
            header += message
            print message
            if ('\r\n\r\n' in header) or (message == ''):
                break
        print 'the http header is ', repr(header)

        http_method, page_file, http_version = header_p(header)

        if http_method == 'GET':
            sc.sendall(page_file)
        else:
            sc.sendall("[COLUMBUS] sorry, currently http method %s\
 is not supported" % http_method)
        sc.close()
        print 'socket is closed'

if __name__ == '__main__':
    main()
