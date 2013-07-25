from config import *

CRLF = "\r\n"

class Header(object):
    def __init__(self, header):
        self.response_status_code = "200 OK"
        header, self.rest = header.split('\r\n\r\n')
        lines = header.split('\r\n')
        self.lines = [line.split() for line in lines]

    def content_first_part(self):
        content_first_part = self.rest
        return self.rest

    def http_method(self):
        http_method = self.lines[0][0]
        return http_method

    def relative_url(self):
        relative_url = self.lines[0][1]
        if relative_url != '/' and relative_url.endswith('/'):
            relative_url = relative_url.rstrip('/')
        return relative_url

    def http_version(self):
        http_version = self.lines[0][2]
        return http_version

    def accept_types(self):
        for line in self.lines:
            if 'accept:' == line[0].lower():
                accept_types = line[1]
                return accept_types
        return None

    def content_length(self):
        for line in self.lines:
            if 'content-length:' == line[0].lower():
                content_length= int(line[1])
                return content_length
        return None

    def response_header(self):
        response_header = self.http_version() + ' ' \
                        + self.response_status_code + CRLF

        if 'png' == self.relative_url().split('.')[-1]:
            content_type = "image/png"
            accept_ranges = "bytes"
            content_length = len(self.page())

            response_header +=  "Accept-Ranges:" + ' ' + accept_ranges + CRLF \
                             + "Content-Type:" + ' ' + content_type + CRLF \
                             + "Content-Length:" + ' ' + str(content_length) + CRLF

        if self.http_method() == 'POST':
            self.response_status_code = '302 Found'
            response_header  = self.http_version() + ' ' \
                             + self.response_status_code + CRLF
            response_header += "Location:" + ' ' + self.redirect_url() + CRLF

        print 'self.relative_url() is: ', self.relative_url()
        print 'cookies is: ', cookies
        if self.relative_url() in cookies:
            print 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'
            for cookie in cookies[self.relative_url()]:
                response_header += "Set-Cookie:" + ' ' + cookie + CRLF

        response_header += CRLF
        return response_header

    def redirect_url(self):
        if self.http_method() == 'POST':
            print
            print self.relative_url()
            print
            redirect_url = redirect[self.relative_url()]
            return redirect_url
        return None

    def db_table(self):
        if self.http_method() == 'POST' & proc[self.relative_url()] == 'database':
            ####### ....split('/')[0] is ''!!!!! #######
            db_table = self.relative_url().split('/')[2]
            return db_table
        return None

    def db_action(self):
        if self.http_method() == 'POST' & proc[self.relative_url()] == 'database':
            db_action = self.relative_url().split('/')[3]
            return db_action
        return None

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
                    page = path + relative_url + '.htm'
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