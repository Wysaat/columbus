from header import *
from config import *
from tcp import *
from database import *
from ssl_server import *

def main():
    # server = TCP_server(inet_addr)
    server = SSL_server(inet_addr)

    while True:
        server.accept_connection()
        print '[DEBUG]000000000000000000000000000000000000000000'
        header = server.listen()
        print header
        header = Header(header)

        if header.http_method() == 'POST':
            content_length = header.content_length()
            content = server.sc.recv(content_length)
            print repr(content)

            data = get_data(header.content_first_part() + content)

            db = Database()
            db.execute(header.db_table(), header.db_action(), data)
            db.close()

        print '[DEBUG]------------------------------------------'
        server.respond(header)
        print '[DEBUG]222222222222222222222222222222222222222222'

def get_data(content):
    data = []
    entities = content.split('&')
    print entities
    for entity in entities:
        data.append(entity.split('=')[1])
    return data

if __name__ == '__main__':
    main()
