from header import *
from config import *
from tcp import *

def main():
    server = TCP_server(inet_addr)

    while True:
        server.accept_connection()
        print '[DEBUG]000000000000000000000000000000000000000000'
        header = server.listen()
        print header
        header = Header(header)
        print '[DEBUG]------------------------------------------'
        server.respond(header)
        print '[DEBUG]222222222222222222222222222222222222222222'

if __name__ == '__main__':
    main()