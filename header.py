from config import *

CRLF = "\r\n"

class Header(object):
    def __init__(self, header):
        self.response_status_code = "200 OK"
        header = header.strip()
        lines = header.split('\r\n')
        self.lines = [line.split() for line in lines]

    def http_method(self):
        http_method = self.lines[0][0]
        return http_method

    def relative_url(self):
        relative_url = self.lines[0][1]
        return relative_url

    def http_version(self):
        http_version = self.lines[0][2]
        return http_version

    def accept_types(self):
        for line in lines:
            if 'accept:' == line[0].lower():
                accept_types = line[1]
                return accept_types

    def response_header(self):
        response_header = ''
        response_header += self.http_version() + ' ' \
                         + self.response_status_code + CRLF

        if 'png' == self.relative_url().split('.')[-1]:
            content_type = "image/png"
            accept_ranges = "bytes"
            content_length = len(self.page())

            response_header +=  "Accept-Ranges:" + ' ' + accept_ranges + CRLF \
                             + "Content-Type:" + ' ' + content_type + CRLF \
                             + "Content-Length:" + ' ' + str(content_length) + CRLF

        response_header += CRLF
        return response_header



    def page(self):
        relative_url = self.relative_url()    

        if relative_url == '/':
            page = path + '/' + homepage
            f = open(page)
            page_file = f.read()
            f.close()
        else:
            try:
                page = path + relative_url + '.html'
                f = open(page)
                page_file = f.read()
                f.close()
            except IOError:
                try:
                    page = path + relative_url
                    f = open(page)
                    page_file = f.read()
                    f.close()
                except IOError:
                    try:
                        page = path + mapping[relative_url]
                        f = open(page)
                        page_file = f.read()
                        f.close()
                    except KeyError:
                        self.response_status_code = "404 Not Found"
                        page_file = "[COLUMBUS] 404 page %s not found" % relative_url
        return page_file