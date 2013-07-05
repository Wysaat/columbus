from config import *

def header_p(header):
    header = header.strip()
    header_lines = header.split('\r\n')
    header_elements = [line.split() for line in header_lines]
    
    http_method, relative_url, http_version = header_elements[0]

    # a string containing all acceptable types
    header_elements = [element for element in header_elements if len(element) > 1]
    accepts = [element[1] for element in header_elements if
                   element[0].lower() == 'accept:']

    if relative_url == '/':
        page = path + '/' + homepage
        f = open(page)
        page_file = f.read()
    else:
        try:
            page = path + relative_url + '.html'
            f = open(page)
            page_file = f.read()
        except IOError:
            try:
                page = path + mapping[relative_url]
                f = open(page)
                page_file = f.read()
            except KeyError:
                page_file = "[COLUMBUS] 404 page %s not found" % relative_url

    return http_method, page_file, http_version