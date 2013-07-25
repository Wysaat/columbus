from header import *
from config import *
from tcp import *
from database import *
from ssl_server import *

def main():
    if HTTPS:
        server = SSL_server(inet_addr)
    else:
        server = TCP_server(inet_addr)

    while True:
        server.accept_connection()
        print '[DEBUG]000000000000000000000000000000000000000000'
        header = server.listen()
        print header
        try:
            header = Header(header)
        except:
            continue

        if header.http_method() == 'POST':
            content_length = header.content_length()
            print '[DEBUG]content length........................'
            # content = server.sc.recv(content_length)
            content = server.sc.recv(content_length)
            print repr(content)

            total_content = header.content_first_part() + content
            data = get_data(total_content)
            
            if proc[header.relative_url()] == "database":
                db = Database()
                print 'transferring data...'
                db.execute(header.db_table(), header.db_action(), data)
                db.close()
            else:
                method = proc[header.relative_url()]
                method(data)

        print '[DEBUG]------------------------------------------'
        server.respond(header)
        print '[DEBUG]222222222222222222222222222222222222222222'

        # if not HTTPS and header.relative_url() in https:
        #     server = SSL_server(inet_addr, 80)

def get_data(content):
    data = []
    entities = content.split('&')
    print entities
    for entity in entities:
        data.append(entity.split('=')[1])
    return data

if __name__ == '__main__':
    main()
