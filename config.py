import time
import utils
from config_methods import *

# inet_addr = "192.168.233.128"
inet_addr = "114.212.135.187"
path = '/home/user/webpages' 
homepage = 'app.html'
HTTPS = False

# mapping urls to relative pathes
mapping = {}

mapping['/googlehk'] = '/google_hk.htm'

mapping['/form/success'] = '/form_success.html'

# some urls needn't be mapped, for example,
# the following mappings can be ommited:
# mapping['/'] = 'app.html' (when app.html is homepage)
# mapping['/doc'] = '/doc.html'
# mapping['/doc'] = '/doc.htm'
# mapping['/about/us'] = '/about/us'
# mapping['/about/licence'] = '/about/licence.html'

# mapping the urls used in forms to suggest database used
# to the redirected urls
redirect = {}

redirect['/form/old/create/0'] = '/form/success'
redirect['/form/young/create/0'] = '/form/success'

##########################################################
https = []
https.append('/form')

# database configuration
db_type = 'mysql'
db_passwd = ''
db_name = 'expdb'
user_name = 'user'

# configuration for ssl
ssl_port = 4000
ssl_certfile = '/home/user/webpages/cert.pem'
ssl_keyfile = '/home/user/webpages/cert.pem'

# configuration for cookies setting
def cookie(name, value, tlength, path='/', domain=inet_addr):
    t = utils.gettime(tlength).split()
    expires = t[0] + ', ' + t[2] + ' ' + t[1] + ' ' + t[-1] + ' ' + t[-2] + ' GMT'

    cookie = name + '=' + value + '; ' + 'expires=' + expires + '; ' \
           + 'path=' + path + '; ' + 'domain=' + domain
    return cookie

cookies = {}

cookies['/'] = []
cookies['/'].append(cookie("rmk", "4EWrq!$RF^4#@!0pfsf@%!^^%//fasrsawqrfdd", 2))


# configuration for dealing with the posted data
# the methods are defined by user in config_methods.py
proc = {}
proc['/form/old/create/0'] = 'database'
proc['/form/young/create/0'] = 'database'
proc['/newqrcode.png'] = qrcode